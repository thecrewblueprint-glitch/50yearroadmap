---
{
  "chunk_id": "kimi-batch-2026-07-05__md_handoff_bundle__01_google_calendar_affirmations_auto_refresh_scheduler_context.md__chunk-0001",
  "archive_id": "kimi-batch-2026-07-05",
  "archive_filename": "kimi-batch-2026-07-05.zip",
  "source_path": "md_handoff_bundle/01_google_calendar_affirmations_auto_refresh_scheduler_context.md",
  "chunk_index": 1,
  "chunk_count_for_source": 3,
  "char_start": 0,
  "char_end": 11959,
  "source_sha256": "b294d0089e7dd2a083c9d9312e4bc6d92801dc77b8f6c69857f972a594584aab",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

# Google Calendar Affirmations — Auto-Refresh, Scheduler, Audit/Handoff Context

Source file: `Pasted markdown(1).md`

---

Original URL: https://www.kimi.com/chat/19f2a3c6-9722-8725-8000-09e21adc4b62?chat_enter_method=history
Export Time: 7/5/2026, 5:09:46 PM

**[USER]**

sure

---

**[ASSISTANT]**

I'll wire automatic token refresh directly into the `GoogleCalendarService` class so expiry is handled transparently before every API call. This eliminates the need to manually call `/auth/google/refresh` before sync jobs.

* * *

## Updated `services/google_calendar.py`

```
from datetime import datetime, timedelta, date, timezone
from typing import Optional, Dict, Any, List

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request as GoogleRequest
from sqlalchemy.orm import Session

from app.models.google_account import GoogleAccount
from app.core.config import settings

class GoogleCalendarService:
    """
    Calendar service with automatic token refresh.
    Instantiate with a GoogleAccount ORM object; tokens refresh on demand.
    """

    def __init__(self, account: GoogleAccount, db: Session):
        self.account = account
        self.db = db
        self._credentials: Optional[Credentials] = None
        self._service: Optional[Any] = None

    # ─── Token Lifecycle ───────────────────────────────────────────────────────

    def _build_credentials(self) -> Credentials:
        """Create Credentials from stored tokens."""
        return Credentials(
            token=self.account.access_token,
            refresh_token=self.account.refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
            scopes=["https://www.googleapis.com/auth/calendar.events"],
        )

    def _is_token_expired(self) -> bool:
        """Check if the stored access token is expired or near expiry."""
        if not self.account.token_expiry:
            return True  # Unknown expiry = assume expired

        try:
            expiry = datetime.fromisoformat(self.account.token_expiry)
            # Refresh if expires within 5 minutes (clock skew buffer)
            return datetime.now(timezone.utc) >= (expiry - timedelta(minutes=5))
        except ValueError:
            return True

    def _refresh_if_needed(self) -> Credentials:
        """
        Return valid credentials, refreshing automatically if expired.
        Persists new tokens to the database.
        """
        credentials = self._build_credentials()

        if self._is_token_expired() and credentials.refresh_token:
            try:
                credentials.refresh(GoogleRequest())
                # Persist refreshed tokens
                self.account.access_token = credentials.token
                self.account.token_expiry = (
                    credentials.expiry.isoformat() if credentials.expiry else None
                )
                self.db.commit()
            except Exception as exc:
                raise RuntimeError(f"Failed to refresh Google token: {exc}") from exc

        self._credentials = credentials
        return credentials

    def _get_service(self):
        """Lazy-init the Calendar API service with fresh credentials."""
        if self._service is None:
            credentials = self._refresh_if_needed()
            self._service = build("calendar", "v3", credentials=credentials)
        return self._service

    # ─── Calendar Operations ─────────────────────────────────────────────────

    def list_calendars(self) -> Dict[str, Any]:
        """List calendars accessible to the user."""
        service = self._get_service()
        return service.calendarList().list().execute()

    def create_daily_affirmation_event(
        self,
        calendar_id: str,
        event_date: date,
        title: str,
        description: str,
        timezone: str = "UTC",
        all_day: bool = True,
    ) -> Dict[str, Any]:
        """
        Create a single calendar event for a daily affirmation.
        Automatically refreshes token if needed before the API call.
        """
        body = {
            "summary": title,
            "description": description,
        }

        if all_day:
            body["start"] = {"date": event_date.isoformat()}
            body["end"] = {"date": (event_date + timedelta(days=1)).isoformat()}
        else:
            start_dt = datetime.combine(event_date, datetime.min.time())
            end_dt = start_dt + timedelta(minutes=15)
            body["start"] = {"dateTime": start_dt.isoformat(), "timeZone": timezone}
            body["end"] = {"dateTime": end_dt.isoformat(), "timeZone": timezone}

        try:
            service = self._get_service()
            return (
                service.events()
                .insert(calendarId=calendar_id, body=body, sendUpdates="none")
                .execute()
            )
        except HttpError as exc:
            raise RuntimeError(f"Google Calendar event creation failed: {exc}") from exc

    def delete_event(self, calendar_id: str, event_id: str) -> None:
        """Delete a calendar event by Google event ID."""
        try:
            service = self._get_service()
            service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        except HttpError as exc:
            raise RuntimeError(f"Google Calendar delete failed: {exc}") from exc

    def update_event(
        self,
        calendar_id: str,
        event_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update an existing calendar event."""
        try:
            service = self._get_service()
            event = (
                service.events()
                .get(calendarId=calendar_id, eventId=event_id)
                .execute()
            )
            if title is not None:
                event["summary"] = title
            if description is not None:
                event["description"] = description
            return (
                service.events()
                .update(calendarId=calendar_id, eventId=event_id, body=event)
                .execute()
            )
        except HttpError as exc:
            raise RuntimeError(f"Google Calendar update failed: {exc}") from exc

    def batch_create_events(
        self,
        calendar_id: str,
        events_data: List[Dict[str, Any]],
        timezone: str = "UTC",
        all_day: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Create multiple events with automatic token refresh handled once.
        Returns list of created event dicts with Google event IDs.
        """
        results = []
        service = self._get_service()  # Refresh once before the loop

        for item in events_data:
            event = self.create_daily_affirmation_event(
                calendar_id=calendar_id,
                event_date=item["date"],
                title=item.get("title", "Daily Affirmation"),
                description=item["text"],
                timezone=timezone,
                all_day=all_day,
            )
            results.append({
                "date": item["date"],
                "google_event_id": event.get("id"),
                "status": "synced",
            })

        return results
```

* * *

## Updated `api/routes/calendar.py` (Using Auto-Refresh Service)

```
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.google_account import GoogleAccount
from app.models.affirmation import Affirmation
from app.models.calendar_event import CalendarEvent
from app.services.google_calendar import GoogleCalendarService
from app.services.affirmation_generator import generate_year_affirmations

router = APIRouter()

class CalendarSyncRequest(BaseModel):
    user_id: int
    year: int
    calendar_id: str = "primary"
    timezone: str = "UTC"
    all_day: bool = True

def sync_affirmations_for_user(
    db: Session,
    user_id: int,
    year: int,
    calendar_id: str,
    timezone: str,
    all_day: bool,
):
    """
    Background task: generate affirmations and sync to Google Calendar.
    Token refresh happens automatically inside GoogleCalendarService.
    """
    account = (
        db.query(GoogleAccount)
        .filter(GoogleAccount.user_id == user_id)
        .first()
    )
    if not account:
        raise RuntimeError("Google account not connected")

    # Service handles token refresh transparently
    calendar_service = GoogleCalendarService(account, db)

    # Verify calendar access (also triggers any needed refresh)
    try:
        calendar_service.list_calendars()
    except Exception as exc:
        raise RuntimeError(f"Cannot access Google Calendar: {exc}")

    # Generate affirmations
    affirmations = generate_year_affirmations(year)

    # Batch create with auto-refresh handled internally
    for item in affirmations:
        affirmation = Affirmation(
            user_id=user_id,
            affirmation_date=item["date"],
            text=item["text"],
            theme=item["theme"],
        )
        db.add(affirmation)
        db.flush()

        event = calendar_service.create_daily_affirmation_event(
            calendar_id=calendar_id,
            event_date=item["date"],
            title="Daily Affirmation",
            description=item["text"],
            timezone=timezone,
            all_day=all_day,
        )

        link = CalendarEvent(
            user_id=user_id,
            affirmation_id=affirmation.id,
            google_event_id=event.get("id"),
            calendar_id=calendar_id,
            status="synced",
        )
        db.add(link)

    db.commit()

@router.post("/sync")
async def sync_calendar(
    payload: CalendarSyncRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    Kick off a full-year sync. Returns immediately; work continues in background.
    """
    account = (
        db.query(GoogleAccount)
        .filter(GoogleAccount.user_id == payload.user_id)
        .first()
    )
    if not account:
        raise HTTPException(status_code=404, detail="Google account not connected")

    background_tasks.add_task(
        sync_affirmations_for_user,
        db,
        payload.user_id,
        payload.year,
        payload.calendar_id,
        payload.timezone,
        payload.all_day,
    )

    return {
        "message": "Calendar sync started",
        "user_id": payload.user_id,
        "year": payload.year,
        "calendar_id": payload.calendar_id,
    }

@router.get("/status/{user_id}")
def sync_status(user_id: int, db: Session = Depends(get_db)):
    """Check how many events are synced for a user."""
    count = (
        db.query(CalendarEvent)
        .filter(CalendarEvent.user_id == user_id)
        .count()
    )
    return {"user_id": user_id, "synced_events": count}
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
