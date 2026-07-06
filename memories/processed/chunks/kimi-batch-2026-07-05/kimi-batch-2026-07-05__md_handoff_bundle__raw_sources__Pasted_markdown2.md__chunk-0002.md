---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__raw_sources__Pasted_markdown2.md__chunk-0002",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/raw_sources/Pasted_markdown2.md",
  "chunk_index": 2,
  "chunk_count_for_source": 3,
  "char_start": 11366,
  "char_end": 23329,
  "source_sha256": "3a1cafb3f2daf6be934f1c6f450b9558e049cb38022242f1af11c901490f21a9",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

rn {"user_id": user_id, "synced_events": count}
```

* * *

## How Auto-Refresh Works

```
┌─────────────────┐     ┌─────────────────────────────┐     ┌─────────────────┐
│  Calendar Sync  │────▶│  GoogleCalendarService()    │────▶│  Check expiry   │
│  Route Called   │     │  (account + db session)     │     │  (within 5 min) │
└─────────────────┘     └─────────────────────────────┘     └─────────────────┘
                                                                  │
                                    ┌─────────────────────────────┘
                                    ▼
                            ┌───────────────┐
                            │ Token valid?  │
                            └───────┬───────┘
                              Yes │   │ No
                                  ▼   ▼
                            ┌────────┐  ┌─────────────────┐
                            │ Use it │  │ Refresh token   │
                            │        │  │ Update database │
                            └────────┘  │ Commit session  │
                                        └─────────────────┘
```

* * *

## Key Improvements

| Feature | Benefit |
| --- | --- |
| 5-minute expiry buffer | Prevents edge-case failures from clock skew or network latency |
| Lazy service init | Token only refreshes when an API call is actually made |
| Database commit on refresh | New tokens persisted immediately; no data loss if worker crashes |
| Batch loop reuses service | Single refresh check for 365 events, not 365 separate checks |
| No manual refresh endpoint needed | /auth/google/refresh becomes optional/debug-only |

* * *

## Optional: Proactive Health Check

Add a lightweight endpoint to verify token health without triggering a full sync:

```
@router.get("/health/{user_id}")
def calendar_health(user_id: int, db: Session = Depends(get_db)):
    account = db.query(GoogleAccount).filter(GoogleAccount.user_id == user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="No Google account linked")

    service = GoogleCalendarService(account, db)
    try:
        calendars = service.list_calendars()
        return {
            "status": "healthy",
            "token_refreshed": service._credentials.token != account.access_token,
            "calendar_count": len(calendars.get("items", [])),
        }
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Calendar API unhealthy: {exc}")
```

* * *

Your sync pipeline is now fully self-healing. The background worker can run on a schedule (APScheduler/Celery) and will automatically refresh tokens without manual intervention. Want me to draft the APScheduler integration for nightly sync jobs next?

---

**[USER]**

yes

---

**[ASSISTANT]**

I'll draft the APScheduler integration for nightly sync jobs, including retry logic, failure tracking, and a clean job registry. This will run as a separate worker process alongside your FastAPI app.

* * *

## `workers/scheduler.py`

```
"""
APScheduler-based background worker for affirmation sync jobs.
Runs as a standalone process: python -m app.workers.scheduler
"""

import logging
import sys
from datetime import datetime, timezone
from typing import Optional

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from sqlalchemy.orm import Session

# Adjust imports based on your project structure
from app.db.session import SessionLocal
from app.models.google_account import GoogleAccount
from app.models.calendar_event import CalendarEvent
from app.services.google_calendar import GoogleCalendarService
from app.services.affirmation_generator import generate_year_affirmations

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("affirmation_scheduler")

# ─── Job Registry ──────────────────────────────────────────────────────────────

class SyncJobRegistry:
    """Track job execution state for observability."""

    def __init__(self):
        self.last_run: Optional[datetime] = None
        self.last_status: Optional[str] = None
        self.events_synced_today: int = 0
        self.failures_today: int = 0

    def record_success(self, count: int):
        self.last_run = datetime.now(timezone.utc)
        self.last_status = "success"
        self.events_synced_today += count
        self.failures_today = 0

    def record_failure(self):
        self.last_run = datetime.now(timezone.utc)
        self.last_status = "failed"
        self.failures_today += 1

registry = SyncJobRegistry()

# ─── Core Sync Job ─────────────────────────────────────────────────────────────

def sync_user_affirmations(user_id: int, year: Optional[int] = None) -> dict:
    """
    Sync affirmations for a single user. Called by scheduler or manually.
    Returns summary dict for logging/monitoring.
    """
    db = SessionLocal()
    try:
        target_year = year or datetime.now(timezone.utc).year

        account = (
            db.query(GoogleAccount)
            .filter(GoogleAccount.user_id == user_id)
            .first()
        )

        if not account:
            logger.warning(f"[User {user_id}] No Google account linked. Skipping.")
            return {"user_id": user_id, "status": "skipped", "reason": "no_account"}

        # Check if already synced for this year
        existing_count = (
            db.query(CalendarEvent)
            .filter(
                CalendarEvent.user_id == user_id,
                CalendarEvent.calendar_id == account.calendar_id,
            )
            .count()
        )

        if existing_count >= 365:
            logger.info(f"[User {user_id}] Already synced ({existing_count} events). Skipping.")
            return {"user_id": user_id, "status": "skipped", "reason": "already_synced"}

        # Initialize service (auto-refreshes token if needed)
        calendar_service = GoogleCalendarService(account, db)

        # Verify calendar access
        try:
            calendar_service.list_calendars()
        except Exception as exc:
            logger.error(f"[User {user_id}] Calendar access failed: {exc}")
            return {"user_id": user_id, "status": "failed", "reason": "calendar_unavailable"}

        # Generate affirmations
        affirmations = generate_year_affirmations(target_year)
        logger.info(f"[User {user_id}] Generated {len(affirmations)} affirmations for {target_year}")

        # Sync with retry logic
        synced = 0
        failed = 0

        for item in affirmations:
            # Skip if already exists for this date
            existing = (
                db.query(CalendarEvent)
                .join(CalendarEvent.affirmation)
                .filter(
                    CalendarEvent.user_id == user_id,
                    CalendarEvent.affirmation.has(affirmation_date=item["date"]),
                )
                .first()
            )

            if existing:
                continue

            # Create with retry
            for attempt in range(3):
                try:
                    event = calendar_service.create_daily_affirmation_event(
                        calendar_id=account.calendar_id,
                        event_date=item["date"],
                        title="Daily Affirmation",
                        description=item["text"],
                        timezone="UTC",
                        all_day=True,
                    )

                    # Save to database
                    from app.models.affirmation import Affirmation

                    affirmation = Affirmation(
                        user_id=user_id,
                        affirmation_date=item["date"],
                        text=item["text"],
                        theme=item["theme"],
                    )
                    db.add(affirmation)
                    db.flush()

                    link = CalendarEvent(
                        user_id=user_id,
                        affirmation_id=affirmation.id,
                        google_event_id=event.get("id"),
                        calendar_id=account.calendar_id,
                        status="synced",
                    )
                    db.add(link)
                    db.commit()

                    synced += 1
                    break

                except Exception as exc:
                    logger.warning(
                        f"[User {user_id}] Attempt {attempt + 1}/3 failed for {item['date']}: {exc}"
                    )
                    if attempt == 2:  # Final attempt
                        failed += 1
                        # Log failure for manual review
                        logger.error(
                            f"[User {user_id}] Permanent failure for {item['date']}: {exc}"
                        )

        registry.record_success(synced)
        logger.info(
            f"[User {user_id}] Sync complete: {synced} created, {failed} failed, "
            f"{existing_count} pre-existing"
        )

        return {
            "user_id": user_id,
            "status": "success",
            "year": target_year,
            "synced": synced,
            "failed": failed,
            "pre_existing": existing_count,
        }

    except Exception as exc:
        registry.record_failure()
        logger.exception(f"[User {user_id}] Unhandled error in sync: {exc}")
        return {"user_id": user_id, "status": "error", "reason": str(exc)}

    finally:
        db.close()

def nightly_sync_job():
    """
    Scheduled job: find all users with Google accounts and sync their affirmations.
    Runs at 2:00 AM daily by default.
    """
    logger.info("=" * 60)
    logger.info("Starting nightly affirmation sync job")
    logger.info("=" * 60)

    db = SessionLocal()
    try:
        # Find all users with connected Google accounts
        accounts = db.query(GoogleAccount).all()
        logger.info(f"Found {len(accounts)} connected Google accounts")

        results = []
        for account in accounts:
            result = sync_user_affirmations(account.user_id)
            results.append(result)

        success_count = sum(1 for r in results if r["status"] == "success")
        skip_count = sum(1 for r in results if r["status"] == "skipped")
        fail_count = sum(1 for r in results if r["status"] in ("failed", "error"))

        logger.info("=" * 60)
        logger.info(
            f"Nightly sync complete: {success_count} succeeded, "
            f"{skip_count} skipped, {fail_count} failed"
        )
        logger.info("=" * 60)

    except Exception as exc:
        logger.exception(f"Critical failure in nightly sync: {exc}")
        registry.record_failure()

    finally:
        db.close()

# ─── Scheduler Setup ───────────────────────────────────────────────────────────

def job_listener(event):
    """Log job execution events."""
    if event.exception:
        logger.error(f"Job {event.job_id} crashed: {event.exception}")
    else:
        logger.info(f"Job {event.job_id} completed successfully")

def start_scheduler():
    """Initialize and start the background scheduler."""
    scheduler = BackgroundScheduler()

    # Nightly sync at 2:00 AM UTC
    scheduler.add_job(
        nightly_sync_job,
        trigger=CronTrigger(hour=2, minute=0),
        id="nightly_affirmation_sync",
        name="Sync affirmations for all users",
        replace_existing=True,
