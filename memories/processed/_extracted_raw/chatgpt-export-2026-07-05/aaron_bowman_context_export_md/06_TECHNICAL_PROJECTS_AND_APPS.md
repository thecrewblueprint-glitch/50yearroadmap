# Technical Projects and Apps

## Custom Invoice Generator

Known requested framework:

- custom invoice generator
- links to payment processor
- links to bank account
- likely integrations discussed: Stripe and Plaid
- output should include comprehensive architecture and step-by-step build guide
- security concerns: do not store raw card data; use processor-hosted/PCI-safer flows; encrypt banking tokens; use webhook verification and idempotency

Aaron later preferred:

- Android-only invoice app
- offline capability
- static invoice
- fixed positions
- paste text mapped into fields
- PDF only
- no drag/click builder

## 365-Day Affirmation Calendar App

Known context:

- app creates 365 all-day calendar events
- integrates with Google Calendar
- uses OAuth token refresh
- scheduler / APScheduler concepts were discussed
- background sync, token health checks, and calendar event creation were discussed

Important technical points from pasted handoff material:

- `GoogleCalendarService` should refresh tokens automatically before API calls.
- Stored refresh token and expiry need safe handling.
- Background tasks should not reuse request-scoped DB sessions.
- Scheduler should have graceful shutdown and prevent overlapping jobs.
- Sync should include duplicate prevention and retry handling.

## Private Task App

Known desired features:

- single-user private task app
- secure backend
- OpenRouter.ai or AI backend support
- task cleanup
- priority sorting
- risk flagging
- breaking tasks into steps
- daily plan generation
- API keys server-side only
- potential migration of reminders/tasks into this app later

## Database / Backend Ideas

Known discussions:

- backend apps can use AI
- sensitive business documents in an admin dashboard require secure design
- file/image upload to notes may be useful
- login/local upload/security concerns exist
- AWS Aurora/RDS/EC2 and database connection steps were discussed
- Laravel/RAG via cPanel was considered for long-term sturdy systems

## GitHub Workflow Context

Known preference:

- user often wants complete replacement files/packages, not snippets
- user does not want half-copies or “inject this into another piece”
- user wants full copy/paste-ready or downloadable artifacts

Repo references:

- `festival-atlas`
- `thecrewblueprint-glitch/festival-atlas`
- active branch often `research-version`
- stable `main` should not be touched unless explicitly requested

Important boundary:

- No repo changes should be made unless Aaron explicitly asks for that exact repo operation.
