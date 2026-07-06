---
{
  "chunk_id": "Perplexity-Batch-2026-07-05__Perplexity-create_the_framework_for_an_amazing_app_to_put_on_the_pi_token_app_store.md__chunk-0002",
  "archive_id": "Perplexity-Batch-2026-07-05",
  "archive_filename": "Perplexity-Batch-2026-07-05.zip",
  "source_path": "Perplexity-create_the_framework_for_an_amazing_app_to_put_on_the_pi_token_app_store.md",
  "chunk_index": 2,
  "chunk_count_for_source": 2,
  "char_start": 11387,
  "char_end": 22227,
  "source_sha256": "0cdb17287391b918f0356571b1515db47620f625f3c91eba0911344d5d02d64e",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

 TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
    FOREIGN KEY (worker_id) REFERENCES worker_profiles(id) ON DELETE CASCADE,
    FOREIGN KEY (business_id) REFERENCES business_profiles(id) ON DELETE CASCADE
);
```

- This is the “contract” row once a worker is hired.  
- `escrow_*` fields track Pi held for the job.

***

### 7. `milestones`

```sql
CREATE TABLE milestones (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_assignment_id BIGINT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NULL,
    amount DECIMAL(18,8) NOT NULL COMMENT 'Pi allocated to this milestone',
    status ENUM('pending','in_progress','submitted','approved','rejected') NOT NULL DEFAULT 'pending',
    due_date DATE NULL,
    submitted_at DATETIME NULL,
    reviewed_at DATETIME NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (job_assignment_id) REFERENCES job_assignments(id) ON DELETE CASCADE
);
```

- Work is broken into milestones for stepwise payment.

***

### 8. `payments` (Pi payment tracking)

```sql
CREATE TABLE payments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    payer_user_id BIGINT UNSIGNED NOT NULL,
    receiver_user_id BIGINT UNSIGNED NOT NULL,
    job_assignment_id BIGINT UNSIGNED NULL,
    milestone_id BIGINT UNSIGNED NULL,
    payment_type ENUM('deposit','milestone_payout','final_payout','refund','fee') NOT NULL,
    amount DECIMAL(18,8) NOT NULL COMMENT 'Pi',
    currency VARCHAR(10) NOT NULL DEFAULT 'PI',
    pi_payment_id VARCHAR(255) NULL COMMENT 'Pi Platform payment ID',
    pi_txid VARCHAR(255) NULL COMMENT 'Blockchain transaction ID',
    status ENUM('created','approved','completed','failed','refunded') NOT NULL DEFAULT 'created',
    memo TEXT NULL,
    metadata JSON NULL COMMENT 'extra info from SDK',
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (payer_user_id) REFERENCES users(id),
    FOREIGN KEY (receiver_user_id) REFERENCES users(id),
    FOREIGN KEY (job_assignment_id) REFERENCES job_assignments(id) ON DELETE SET NULL,
    FOREIGN KEY (milestone_id) REFERENCES milestones(id) ON DELETE SET NULL
);
```

- This table mirrors Pi’s payment flow: `created → approved → completed`.  
- You’ll update `pi_payment_id`, `pi_txid`, and `status` as you call Pi’s `/approve` and `/complete` endpoints.[1][2][3]

***

### 9. `escrow_ledger` (optional but recommended)

```sql
CREATE TABLE escrow_ledger (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_assignment_id BIGINT UNSIGNED NOT NULL,
    transaction_type ENUM('deposit','release','refund','adjustment') NOT NULL,
    amount DECIMAL(18,8) NOT NULL COMMENT 'Pi, positive for in, negative for out',
    balance_after DECIMAL(18,8) NOT NULL COMMENT 'Running escrow balance',
    related_payment_id BIGINT UNSIGNED NULL,
    notes TEXT NULL,
    created_at TIMESTAMP NULL,
    FOREIGN KEY (job_assignment_id) REFERENCES job_assignments(id) ON DELETE CASCADE,
    FOREIGN KEY (related_payment_id) REFERENCES payments(id) ON DELETE SET NULL
);
```

- Helps you audit escrow per job assignment.

***

### 10. `disputes`

```sql
CREATE TABLE disputes (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_assignment_id BIGINT UNSIGNED NOT NULL,
    opened_by_user_id BIGINT UNSIGNED NOT NULL,
    reason TEXT NOT NULL,
    status ENUM('open','under_review','resolved','closed') NOT NULL DEFAULT 'open',
    resolution TEXT NULL,
    resolved_by_admin_id BIGINT UNSIGNED NULL,
    opened_at TIMESTAMP NULL,
    resolved_at TIMESTAMP NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (job_assignment_id) REFERENCES job_assignments(id) ON DELETE CASCADE,
    FOREIGN KEY (opened_by_user_id) REFERENCES users(id),
    FOREIGN KEY (resolved_by_admin_id) REFERENCES users(id)
);
```

***

### 11. `reviews`

```sql
CREATE TABLE reviews (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    job_assignment_id BIGINT UNSIGNED NOT NULL,
    reviewer_user_id BIGINT UNSIGNED NOT NULL,
    reviewee_user_id BIGINT UNSIGNED NOT NULL,
    rating TINYINT UNSIGNED NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT NULL,
    is_visible BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (job_assignment_id) REFERENCES job_assignments(id) ON DELETE CASCADE,
    FOREIGN KEY (reviewer_user_id) REFERENCES users(id),
    FOREIGN KEY (reviewee_user_id) REFERENCES users(id),
    UNIQUE KEY unique_review_pair (job_assignment_id, reviewer_user_id)
);
```

***

### 12. `notifications`

```sql
CREATE TABLE notifications (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    type VARCHAR(100) NOT NULL COMMENT 'e.g. job_applied,milestone_approved,payment_received',
    title VARCHAR(255) NOT NULL,
    body TEXT NULL,
    data JSON NULL,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

***

## Key Relationships at a Glance

- `users` → `business_profiles` / `worker_profiles` (1:1)  
- `business_profiles` → `jobs` (1:many)  
- `jobs` → `job_applications` (1:many)  
- `jobs` → `job_assignments` (1:1 once hired)  
- `job_assignments` → `milestones`, `payments`, `escrow_ledger`, `disputes`, `reviews` (1:many)  
- `payments` links back to `users` (payer/receiver) and optionally to `job_assignments`/`milestones`.  

***

## Next Steps to Turn This Into Laravel Migrations

If you want, the next step can be:

- A set of ready-to-paste Laravel migration files (`create_users_table.php`, `create_jobs_table.php`, etc.).  
- Eloquent models with relationships (`User`, `Job`, `JobAssignment`, `Payment`, etc.).  
- A simple diagram (ERD) to visualize the schema.

Tell me which you’d like first: migrations, models, or a visual ERD.

---

**[USER]**

would it be a bad idea to put my web App on the pi network to run small tests?

---

**[ASSISTANT]**

Short answer: it’s not a bad idea at all—*if* you treat it as a **Testnet sandbox**, not a production Mainnet app. That’s literally how Pi expects developers to start.[1]

Below is a practical way to think about it, plus the main pros/cons and a safe rollout plan.

***

## Why testing on Pi is actually a good idea

Pi’s developer flow is built around:

- Registering an app in the **Developer Portal** (Pi Browser).  
- Choosing **Testnet vs Mainnet** at registration (you can’t switch networks later, so you create separate projects).[1]
- Running your web app in **sandbox mode** on your local/online host, then pointing the Pi SDK to Testnet.[1]
- Using the **Pi Testnet** (now with public RPC and smart-contract testing) to validate payments and logic before Mainnet.[2][3][4]

For WorkHub, that means you can:

- Test Pi login + payments with **zero real value**.  
- Iterate quickly on UX inside the Pi Browser.  
- Get comfortable with the **create → approve → complete** payment flow before going live.[5][6][7]

***

## Potential downsides (and how to avoid them)

1. **Confusing Testnet vs Mainnet projects**  
   - Risk: Mixing Testnet API keys/endpoints with Mainnet, causing payment failures.  
   - Fix: Create **two separate Developer Portal projects**:  
     - `WorkHub Testnet` → all your experiments.  
     - `WorkHub Mainnet` → only when you’re ready for real users and real π.[1]

2. **User expectations**  
   - Risk: Real Pioneers trying your app and expecting “real” earnings/payments while you’re still on Testnet.  
   - Fix:  
     - Clearly label the app as **“Testnet / Beta – No real Pi”**.  
     - Use a distinct name or subtitle (e.g., “WorkHub (Testnet)”).  
     - Don’t market it as a finished product; frame it as a developer test.

3. **Compliance with developer rules**  
   - Risk: Accidentally violating rules around payments, KYC, or Mainnet claims.  
   - Fix:  
     - Stay on **Testnet** until your payment flow, escrow logic, and dispute handling are solid.  
     - Read the latest **developer guidelines** (especially around Mainnet apps and multisig) before promoting beyond a small test group.[8][1]

4. **Overengineering before validation**  
   - Risk: Spending months building a full platform before you know if Pioneers actually want it.  
   - Fix: Use this test phase to validate just:  
     - Can a business post a job and pay a deposit in (test) π?  
     - Can a worker apply, get hired, complete a milestone, and receive test π?  
     - Do users understand the flow without a tutorial?

***

## A safe, smart rollout plan for WorkHub

### Phase 1 – Local + Sandbox (just you)

- Host your Laravel app on a dev URL (e.g., ngrok, Vercel, or your own server).  
- In the Pi Developer Portal (Testnet project):  
  - Set the **Development URL** to your localhost/ngrok URL.  
  - Enable **sandbox = true** in your frontend Pi SDK config.[1]
- Test:  
  - Login via Pi SDK.  
  - Create a dummy job, simulate a deposit, milestone payout, etc.  
  - Verify your `payments` table records `pi_payment_id`, `txid`, and status transitions.  

This is pure dev; no real users, no risk.

***

### Phase 2 – Small closed beta on Testnet

- Deploy your app to a stable URL (e.g., `workhub-test.yourdomain.com`).  
- In the Developer Portal:  
  - Set the **Production URL** to that domain.  
  - Add the **validation key** file to prove ownership.[1]
- Invite a small group (5–20 trusted Pioneers):  
  - Friends, other devs, or a small Telegram/Discord group.  
  - Make it clear: **“Testnet only – no real Pi value.”**  
- Observe:  
  - Where do they get stuck?  
  - Do they understand job posting, applying, and payments?  
  - Are there edge cases (failed payments, double applications, etc.)?

Use this to refine your database schema, UI, and error handling.

***

### Phase 3 – Mainnet pilot (only after Testnet is solid)

Once your Testnet version:

- Processes payments cleanly end-to-end.  
- Has basic dispute/review flows working.  
- Feels stable for your small beta group.

Then:

- Create a **new Mainnet project** in the Developer Portal.  
- Get a **Mainnet wallet** (with KYC/migration as required).[1]
- Update API keys and endpoints for Mainnet.  
- Launch a **very limited Mainnet pilot** (e.g., 1–2 real businesses, a handful of workers) with real but small π amounts.

***

## Bottom line

- It’s **not a bad idea** to put your web app on Pi for small tests; it’s exactly what the Testnet+Sandbox flow is for.[1]
- Just keep it clearly labeled as **Testnet/beta**, separate from any future Mainnet project, and use it to validate the core WorkHub flows before investing heavily.  
- If you want, I can sketch a minimal “Testnet-only” feature set (tables + screens) so you can ship a tiny but complete pilot quickly.
