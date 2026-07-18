# Website Update Handoff — Portfolio Disclaimer & Caption Framing

**To:** Deadhang Labor LLC website developer
**Site:** deadhanglaborllc.com (static HTML/CSS, Namecheap Stellar Plus / cPanel)
**Date:** 2026-07-18
**Priority:** Medium (legal/brand accuracy — do before further portfolio promotion)
**Estimated effort:** ~30–60 min

## Why

The Portfolio page lists trademarked event, festival, tour, and artist names
(Electric Forest, Lost Lands, Country Thunder, ELO, Super Bowl Host Committee,
Innings, etc.) with **no on-page disclaimer**, and several captions use
build/deploy/operations verbs that can imply Deadhang was solely responsible for a
structure or show rather than **providing independent labor support**.

Two fixes: (1) add a trademark/role disclaimer **on the portfolio page itself**,
and (2) lightly re-word captions to lead with the labor role. The Terms page
already has the underlying clause — this surfaces it where the names appear.

**Do NOT change:** the legal pages (`privacy.html`, `cookies.html`, `terms.html`)
— they are complete and correct. Keep the navy/gold brand and existing layout.

---

## Task 1 — Add the portfolio disclaimer (required)

**File:** `portfolio.html`
**Where:** at the bottom of the portfolio content, above the site footer (after the
last portfolio item / "Full Portfolio" grid).

**Markup to add** (match existing footer/disclaimer styling; a fallback inline
style is included — remove it if you wire it to the site's CSS):

```html
<!-- Portfolio credits disclaimer -->
<section class="portfolio-disclaimer" aria-label="Portfolio credits and trademark notice">
  <h2>About These Credits</h2>
  <p>
    All event, festival, tour, venue, and organization names and logos shown are
    trademarks of their respective owners and are referenced here for
    identification purposes only. Deadhang Labor LLC provided independent
    production labor and support services on these productions in an
    independent-contractor capacity. Their inclusion does not imply employment by,
    affiliation with, sponsorship by, or endorsement by any artist, tour, promoter,
    venue, or organizer.
  </p>
</section>
```

**Suggested styling** (only if not using an existing class — keep it subtle,
small, muted, consistent with the footer):

```css
.portfolio-disclaimer {
  max-width: 900px;
  margin: 2.5rem auto 0;
  padding: 1.25rem 1.5rem;
  border-top: 1px solid rgba(0,0,0,0.12);
  font-size: 0.85rem;
  line-height: 1.5;
  color: #6b7280; /* muted gray; adjust to brand */
}
.portfolio-disclaimer h2 {
  font-size: 0.95rem;
  margin: 0 0 0.5rem;
  letter-spacing: 0.02em;
}
```

**Acceptance:** the disclaimer is visible on the portfolio page, reads correctly
on mobile and desktop, and does not overlap the footer.

---

## Task 2 — Re-frame portfolio captions (recommended)

Lead each caption with the **labor/support role**. Keep it truthful — the owner
should confirm the actual role performed on each show before publishing. Use this
pattern:

> **[Event / Venue] — [task performed], labor support**

**Current → suggested** (confirm the exact role per show with the owner):

| Current caption | Suggested |
| --- | --- |
| ELO Spaceship Stage Build | ELO — spaceship stage build, labor support |
| Touring Concert Production | Touring concert production — labor support |
| Carousel Club – Electric Forest 2025 | Electric Forest 2025 — Carousel Club, labor support |
| Sherwood Court Video Wall Installation | Sherwood Court — video wall install, labor support |
| Electric Thunder Tent – Country Thunder | Country Thunder — Electric Thunder tent, labor support |
| Night Trip – Relentless Beats | Relentless Beats "Night Trip" — labor support |
| Innings Festival 2026 | Innings Festival 2026 — production labor support |
| Super Bowl Host Committee Event – San Jose 2026 | Super Bowl Host Committee event, San Jose 2026 — production labor support |
| Lost Lands Main Stage Deployment | Lost Lands — Main Stage, labor support |
| Country Thunder Spotlight Operations | Country Thunder — spotlight operation (labor support) |
| Country Jam Spotlight Operations | Country Jam — spotlight operation (labor support) |

**Acceptance:** no caption implies sole responsibility for a build/show or an
official relationship with the artist/organizer; captions match the owner-confirmed
role.

---

## Task 3 — Verify two open items (quick check)

- **Mobile hamburger menu** — confirm it opens/closes on tap across pages
  (previously flagged as a JS/CSS selector mismatch). Fix if still broken.
- **SSL/security hardening** — confirm HTTPS is enforced site-wide (HTTP → HTTPS
  redirect) and there is no mixed-content warning on any page.

---

## Definition of done

1. Portfolio disclaimer live on `portfolio.html`, responsive, brand-consistent.
2. Captions re-framed to lead with the labor role (owner-confirmed).
3. Hamburger menu and HTTPS verified.
4. No changes to the legal pages or the navy/gold brand.

## Notes

- Disclaimer language intentionally mirrors the existing Terms & Disclaimer clause
  for consistency — keep them aligned if either changes.
- Keep everything static; no new trackers, forms, or third-party scripts.
