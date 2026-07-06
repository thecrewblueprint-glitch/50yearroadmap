---
{
  "chunk_id": "Perplexity-Batch-2026-07-05__Perplexity-write_the_framework_needed_to_create_an_app_that_links_to_your_google_calender_and_cr__chunk-0002",
  "archive_id": "Perplexity-Batch-2026-07-05",
  "archive_filename": "Perplexity-Batch-2026-07-05.zip",
  "source_path": "Perplexity-write_the_framework_needed_to_create_an_app_that_links_to_your_google_calender_and_creates_365_DIFFERENT_positive_affirmations,_one_for_each_day_of_the_year.md",
  "chunk_index": 2,
  "chunk_count_for_source": 5,
  "char_start": 11384,
  "char_end": 23383,
  "source_sha256": "0619bdd89220a127013a2e660b1c64b0f37d833baa29a74bacdf9883355663c8",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

t you can use for the app that connects to Google Calendar and creates 365 unique affirmations. FastAPI’s `BackgroundTasks` is a good fit for kicking off sync work after the API responds, and Google Calendar event creation is done through `events.insert()`.[1][2]

## Stack

- FastAPI for the API layer.
- Google OAuth 2.0 for calendar connection.
- `google-api-python-client` plus Google auth libraries for Calendar access.
- PostgreSQL for persistence.
- SQLAlchemy or SQLModel for the ORM.
- APScheduler or Celery for scheduled generation/sync jobs.
- Redis if you want queued background workers.
- React or a simple admin dashboard for the frontend.

Google’s Calendar docs emphasize choosing the narrowest scope that fits the app, and `calendar.events` is the right level if your app needs to view and edit events.[3]

## Core folders

```text
app/
  main.py
  core/
    config.py
    security.py
  api/
    routes/
      auth.py
      calendar.py
      affirmations.py
  schemas/
    user.py
    affirmation.py
    calendar.py
  models/
    user.py
    google_account.py
    affirmation.py
    calendar_event.py
  services/
    google_oauth.py
    google_calendar.py
    affirmation_generator.py
    sync_service.py
  workers/
    tasks.py
  db/
    session.py
    base.py
```

This layout keeps your Google logic, business rules, and API routes separate so the app stays easy to maintain.

## API routes

### `POST /auth/google/start`
Begins the Google OAuth flow and returns the authorization URL.

### `GET /auth/google/callback`
Handles Google’s redirect, exchanges the code for tokens, and stores them securely.

### `POST /affirmations/generate`
Creates 365 affirmations for the current year or a chosen date range.

### `POST /calendar/sync`
Pushes the stored affirmations into Google Calendar as events.

### `GET /affirmations`
Returns the saved affirmations for preview or editing.

### `DELETE /calendar/resync`
Removes old generated events and rebuilds them.

FastAPI background tasks can handle small post-response jobs, but for syncing all 365 events, a real worker queue is better if you want retries and reliability.[1]

## Pydantic schemas

```python
from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str

class AffirmationCreate(BaseModel):
    date: date
    text: str
    theme: Optional[str] = None

class AffirmationOut(BaseModel):
    id: int
    date: date
    text: str
    theme: Optional[str] = None

    class Config:
        from_attributes = True

class CalendarSyncRequest(BaseModel):
    year: int
    calendar_id: Optional[str] = "primary"
```

These schemas define clean input and output contracts so your API stays predictable.

## Google Calendar service

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

class GoogleCalendarService:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.service = build("calendar", "v3", credentials=credentials)

    def create_affirmation_event(self, calendar_id: str, title: str, text: str, event_date):
        start_dt = datetime.combine(event_date, datetime.min.time()).replace(tzinfo=timezone.utc)
        end_dt = start_dt + timedelta(days=1)

        body = {
            "summary": title,
            "description": text,
            "start": {"date": event_date.isoformat()},
            "end": {"date": (event_date + timedelta(days=1)).isoformat()},
        }

        return self.service.events().insert(calendarId=calendar_id, body=body).execute()
```

Google Calendar event creation uses `events.insert()`, and the API supports event creation through that method.[2]

## Affirmation generator

```python
import random

THEMES = [
    "confidence", "focus", "gratitude", "discipline",
    "peace", "leadership", "growth", "resilience"
]

TEMPLATES = [
    "I am building {theme} with every action I take.",
    "Each day I grow stronger in {theme}.",
    "I trust myself to create a life of {theme}.",
    "My {theme} expands as I stay consistent."
]

def generate_affirmations(days=365):
    affirmations = []
    used = set()

    for day in range(days):
        while True:
            theme = random.choice(THEMES)
            text = random.choice(TEMPLATES).format(theme=theme)
            if text not in used:
                used.add(text)
                affirmations.append({
                    "day_index": day + 1,
                    "theme": theme,
                    "text": text
                })
                break

    return affirmations
```

This version is simple and easy to ship, and later you can replace it with AI-generated text or theme-based monthly batches.

## Main app file

```python
from fastapi import FastAPI, BackgroundTasks
from app.api.routes import auth, affirmations, calendar

app = FastAPI(title="Daily Affirmations Calendar")

app.include_router(auth.router, prefix="/auth")
app.include_router(affirmations.router, prefix="/affirmations")
app.include_router(calendar.router, prefix="/calendar")

@app.get("/health")
def health():
    return {"status": "ok"}
```

That gives you a clean entry point and keeps route registration centralized.

## Sync workflow

```python
from app.services.google_calendar import GoogleCalendarService
from app.services.affirmation_generator import generate_affirmations

def sync_year(user_id: int, credentials, calendar_id: str, year: int):
    service = GoogleCalendarService(credentials)
    affirmations = generate_affirmations(365)

    for idx, item in enumerate(affirmations):
        # map each item to a real date in the year
        pass
```

A production version should map each affirmation to a real date, save it first, then create events and store the returned Google event IDs so you can update or delete them later. The sync process is safer when the database is the source of truth.

## Practical MVP

For your first build, I would implement:
- Google OAuth login.
- Store refresh tokens.
- Generate 365 unique affirmations.
- Save them to PostgreSQL.
- Create one daily Google Calendar event per affirmation.
- Add a dashboard to edit, regenerate, and resync.

This is enough to validate the product without getting bogged down in advanced automation on day one.

Would you like me to draft the actual FastAPI project files next, including `main.py`, `auth.py`, `google_calendar.py`, and SQLAlchemy models?

---

**[USER]**

Yes, please draft the main.py and the auth.py routes next

---

**[ASSISTANT]**

Yes — below is a solid starter draft for `main.py` and `auth.py` built for FastAPI, with Google OAuth wiring and a clean path for calendar permissions. FastAPI supports `BackgroundTasks` for post-response work, and Google Calendar integration should be built around OAuth scopes plus the Calendar API’s event endpoints.[1][2][3]

## `main.py`

```python
from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(
    title="Daily Affirmations Calendar",
    version="0.1.0",
    description="Connect Google Calendar and generate 365 unique daily affirmations."
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
```

## `auth.py`

```python
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from starlette.config import Config
from starlette.datastructures import URL
from authlib.integrations.starlette_client import OAuth
import os

router = APIRouter()

config = Config(".env")

GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID", default=os.getenv("GOOGLE_CLIENT_ID"))
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET", default=os.getenv("GOOGLE_CLIENT_SECRET"))
GOOGLE_REDIRECT_URI = config(
    "GOOGLE_REDIRECT_URI",
    default=os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")
)

oauth = OAuth()
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile https://www.googleapis.com/auth/calendar.events"
    },
)

@router.get("/google/login")
async def google_login(request: Request):
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        raise HTTPException(status_code=500, detail="Google OAuth credentials not configured")

    redirect_uri = GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo")

        if not user_info:
            user_info = await oauth.google.parse_id_token(request, token)

        return {
            "message": "Google account connected successfully",
            "user": {
                "email": user_info.get("email"),
                "name": user_info.get("name"),
                "sub": user_info.get("sub"),
            },
            "token_present": True
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Google OAuth failed: {str(exc)}")
```

## What this gives you

This setup gives you a basic Google login flow, a health check endpoint, and the right place to expand into token storage and calendar syncing. The scope used here is write-oriented for calendar events, which fits an app that will create affirmation entries in the user’s calendar.[2][3]

## What to add next

You should next add:
- token persistence in PostgreSQL,
- a `google_calendar.py` service,
- an `affirmation_generator.py`,
- and a sync endpoint that queues the 365 event creations.

FastAPI’s background task pattern can help with small follow-up tasks after login, but the actual year-long sync is better handled in a dedicated service or worker.[1]

## Important setup notes

You’ll need:
- `authlib`,
- `httpx`,
- `python-dotenv`,
- `google-api-python-client`,
- `google-auth`,
- `google-auth-oauthlib`.

Google’s Python quickstart is the standard reference for setup patterns, and you’ll want to mirror its OAuth credential handling while adapting it to FastAPI instead of a command-line script.[4][5]

Would you like me to draft the next files as well — `google_calendar.py`, `affirmation_generator.py`, and the SQLAlchemy models?

---

**[USER]**

Yes, please draft the calendar service and affirmation logic

---

**[ASSISTANT]**

Absolutely — here’s a clean draft for the calendar service and affirmation logic, built for your FastAPI app. Google Calendar event creation is handled through `events.insert()`, and FastAPI’s background-task pattern works well for kicking off non-blocking sync work after a request is accepted.[1][2]

## `services/google_calendar.py`

```python
from datetime import datetime, timedelta, date
from typing import Optional, Dict, Any, List

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleCalendarService:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.service = build("calendar", "v3", credentials=self.credentials)

    def list_calendars(self) -> Dict[str, Any]:
        return self.service.calendarList().list().execute()

    def create_daily_affirmation_event(
        self,
        calendar_id: str,
        event_date: date,
        title: str,
        description: str,
        timezone: str = "UTC",
        all_day: bool = True,
    ) -> Dict[str, Any]:
        body = {
            "summary": title,
            "description": description,
        }

        if all_day:
            body["start"] = {"date": event_date.isoformat()}
