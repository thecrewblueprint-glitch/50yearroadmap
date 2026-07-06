Original URL: https://claude.ai/chat/99d71f82-32dc-4eab-9ca5-b5831de29006
Conversation Time: 6/6/2026, 9:42:25 PM
Export Time: 7/5/2026, 4:49:57 PM

**[USER]**

rewrite this and make it look pretty at least. I don't know why the hell it got made so shitty looking it was supposed to be a part of the admin dashboard we were building

---

**[ASSISTANT]**

1	---
     2	name: frontend-design
     3	description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
     4	license: Complete terms in LICENSE.txt
     5	---
     6	
     7	This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.
     8	
     9	The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.
    10	
    11	## Design Thinking
    12	
    13	Before coding, understand the context and commit to a BOLD aesthetic direction:
    14	- **Purpose**: What problem does this interface solve? Who uses it?
    15	- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
    16	- **Constraints**: Technical requirements (framework, performance, accessibility).
    17	- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?
    18	
    19	**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.
    20	
    21	Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
    22	- Production-grade and functional
    23	- Visually striking and memorable
    24	- Cohesive with a clear aesthetic point-of-view
    25	- Meticulously refined in every detail
    26	
    27	## Frontend Aesthetics Guidelines
    28	
    29	Focus on:
    30	- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
    31	- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
    32	- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
    33	- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
    34	- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.
    35	
    36	NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.
    37	
    38	Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.
    39	
    40	**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.
    41	
    42	Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
    43	     1	import base64
     2	import hashlib
     3	import io
     4	import json
     5	import mimetypes
     6	import os
     7	import secrets
     8	import sqlite3
     9	import time
    10	import zipfile
    11	from datetime import datetime, timedelta, timezone
    12	from functools import wraps
    13	from pathlib import Path
    14	
    15	from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    16	from flask import (
    17	    Flask,
    18	    abort,
    19	    flash,
    20	    redirect,
    21	    render_template,
    22	    request,
    23	    send_file,
    24	    session,
    25	    url_for,
    26	)
    27	from flask_wtf import CSRFProtect
    28	from werkzeug.security import check_password_hash, generate_password_hash
    29	from werkzeug.utils import secure_filename
    30	
    31	BASE_DIR = Path(__file__).resolve().parent
    32	INSTANCE_DIR = BASE_DIR / "instance"
    33	STORAGE_DIR = BASE_DIR / "storage"
    34	DB_PATH = INSTANCE_DIR / "dashboard.db"
    35	MAX_UPLOAD_BYTES = 25 * 1024 * 1024
    36	ALLOWED_EXTENSIONS = {"pdf", "docx", "xlsx", "png", "jpg", "jpeg", "webp", "txt", "csv"}
    37	
    38	INSTANCE_DIR.mkdir(exist_ok=True)
    39	STORAGE_DIR.mkdir(exist_ok=True)
    40	
    41	
    42	def load_or_create_secret(path: Path, size: int = 32) -> str:
    43	    if path.exists():
    44	        return path.read_text(encoding="utf-8").strip()
    45	    value = base64.urlsafe_b64encode(os.urandom(size)).decode("ascii")
    46	    path.write_text(value, encoding="utf-8")
    47	    try:
    48	        os.chmod(path, 0o600)
    49	    except OSError:
    50	        pass
    51	    return value
    52	
    53	
    54	app = Flask(__name__, instance_path=str(INSTANCE_DIR), instance_relative_config=True)
    55	app.config.update(
    56	    SECRET_KEY=os.environ.get("APP_SECRET_KEY") or load_or_create_secret(INSTANCE_DIR / ".app_secret"),
    57	    MAX_CONTENT_LENGTH=MAX_UPLOAD_BYTES,
    58	    SESSION_COOKIE_HTTPONLY=True,
    59	    SESSION_COOKIE_SAMESITE="Strict",
    60	    SESSION_COOKIE_SECURE=False,  # local HTTP only; set True behind HTTPS
    61	    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30),
    62	    WTF_CSRF_TIME_LIMIT=timedelta(hours=2),
    63	)
    64	csrf = CSRFProtect(app)
    65	
    66	MASTER_KEY_B64 = os.environ.get("DASHBOARD_MASTER_KEY") or load_or_create_secret(INSTANCE_DIR / ".master_key")
    67	try:
    68	    MASTER_KEY = base64.urlsafe_b64decode(MASTER_KEY_B64)
    69	except Exception as exc:
    70	    raise RuntimeError("Invalid DASHBOARD_MASTER_KEY") from exc
    71	if len(MASTER_KEY) != 32:
    72	    raise RuntimeError("DASHBOARD_MASTER_KEY must decode to exactly 32 bytes")
    73	
    74	
    75	def utc_now() -> str:
    76	    return datetime.now(timezone.utc).isoformat()
    77	
    78	
    79	def db_conn():
    80	    conn = sqlite3.connect(DB_PATH)
    81	    conn.row_factory = sqlite3.Row
    82	    conn.execute("PRAGMA foreign_keys = ON")
    83	    conn.execute("PRAGMA journal_mode = WAL")
    84	    return conn
    85	
    86	
    87	def init_db():
    88	    with db_conn() as db:
    89	        db.executescript(
    90	            """
    91	            CREATE TABLE IF NOT EXISTS users (
    92	                id INTEGER PRIMARY KEY AUTOINCREMENT,
    93	                username TEXT UNIQUE NOT NULL,
    94	                password_hash TEXT NOT NULL,
    95	                failed_attempts INTEGER NOT NULL DEFAULT 0,
    96	                locked_until TEXT,
    97	                created_at TEXT NOT NULL,
    98	                last_login_at TEXT
    99	            );
   100	
   101	            CREATE TABLE IF NOT EXISTS notes (
   102	                id INTEGER PRIMARY KEY AUTOINCREMENT,
   103	                title TEXT NOT NULL,
   104	                category TEXT NOT NULL DEFAULT 'General',
   105	                encrypted_body BLOB NOT NULL,
   106	                body_nonce BLOB NOT NULL,
   107	                created_by INTEGER NOT NULL,
   108	                created_at TEXT NOT NULL,
   109	                updated_at TEXT NOT NULL,
   110	                FOREIGN KEY(created_by) REFERENCES users(id)
   111	            );
   112	
   113	            CREATE TABLE IF NOT EXISTS attachments (
   114	                id INTEGER PRIMARY KEY AUTOINCREMENT,
   115	                note_id INTEGER NOT NULL,
   116	                original_name TEXT NOT NULL,
   117	                stored_name TEXT UNIQUE NOT NULL,
   118	                extension TEXT NOT NULL,
   119	                mime_type TEXT NOT NULL,
   120	                size_bytes INTEGER NOT NULL,
   121	                sha256 TEXT NOT NULL,
   122	                nonce BLOB NOT NULL,
   123	                created_by INTEGER NOT NULL,
   124	                created_at TEXT NOT NULL,
   125	                FOREIGN KEY(note_id) REFERENCES notes(id) ON DELETE CASCADE,
   126	                FOREIGN KEY(created_by) REFERENCES users(id)
   127	            );
   128	
   129	            CREATE TABLE IF NOT EXISTS audit_log (
   130	                id INTEGER PRIMARY KEY AUTOINCREMENT,
   131	                user_id INTEGER,
   132	                action TEXT NOT NULL,
   133	                target_type TEXT,
   134	                target_id INTEGER,
   135	                details TEXT,
   136	                ip_address TEXT,
   137	                created_at TEXT NOT NULL,
   138	                FOREIGN KEY(user_id) REFERENCES users(id)
   139	            );
   140	            """
   141	        )
   142	
   143	
   144	init_db()
   145	
   146	
   147	def encrypt_bytes(data: bytes) -> tuple[bytes, bytes]:
   148	    nonce = os.urandom(12)
   149	    ciphertext = AESGCM(MASTER_KEY).encrypt(nonce, data, None)
   150	    return nonce, ciphertext
   151	
   152	
   153	def decrypt_bytes(nonce: bytes, ciphertext: bytes) -> bytes:
   154	    return AESGCM(MASTER_KEY).decrypt(nonce, ciphertext, None)
   155	
   156	
   157	def audit(action: str, target_type: str | None = None, target_id: int | None = None, details: dict | None = None):
   158	    user_id = session.get("user_id")
   159	    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
   160	    with db_conn() as db:
   161	        db.execute(
   162	            "INSERT INTO audit_log (user_id, action, target_type, target_id, details, ip_address, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
   163	            (user_id, action, target_type, target_id, json.dumps(details or {}), ip, utc_now()),
   164	        )
   165	
   166	
   167	def user_count() -> int:
   168	    with db_conn() as db:
   169	        return db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
   170	
   171	
   172	def login_required(fn):
   173	    @wraps(fn)
   174	    def wrapper(*args, **kwargs):
   175	        if not session.get("user_id"):
   176	            return redirect(url_for("login"))
   177	        session.permanent = True
   178	        return fn(*args, **kwargs)
   179	    return wrapper
   180	
   181	
   182	@app.after_request
   183	def security_headers(response):
   184	    response.headers["X-Content-Type-Options"] = "nosniff"
   185	    response.headers["X-Frame-Options"] = "DENY"
   186	    response.headers["Referrer-Policy"] = "no-referrer"
   187	    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
   188	    response.headers["Content-Security-Policy"] = (
   189	        "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; "
   190	        "object-src 'none'; base-uri 'self'; frame-ancestors 'none'; form-action 'self'"
   191	    )
   192	    response.headers["Cache-Control"] = "no-store"
   193	    return response
   194	
   195	
   196	def validate_password(password: str) -> list[str]:
   197	    issues = []
   198	    if len(password) < 12:
   199	        issues.append("Password must be at least 12 characters.")
   200	    if not any(c.islower() for c in password):
   201	        issues.append("Password must contain a lowercase letter.")
   202	    if not any(c.isupper() for c in password):
   203	        issues.append("Password must contain an uppercase letter.")
   204	    if not any(c.isdigit() for c in password):
   205	        issues.append("Password must contain a number.")
   206	    if not any(not c.isalnum() for c in password):
   207	        issues.append("Password must contain a symbol.")
   208	    return issues
   209	
   210	
   211	@app.route("/setup", methods=["GET", "POST"])
   212	def setup():
   213	    if user_count() > 0:
   214	        return redirect(url_for("login"))
   215	    if request.method == "POST":
	< truncated lines 216-360 >
   361	
   362	
   363	@app.route("/notes/new", methods=["GET", "POST"])
   364	@login_required
   365	def note_new():
   366	    if request.method == "POST":
   367	        title = request.form.get("title", "").strip()
   368	        category = request.form.get("category", "General").strip() or "General"
   369	        body = request.form.get("body", "")
   370	        if not title:
   371	            flash("Title is required.", "error")
   372	            return render_template("note_form.html", note=None)
   373	        nonce, encrypted_body = encrypt_bytes(body.encode("utf-8"))
   374	        with db_conn() as db:
   375	            cur = db.execute(
   376	                "INSERT INTO notes (title, category, encrypted_body, body_nonce, created_by, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
   377	                (title, category, encrypted_body, nonce, session["user_id"], utc_now(), utc_now()),
   378	            )
   379	            note_id = cur.lastrowid
   380	        files = request.files.getlist("attachments")
   381	        errors = []
   382	        for f in files:
   383	            if f and f.filename:
   384	                try:
   385	                    save_attachment(f, note_id, session["user_id"])
   386	                except ValueError as exc:
   387	                    errors.append(f"{f.filename}: {exc}")
   388	        audit("note_created", "note", note_id, {"title": title, "category": category})
   389	        for err in errors:
   390	            flash(err, "error")
   391	        flash("Note created.", "success")
   392	        return redirect(url_for("note_view", note_id=note_id))
   393	    return render_template("note_form.html", note=None)
   394	
   395	
   396	@app.route("/notes/<int:note_id>")
   397	@login_required
   398	def note_view(note_id):
   399	    with db_conn() as db:
   400	        note = db.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
   401	        if not note:
   402	            abort(404)
   403	        attachments = db.execute("SELECT * FROM attachments WHERE note_id = ? ORDER BY created_at DESC", (note_id,)).fetchall()
   404	    try:
   405	        body = decrypt_bytes(note["body_nonce"], note["encrypted_body"]).decode("utf-8")
   406	    except Exception:
   407	        abort(500, "Unable to decrypt note. The master key may have changed.")
   408	    return render_template("note_view.html", note=note, body=body, attachments=attachments)
   409	
   410	
   411	@app.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
   412	@login_required
   413	def note_edit(note_id):
   414	    with db_conn() as db:
   415	        note = db.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
   416	    if not note:
   417	        abort(404)
   418	    if request.method == "POST":
   419	        title = request.form.get("title", "").strip()
   420	        category = request.form.get("category", "General").strip() or "General"
   421	        body = request.form.get("body", "")
   422	        if not title:
   423	            flash("Title is required.", "error")
   424	            return redirect(url_for("note_edit", note_id=note_id))
   425	        nonce, encrypted_body = encrypt_bytes(body.encode("utf-8"))
   426	        with db_conn() as db:
   427	            db.execute(
   428	                "UPDATE notes SET title = ?, category = ?, encrypted_body = ?, body_nonce = ?, updated_at = ? WHERE id = ?",
   429	                (title, category, encrypted_body, nonce, utc_now(), note_id),
   430	            )
   431	        for f in request.files.getlist("attachments"):
   432	            if f and f.filename:
   433	                try:
   434	                    save_attachment(f, note_id, session["user_id"])
   435	                except ValueError as exc:
   436	                    flash(f"{f.filename}: {exc}", "error")
   437	        audit("note_updated", "note", note_id, {"title": title})
   438	        flash("Note updated.", "success")
   439	        return redirect(url_for("note_view", note_id=note_id))
   440	    body = decrypt_bytes(note["body_nonce"], note["encrypted_body"]).decode("utf-8")
   441	    return render_template("note_form.html", note=note, body=body)
   442	
   443	
   444	@app.route("/notes/<int:note_id>/delete", methods=["POST"])
   445	@login_required
   446	def note_delete(note_id):
   447	    with db_conn() as db:
   448	        files = db.execute("SELECT stored_name FROM attachments WHERE note_id = ?", (note_id,)).fetchall()
   449	        db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
   450	    for row in files:
   451	        try:
   452	            (STORAGE_DIR / row["stored_name"]).unlink(missing_ok=True)
   453	        except OSError:
   454	            pass
   455	    audit("note_deleted", "note", note_id)
   456	    flash("Note deleted.", "success")
   457	    return redirect(url_for("dashboard"))
   458	
   459	
   460	@app.route("/attachments/<int:attachment_id>/<mode>")
   461	@login_required
   462	def attachment_get(attachment_id, mode):
   463	    if mode not in {"download", "preview"}:
   464	        abort(404)
   465	    with db_conn() as db:
   466	        item = db.execute("SELECT * FROM attachments WHERE id = ?", (attachment_id,)).fetchone()
   467	    if not item:
   468	        abort(404)
   469	    encrypted_path = STORAGE_DIR / item["stored_name"]
   470	    if not encrypted_path.exists():
   471	        abort(404)
   472	    try:
   473	        data = decrypt_bytes(item["nonce"], encrypted_path.read_bytes())
   474	    except Exception:
   475	        abort(500, "Unable to decrypt attachment. The master key may have changed.")
   476	    audit("attachment_accessed", "attachment", attachment_id, {"mode": mode})
   477	    inline_allowed = item["extension"] in {"pdf", "png", "jpg", "jpeg", "webp", "txt", "csv"}
   478	    as_attachment = mode == "download" or not inline_allowed
   479	    return send_file(
   480	        io.BytesIO(data),
   481	        mimetype=item["mime_type"],
   482	        as_attachment=as_attachment,
   483	        download_name=item["original_name"],
   484	        max_age=0,
   485	    )
   486	
   487	
   488	@app.route("/attachments/<int:attachment_id>/delete", methods=["POST"])
   489	@login_required
   490	def attachment_delete(attachment_id):
   491	    with db_conn() as db:
   492	        item = db.execute("SELECT * FROM attachments WHERE id = ?", (attachment_id,)).fetchone()
   493	        if not item:
   494	            abort(404)
   495	        db.execute("DELETE FROM attachments WHERE id = ?", (attachment_id,))
   496	    (STORAGE_DIR / item["stored_name"]).unlink(missing_ok=True)
   497	    audit("attachment_deleted", "attachment", attachment_id, {"name": item["original_name"]})
   498	    flash("Attachment deleted.", "success")
   499	    return redirect(url_for("note_view", note_id=item["note_id"]))
   500	
   501	
   502	@app.route("/audit")
   503	@login_required
   504	def audit_view():
   505	    with db_conn() as db:
   506	        logs = db.execute(
   507	            """
   508	            SELECT a.*, u.username
   509	            FROM audit_log a
   510	            LEFT JOIN users u ON u.id = a.user_id
   511	            ORDER BY a.created_at DESC
   512	            LIMIT 500
   513	            """
   514	        ).fetchall()
   515	    return render_template("audit.html", logs=logs)
   516	
   517	
   518	@app.route("/settings", methods=["GET", "POST"])
   519	@login_required
   520	def settings():
   521	    if request.method == "POST":
   522	        current = request.form.get("current_password", "")
   523	        new = request.form.get("new_password", "")
   524	        confirm = request.form.get("confirm_password", "")
   525	        with db_conn() as db:
   526	            user = db.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()
   527	            if not check_password_hash(user["password_hash"], current):
   528	                flash("Current password is incorrect.", "error")
   529	                return render_template("settings.html")
   530	            issues = validate_password(new)
   531	            if new != confirm:
   532	                issues.append("New passwords do not match.")
   533	            if issues:
   534	                for issue in issues:
   535	                    flash(issue, "error")
   536	                return render_template("settings.html")
   537	            db.execute("UPDATE users SET password_hash = ? WHERE id = ?", (generate_password_hash(new, method="scrypt"), session["user_id"]))
   538	        audit("password_changed", "user", session["user_id"])
   539	        session.clear()
   540	        flash("Password changed. Sign in again.", "success")
   541	        return redirect(url_for("login"))
   542	    return render_template("settings.html")
   543	
   544	
   545	@app.route("/backup", methods=["POST"])
   546	@login_required
   547	def backup():
   548	    manifest = {
   549	        "app": "Deadhang Secure Dashboard",
   550	        "created_at": utc_now(),
   551	        "format_version": 1,
   552	        "encrypted": True,
   553	    }
   554	    raw_zip = io.BytesIO()
   555	    with zipfile.ZipFile(raw_zip, "w", zipfile.ZIP_DEFLATED) as zf:
   556	        zf.writestr("manifest.json", json.dumps(manifest, indent=2))
   557	        zf.write(DB_PATH, "instance/dashboard.db")
   558	        for path in STORAGE_DIR.glob("*.bin"):
   559	            zf.write(path, f"storage/{path.name}")
   560	    nonce, ciphertext = encrypt_bytes(raw_zip.getvalue())
   561	    payload = b"DHBK1" + nonce + ciphertext
   562	    audit("backup_created", "system", None, {"size": len(payload)})
   563	    filename = f"deadhang-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.dhbackup"
   564	    return send_file(io.BytesIO(payload), as_attachment=True, download_name=filename, mimetype="application/octet-stream")
   565	
   566	
   567	@app.errorhandler(413)
   568	def too_large(_):
   569	    flash("Upload exceeds the 25 MB request limit.", "error")
   570	    return redirect(request.referrer or url_for("dashboard"))
   571	
   572	
   573	if __name__ == "__main__":
   574	    app.run(host="127.0.0.1", port=5050, debug=False)
   575	Good — I've got the full picture now. The existing CSS is functional but basic as hell — flat panels, generic Arial, no real hierarchy or polish. I'm going to rebuild `style.css` and all the templates to match the dark-gold Deadhang brand identity you've already established, with proper visual weight, typography, and a dashboard that actually looks like it belongs in a professional operation.{"returncode":0,"stdout":"done\n","stderr":""}{"returncode":0,"stdout":"style.css written\n","stderr":""}{"returncode":0,"stdout":"base.html done\n","stderr":""}{"returncode":0,"stdout":"auth templates done\n","stderr":""}{"returncode":0,"stdout":"dashboard done\n","stderr":""}{"returncode":0,"stdout":"note_form done\n","stderr":""}{"returncode":0,"stdout":"note_view done\n","stderr":""}{"returncode":0,"stdout":"settings done\n","stderr":""}{"returncode":0,"stdout":"audit done\n","stderr":""}{"returncode":0,"stdout":"-rw-r--r-- 1 root root 1.3K Jun  7 01:45 /home/claude/audit.html\n-rw-r--r-- 1 root root 1.7K Jun  7 01:44 /home/claude/base.html\n-rw-r--r-- 1 root root 1.9K Jun  7 01:44 /home/claude/dashboard.html\n-rw-r--r-- 1 root root  831 Jun  7 01:44 /home/claude/login.html\n-rw-r--r-- 1 root root 1.6K Jun  7 01:44 /home/claude/note_form.html\n-rw-r--r-- 1 root root 2.2K Jun  7 01:44 /home/claude/note_view.html\n-rw-r--r-- 1 root root 1.7K Jun  7 01:45 /home/claude/settings.html\n-rw-r--r-- 1 root root 1.3K Jun  7 01:44 /home/claude/setup.html\n-rw-r--r-- 1 root root  15K Jun  7 01:43 /home/claude/style.css\n","stderr":""}{"returncode":0,"stdout":"all copied to outputs\n","stderr":""}All 9 files are rebuilt. Drop them into your Flask `templates/` and `static/` folders as-is, replacing the originals — no changes to `app.py` needed.

Here's what changed and why:

**Typography** — swapped Arial out for **Barlow Condensed** (headers/eyebrows), **Barlow** (body), and **JetBrains Mono** (code, hashes, timestamps). Makes it feel like a real tool, not a default browser form.

**Color system** — kept your `#0b0d10` / `#f6c65b` Deadhang palette but added proper layering: `--bg`, `--surface`, `--panel`, `--panel2` for actual depth instead of everything being the same flat dark.

**Stat cards** — the dashboard numbers now have proper visual weight with a gold accent bar at the bottom of each card. The values use the condensed display font at a proper scale.

**Note cards** — added a gold left-border reveal on hover, subtle lift animation, and consistent category label treatment.

**Forms** — inputs have gold focus rings (`box-shadow: 0 0 0 3px rgba(246,198,91,.12)`), fields are properly labeled at small uppercase, and the two-column title/category layout on the note form is cleaner.

**Audit log** — action badges styled with monospace font, timestamps dimmed appropriately, sticky header on the table.

**Base grid texture** — very subtle gold-tinted grid overlay on the body via `::before` pseudo-element. Adds depth without noise.

The `note_form.html` has one layout addition — title and category are now side-by-side in a 2fr/1fr grid. If that causes any Jinja issues with your current setup, just let me know and I'll flatten it back.

---

**[USER]**

no. work those into this app: 

also.. anything that is completed needs to be stored into the apps memory, so don't let it just disappear. and i need to be able to add documents straight into the notes so if a task says (get a copy of your articles of organization) i can securely put my articles straight into the notes hit complete and then they just sit in the app undisturbed and encrypted until i need them
just in case i ever lose  my copies >

---

**[ASSISTANT]**

Looking at this, you want to integrate the Vault's encrypted document storage directly into the Task Command Center — so completed tasks with attached documents become a secure, browsable archive. Let me read the app code carefully before touching anything.3.9M	/mnt/skills/public
1.1M	/mnt/skills/public/docx
155K	/mnt/skills/public/docx.skill
1.5K	/mnt/skills/public/docx/LICENSE.txt
20K	/mnt/skills/public/docx/SKILL.md
1.1M	/mnt/skills/public/docx/scripts
16K	/mnt/skills/public/file-reading
6.0K	/mnt/skills/public/file-reading.skill
1.5K	/mnt/skills/public/file-reading/LICENSE.txt
14K	/mnt/skills/public/file-reading/SKILL.md
15K	/mnt/skills/public/frontend-design
6.0K	/mnt/skills/public/frontend-design.skill
10K	/mnt/skills/public/frontend-design/LICENSE.txt
4.5K	/mnt/skills/public/frontend-design/SKILL.md
60K	/mnt/skills/public/pdf
18K	/mnt/skills/public/pdf-reading
8.0K	/mnt/skills/public/pdf-reading.skill
1.5K	/mnt/skills/public/pdf-reading/LICENSE.txt
5.5K	/mnt/skills/public/pdf-reading/REFERENCE.md
11K	/mnt/skills/public/pdf-reading/SKILL.md
22K	/mnt/skills/public/pdf.skill
12K	/mnt/skills/public/pdf/FORMS.md
1.5K	/mnt/skills/public/pdf/LICENSE.txt
17K	/mnt/skills/public/pdf/REFERENCE.md
8.0K	/mnt/skills/public/pdf/SKILL.md
22K	/mnt/skills/public/pdf/scripts
1.2M	/mnt/skills/public/pptx
161K	/mnt/skills/public/pptx.skill
1.5K	/mnt/skills/public/pptx/LICENSE.txt
11K	/mnt/skills/public/pptx/SKILL.md
7.0K	/mnt/skills/public/pptx/editing.md
15K	/mnt/skills/public/pptx/pptxgenjs.md
1.1M	/mnt/skills/public/pptx/scripts
3.0K	/mnt/skills/public/product-self-knowledge
1.5K	/mnt/skills/public/product-self-knowledge.skill
3.0K	/mnt/skills/public/product-self-knowledge/SKILL.md
1.1M	/mnt/skills/public/xlsx
148K	/mnt/skills/public/xlsx.skill
1.5K	/mnt/skills/public/xlsx/LICENSE.txt
12K	/mnt/skills/public/xlsx/SKILL.md
1.1M	/mnt/skills/public/xlsx/scripts
     1	---
     2	name: frontend-design
     3	description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
     4	license: Complete terms in LICENSE.txt
     5	---
     6	
     7	This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.
     8	
     9	The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.
    10	
    11	## Design Thinking
    12	
    13	Before coding, understand the context and commit to a BOLD aesthetic direction:
    14	- **Purpose**: What problem does this interface solve? Who uses it?
    15	- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
    16	- **Constraints**: Technical requirements (framework, performance, accessibility).
    17	- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?
    18	
    19	**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.
    20	
    21	Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
    22	- Production-grade and functional
    23	- Visually striking and memorable
    24	- Cohesive with a clear aesthetic point-of-view
    25	- Meticulously refined in every detail
    26	
    27	## Frontend Aesthetics Guidelines
    28	
    29	Focus on:
    30	- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
    31	- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
    32	- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
    33	- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
    34	- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.
    35	
    36	NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.
    37	
    38	Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.
    39	
    40	**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.
    41	
    42	Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
    43	Good. Now I have a clear picture of everything. Let me plan what needs to happen before writing a single line:

**What you actually need:**
1. The Vault's Deadhang aesthetic applied to the Task Command Center (the HTML app in document 15)
2. A **secure document vault built into the task app** — attach files to tasks, encrypt them in the browser (AES-256-GCM using Web Crypto API, no server needed), store in localStorage as base64 ciphertext
3. Completed tasks with attachments go to a **Completed Archive** — they don't disappear, they become a searchable encrypted record
4. A master key system with export/backup — so files survive even if you clear localStorage

This is a substantial build. The HTML file in document 15 is already ~4000 lines. I'm going to write a full upgraded version with all of this integrated cleanly.{"returncode":0,"stdout":"608 /mnt/user-data/uploads/audit.html\nREADME.md\n_gitignore\n_gitkeep\napp.py\naudit.html\nbase.html\ndashboard.html\nlogin.html\nnote_form.html\nnote_view.html\nrequirements.txt\nrestore_backup.py\nsettings.html\nsetup.html\nstart_mac_linux.sh\nstart_windows.bat\nstyle.css\n","stderr":""}Command argument is 153_314 bytes, exceeding the 100_000-byte per-argument limit. For large content, pipe via stdin or use a file-write API instead of embedding the content inline in the command. Argument preview: 'cat > /home/claude/task_app.html << \'HTMLEOF\'\n<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1.0">\n<title>Deadhang · Tas'

---

**[ASSISTANT]**

Looking at what you've got and what you need — you want the Deadhang dark gold theme applied to this command center, completed tasks stored persistently in memory (not just flagged), and the ability to attach/embed documents directly into task notes with encryption. Let me build this out properly.3.9M	/mnt/skills/public
1.1M	/mnt/skills/public/docx
155K	/mnt/skills/public/docx.skill
1.5K	/mnt/skills/public/docx/LICENSE.txt
20K	/mnt/skills/public/docx/SKILL.md
1.1M	/mnt/skills/public/docx/scripts
16K	/mnt/skills/public/file-reading
6.0K	/mnt/skills/public/file-reading.skill
1.5K	/mnt/skills/public/file-reading/LICENSE.txt
14K	/mnt/skills/public/file-reading/SKILL.md
15K	/mnt/skills/public/frontend-design
6.0K	/mnt/skills/public/frontend-design.skill
10K	/mnt/skills/public/frontend-design/LICENSE.txt
4.5K	/mnt/skills/public/frontend-design/SKILL.md
60K	/mnt/skills/public/pdf
18K	/mnt/skills/public/pdf-reading
8.0K	/mnt/skills/public/pdf-reading.skill
1.5K	/mnt/skills/public/pdf-reading/LICENSE.txt
5.5K	/mnt/skills/public/pdf-reading/REFERENCE.md
11K	/mnt/skills/public/pdf-reading/SKILL.md
22K	/mnt/skills/public/pdf.skill
12K	/mnt/skills/public/pdf/FORMS.md
1.5K	/mnt/skills/public/pdf/LICENSE.txt
17K	/mnt/skills/public/pdf/REFERENCE.md
8.0K	/mnt/skills/public/pdf/SKILL.md
22K	/mnt/skills/public/pdf/scripts
1.2M	/mnt/skills/public/pptx
161K	/mnt/skills/public/pptx.skill
1.5K	/mnt/skills/public/pptx/LICENSE.txt
11K	/mnt/skills/public/pptx/SKILL.md
7.0K	/mnt/skills/public/pptx/editing.md
15K	/mnt/skills/public/pptx/pptxgenjs.md
1.1M	/mnt/skills/public/pptx/scripts
3.0K	/mnt/skills/public/product-self-knowledge
1.5K	/mnt/skills/public/product-self-knowledge.skill
3.0K	/mnt/skills/public/product-self-knowledge/SKILL.md
1.1M	/mnt/skills/public/xlsx
148K	/mnt/skills/public/xlsx.skill
1.5K	/mnt/skills/public/xlsx/LICENSE.txt
12K	/mnt/skills/public/xlsx/SKILL.md
1.1M	/mnt/skills/public/xlsx/scripts
This is a substantial rebuild — complete reskin + secure document attachment system + persistent completed task storage. I'm going to build this as a standalone HTML artifact with the full Deadhang dark theme and all three new systems baked in.# Imagine — Visual Creation Suite

## Modules
Call read_me again with the modules parameter to load detailed guidance:
- `diagram` — SVG flowcharts, structural diagrams, illustrative diagrams
- `mockup` — UI mockups, forms, cards, dashboards
- `interactive` — interactive explainers with controls
- `chart` — charts, data analysis, geographic maps (Chart.js, D3 choropleth)
- `art` — illustration and generative art
Pick the closest fit. The module includes all relevant design guidance.

**Complexity budget — hard limits:**
- Box subtitles: ≤5 words. Detail goes in click-through (`sendPrompt`) or the prose below — not the box.
- Colors: ≤2 ramps per diagram. If colors encode meaning (states, tiers), add a 1-line legend. Otherwise use one neutral ramp.
- Horizontal tier: ≤4 boxes at full width (~140px each). 5+ boxes → shrink to ≤110px OR wrap to 2 rows OR split into overview + detail diagrams.

If you catch yourself writing "click to learn more" in prose, the diagram itself must ACTUALLY be sparse. Don't promise brevity then front-load everything.

**Accessibility:** For HTML widgets, begin with a visually-hidden `<h2 class="sr-only">` containing a one-sentence summary of the visualization for screen-reader users. (SVG widgets use `role="img"` with `<title>` and `<desc>` instead — see SVG setup.)

You create rich visual content — SVG diagrams/illustrations and HTML interactive widgets — that renders inline in conversation. The best output feels like a natural extension of the chat.

## Core Design System

These rules apply to ALL use cases.

### Philosophy
- **Seamless**: Users shouldn't notice where claude.ai ends and your widget begins.
- **Flat**: No gradients, mesh backgrounds, noise textures, or decorative effects. Clean flat surfaces.
- **Compact**: Show the essential inline. Explain the rest in text.
- **Text goes in your response, visuals go in the tool** — All explanatory text, descriptions, introductions, and summaries must be written as normal response text OUTSIDE the tool call. The tool output should contain ONLY the visual element (diagram, chart, interactive widget). Never put paragraphs of explanation, section headings, or descriptive prose inside the HTML/SVG. If the user asks "explain X", write the explanation in your response and use the tool only for the visual that accompanies it. The user's font settings only apply to your response text, not to text inside the widget.

### Streaming
Output streams token-by-token. Structure code so useful content appears early.
- **HTML**: `<style>` (short) → content HTML → `<script>` last.
- **SVG**: `<defs>` (markers) → visual elements immediately.
- Prefer inline `style="..."` over `<style>` blocks — inputs/controls must look correct mid-stream.
- Keep `<style>` under ~15 lines. Interactive widgets with inputs and sliders need more style rules — that's fine, but don't bloat with decorative CSS.
- Gradients, shadows, and blur flash during streaming DOM diffs. Use solid flat fills instead.

### Rules
- No `<!-- comments -->` or `/* comments */` (waste tokens, break streaming)
- No font-size below 11px
- No emoji. Icons = Tabler **outline** webfont (5800+, already loaded): `<i class="ti ti-home"></i>`. Outline only — never use `-filled` suffixes (`ti-heart-filled` etc. are not loaded and will render blank). Inherits color + font-size from parent. Decorative icons get `aria-hidden="true"`; icon-only buttons get `aria-label`. Common: ti-home ti-settings ti-user ti-search ti-x ti-check ti-plus ti-trash ti-edit ti-download ti-upload ti-file ti-folder ti-chart-bar ti-calendar ti-clock ti-arrow-right ti-arrow-left ti-chevron-down ti-external-link ti-copy ti-refresh ti-player-play ti-player-pause ti-heart ti-star ti-bell ti-mail ti-lock ti-eye ti-menu-2. Don't hand-draw icon SVG paths.
- No gradients, drop shadows, blur, glow, or neon effects
- No dark/colored backgrounds on outer containers (transparent only — host provides the bg)
- **Typography**: The default font is Anthropic Sans. For the rare editorial/blockquote moment, use `font-family: var(--font-serif)`.
- **Headings**: h1 = 22px, h2 = 18px, h3 = 16px — all `font-weight: 500`. Heading color is pre-set to `var(--color-text-primary)` — don't override it. Body text = 16px, weight 400, `line-height: 1.7`. **Two weights only: 400 regular, 500 bold.** Never use 600 or 700 — they look heavy against the host UI.
- **Sentence case** always. Never Title Case, never ALL CAPS. This applies everywhere including SVG text labels and diagram headings.
- **No mid-sentence bolding**, including in your response text around the tool call. Entity names, class names, function names go in `code style` not **bold**. Bold is for headings and labels only.
- The widget container is `display: block; width: 100%`. Your HTML fills it naturally — no wrapper div needed. Just start with your content directly. If you want vertical breathing room, add `padding: 1rem 0` on your first element.
- Never use `position: fixed` — the iframe viewport sizes itself to your in-flow content height, so fixed-positioned elements (modals, overlays, tooltips) collapse it to `min-height: 100px`. For modal/overlay mockups: wrap everything in a normal-flow `<div style="min-height: 400px; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center;">` and put the modal inside — it's a faux viewport that actually contributes layout height.
- No DOCTYPE, `<html>`, `<head>`, or `<body>` — just content fragments.
- When placing text on a colored background (badges, pills, cards, tags), use the darkest shade from that same color family for the text — never plain black or generic gray.
- **Corners**: use `border-radius: var(--border-radius-md)` (or `-lg` for cards) in HTML. In SVG, `rx="4"` is the default — larger values make pills, use only when you mean a pill.
- **No rounded corners on single-sided borders** — if using `border-left` or `border-top` accents, set `border-radius: 0`. Rounded corners only work with full borders on all sides.
- **No titles or prose inside the tool output** — see Philosophy above.
- **Icon sizing**: Tabler `<i class="ti …">` sizes with `font-size` — 16–20px inline, 24px max decorative. For one-off inline SVG icons, set `width`/`height` explicitly (same limits).
- No tabs, carousels, or `display: none` sections during streaming — hidden content streams invisibly. Show all content stacked vertically. (Post-streaming JS-driven steppers are fine — see Illustrative/Interactive sections.)
- No nested scrolling — auto-fit height.
- Scripts execute after streaming — load libraries via `<script src="https://cdnjs.cloudflare.com/ajax/libs/...">` (UMD globals), then use the global in a plain `<script>` that follows.
- **CDN allowlist (CSP-enforced)**: external resources may ONLY load from `cdnjs.cloudflare.com`, `esm.sh`, `cdn.jsdelivr.net`, `unpkg.com`, `fonts.googleapis.com`, `fonts.gstatic.com`. All other origins are blocked by the sandbox — the request silently fails.

### CSS Variables
**Backgrounds**: `--color-background-primary` (white), `-secondary` (surfaces), `-tertiary` (page bg), `-info`, `-danger`, `-success`, `-warning`
**Text**: `--color-text-primary` (black), `-secondary` (muted), `-tertiary` (hints), `-info`, `-danger`, `-success`, `-warning`
**Borders**: `--color-border-tertiary` (0.15α, default), `-secondary` (0.3α, hover), `-primary` (0.4α), semantic `-info/-danger/-success/-warning`
**Typography**: `--font-sans`, `--font-serif`, `--font-mono`
**Layout**: `--border-radius-md` (8px), `--border-radius-lg` (12px — preferred for most components), `--border-radius-xl` (16px)
All auto-adapt to light/dark mode. For custom colors in HTML, use CSS variables.

**Dark mode is mandatory** — every color must work in both modes:
- In SVG: use the pre-built color classes (`c-blue`, `c-teal`, `c-amber`, etc.) for colored nodes — they handle light/dark mode automatically. Never write `<style>` blocks for colors.
- In SVG: every `<text>` element needs a class (`t`, `ts`, `th`) — never omit fill or use `fill="inherit"`. Inside a `c-{color}` parent, text classes auto-adjust to the ramp.
- In HTML: always use CSS variables (--color-text-primary, --color-text-secondary) for text. Never hardcode colors like color: #333 — invisible in dark mode.
- Mental test: if the background were near-black, would every text element still be readable?

### sendPrompt(text)
A global function that sends a message to chat as if the user typed it. Use it when the user's next step benefits from Claude thinking. Handle filtering, sorting, toggling, and calculations in JS instead.

### Links
`<a href="https://...">` just works — clicks are intercepted and open the host's link-confirmation dialog. Or call `openLink(url)` directly.

## When nothing fits
Pick the closest use case below and adapt. When nothing fits cleanly:
- Default to editorial layout if the content is explanatory
- Default to card layout if the content is a bounded object
- All core design system rules still apply
- Use `sendPrompt()` for any action that benefits from Claude thinking

## UI components

### Layout width
The widget container is 680px wide. Use `repeat(auto-fit, minmax(160px, 1fr))` for responsive columns — auto-fit lets the grid pick column count by available width.

### Aesthetic
Flat, clean, white surfaces. Minimal 0.5px borders. Generous whitespace. No gradients, no shadows (except functional focus rings). Everything should feel native to claude.ai — like it belongs on the page, not embedded from somewhere else.

### Tokens
- Borders: always `0.5px solid var(--color-border-tertiary)` (or `-secondary` for emphasis)
- Corner radius: `var(--border-radius-md)` for most elements, `var(--border-radius-lg)` for cards
- Cards: white bg (`var(--color-background-primary)`), 0.5px border, radius-lg, padding 1rem 1.25rem
- Form elements (input, select, textarea, button, range slider) are pre-styled — write bare tags. Text inputs are 36px with hover/focus built in; range sliders have 4px track + 18px thumb; buttons have outline style with hover/active. Only add inline styles to override (e.g., different width).
- Buttons: pre-styled with transparent bg, 0.5px border-secondary, hover bg-secondary, active scale(0.98). If it triggers sendPrompt, append a ↗ arrow.
- **Round every displayed number.** JS float math leaks artifacts — `0.1 + 0.2` gives `0.30000000000000004`, `7 * 1.1` gives `7.700000000000001`. Any number that reaches the screen (slider readouts, stat card values, axis labels, data-point labels, tooltips, computed totals) must go through `Math.round()`, `.toFixed(n)`, or `Intl.NumberFormat`. Pick the precision that makes sense for the context — integers for counts, 1–2 decimals for percentages, `toLocaleString()` for currency. For range sliders, also set `step="1"` (or step="0.1" etc.) so the input itself emits round values.
- Spacing: use rem for vertical rhythm (1rem, 1.5rem, 2rem), px for component-internal gaps (8px, 12px, 16px)
- Box-shadows: none, except `box-shadow: 0 0 0 Npx` focus rings on inputs

### Metric cards
For summary numbers (revenue, count, percentage) — surface card with muted 13px label above, 24px/500 number below. `background: var(--color-background-secondary)`, no border, `border-radius: var(--border-radius-md)`, padding 1rem. Use in grids of 2-4 with `gap: 12px`. Distinct from raised cards (which have white bg + border).

### Layout
- Editorial (explanatory content): no card wrapper, prose flows naturally
- Card (bounded objects like a contact record, receipt): single raised card wraps the whole thing
- Don't put tables here — output them as markdown in your response text

**Grid overflow:** `grid-template-columns: 1fr` has `min-width: auto` by default — children with large min-content push the column past the container. Use `minmax(0, 1fr)` to clamp.

**Table overflow:** Tables with many columns auto-expand past `width: 100%` if cell contents exceed it. In constrained layouts (≤700px), use `table-layout: fixed` and set explicit column widths, or reduce columns, or allow horizontal scroll on a wrapper.

### Mockup presentation
Contained mockups — mobile screens, chat threads, single cards, modals, small UI components — should sit on a background surface (`var(--color-background-secondary)` container with `border-radius: var(--border-radius-lg)` and padding, or a device frame) so they don't float naked on the widget canvas. Full-width mockups like dashboards, settings pages, or data tables that naturally fill the viewport do not need an extra wrapper.

### 1. Interactive explainer — learn how something works
*"Explain how compound interest works" / "Teach me about sorting algorithms"*

Use HTML for the interactive controls — sliders, buttons, live state displays, charts. Keep prose explanations in your normal response text (outside the tool call), not embedded in the HTML. No card wrapper. Whitespace is the container.

```html
<div style="display: flex; align-items: center; gap: 12px; margin: 0 0 1.5rem;">
  <label style="font-size: 14px; color: var(--color-text-secondary);">Years</label>
  <input type="range" min="1" max="40" value="20" id="years" style="flex: 1;" />
  <span style="font-size: 14px; font-weight: 500; min-width: 24px;" id="years-out">20</span>
</div>

<div style="display: flex; align-items: baseline; gap: 8px; margin: 0 0 1.5rem;">
  <span style="font-size: 14px; color: var(--color-text-secondary);">£1,000 →</span>
  <span style="font-size: 24px; font-weight: 500;" id="result">£3,870</span>
</div>

<div style="margin: 2rem 0; position: relative; height: 240px;">
  <canvas id="chart"></canvas>
</div>
```

Use `sendPrompt()` to let users ask follow-ups: `sendPrompt('What if I increase the rate to 10%?')`

### 2. Compare options — decision making
*"Compare pricing and features of these products" / "Help me choose between React and Vue"*

Use HTML. Side-by-side card grid for options. Highlight differences with semantic colors. Interactive elements for filtering or weighting.

- Each option in a card. Use badges for key differentiators. A leading Tabler icon (`<i class="ti ti-NAME">` at 20px, `aria-hidden`) anchors each option visually — pick the most apt name per option.
- Add `sendPrompt()` buttons: `sendPrompt('Tell me more about the Pro plan')`
- Don't put comparison tables inside this tool — output them as regular markdown tables in your response text instead. The tool is for the visual card grid only.
- When one option is recommended or "most popular", accent its card with `border: 2px solid var(--color-border-info)` only (2px is deliberate — the only exception to the 0.5px rule, used to accent featured items) — keep the same background and border as the other cards. Add a small badge (e.g. "Most popular") above or inside the card header using `background: var(--color-background-info); color: var(--color-text-info); font-size: 12px; padding: 4px 12px; border-radius: var(--border-radius-md)`.

### 3. Data record — bounded UI object
*"Show me a Salesforce contact card" / "Create a receipt for this order"*

Use HTML. Wrap the entire thing in a single raised card. All content is sans-serif since it's pure UI. Use an avatar/initials circle for people (see example below).

```html
<div style="background: var(--color-background-primary); border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 1rem 1.25rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
    <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--color-background-info); display: flex; align-items: center; justify-content: center; font-weight: 500; font-size: 14px; color: var(--color-text-info);">MR</div>
    <div>
      <p style="font-weight: 500; font-size: 15px; margin: 0;">Maya Rodriguez</p>
      <p style="font-size: 13px; color: var(--color-text-secondary); margin: 0;">VP of Engineering</p>
    </div>
  </div>
  <div style="border-top: 0.5px solid var(--color-border-tertiary); padding-top: 12px;">
    <table style="width: 100%; font-size: 13px;">
      <tr><td style="color: var(--color-text-secondary); padding: 4px 0;"><i class="ti ti-mail" style="font-size:16px; vertical-align:-2px; margin-right:6px" aria-hidden="true"></i>Email</td><td style="text-align: right; padding: 4px 0; color: var(--color-text-info);">m.rodriguez@acme.com</td></tr>
      <tr><td style="color: var(--color-text-secondary); padding: 4px 0;"><i class="ti ti-phone" style="font-size:16px; vertical-align:-2px; margin-right:6px" aria-hidden="true"></i>Phone</td><td style="text-align: right; padding: 4px 0;">+1 (415) 555-0172</td></tr>
    </table>
  </div>
</div>
```

## Color palette

9 color ramps, each with 7 stops from lightest to darkest. 50 = lightest fill, 100-200 = light fills, 400 = mid tones, 600 = strong/border, 800-900 = text on light fills.

| Class | Ramp | 50 (lightest) | 100 | 200 | 400 | 600 | 800 | 900 (darkest) |
|-------|------|------|-----|-----|-----|-----|-----|------|
| `c-purple` | Purple | #EEEDFE | #CECBF6 | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |
| `c-teal` | Teal | #E1F5EE | #9FE1CB | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |
| `c-coral` | Coral | #FAECE7 | #F5C4B3 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |
| `c-pink` | Pink | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |
| `c-gray` | Gray | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |
| `c-blue` | Blue | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |
| `c-green` | Green | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |
| `c-amber` | Amber | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |
| `c-red` | Red | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |

**How to assign colors**: Color should encode meaning, not sequence. Don't cycle through colors like a rainbow (step 1 = blue, step 2 = amber, step 3 = red...). Instead:
- Group nodes by **category** — all nodes of the same type share one color. E.g. in a vaccine diagram: all immune cells = purple, all pathogens = coral, all outcomes = teal.
- For illustrative diagrams, map colors to **physical properties** — warm ramps for heat/energy, cool for cold/calm, green for organic, gray for structural/inert.
- Use **gray for neutral/structural** nodes (start, end, generic steps).
- Use **2-3 colors per diagram**, not 6+. More colors = more visual noise. A diagram with gray + purple + teal is cleaner than one using every ramp.
- **Prefer purple, teal, coral, pink** for general diagram categories. Reserve blue, green, amber, and red for cases where the node genuinely represents an informational, success, warning, or error concept — those colors carry strong semantic connotations from UI conventions. (Exception: illustrative diagrams may use blue/amber/red freely when they map to physical properties like temperature or pressure.)

**Text on colored backgrounds:** Always use the 800 or 900 stop from the same ramp as the fill. Never use black, gray, or --color-text-primary on colored fills. **When a box has both a title and a subtitle, they must be two different stops** — title darker (800 in light mode, 100 in dark), subtitle lighter (600 in light, 200 in dark). Same stop for both reads flat; the weight difference alone isn't enough. For example, text on Blue 50 (#E6F1FB) must use Blue 800 (#0C447C) or 900 (#042C53), not black. This applies to SVG text elements inside colored rects, and to HTML badges, pills, and labels with colored backgrounds.

**Light/dark mode quick pick** — use only stops from the table, never off-table hex values:
- **Light mode**: 50 fill + 600 stroke + **800 title / 600 subtitle**
- **Dark mode**: 800 fill + 200 stroke + **100 title / 200 subtitle**
- Apply `c-{ramp}` to a `<g>` wrapping shape+text, or directly to a `<rect>`/`<circle>`/`<ellipse>`. Never to `<path>` — paths don't get ramp fill. For colored connector strokes use inline `stroke="#..."` (any mid-ramp hex works in both modes). Dark mode is automatic for ramp classes. Available: c-gray, c-blue, c-red, c-amber, c-green, c-teal, c-purple, c-coral, c-pink.

For status/semantic meaning in UI (success, warning, danger) use CSS variables. For categorical coloring in both diagrams and UI, use these ramps.
This is a big build. The core features I'm adding on top of the existing task system:

1. **Deadhang dark-gold theme** applied throughout
2. **Completed tasks archive** — tasks don't vanish when completed, they move to an encrypted archive tab with full detail preserved
3. **Secure document attachment** — paste or upload files directly into task notes, stored as base64 with AES-GCM encryption in localStorage, viewable/downloadable only from within the app{"returncode":0,"stdout":"Building the enhanced version with dark theme + document vault\n","stderr":""}Command argument is 124_105 bytes, exceeding the 100_000-byte per-argument limit. For large content, pipe via stdin or use a file-write API instead of embedding the content inline in the command. Argument preview: 'cat > /mnt/user-data/outputs/deadhang-command-center.html << \'HTMLEOF\'\n<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1.'

---

**[ASSISTANT]**

Looking at what you've got and what you want to add. Let me make sure I understand the full scope before I build:{
  "questions": [
    {
      "question": "Where should completed tasks live?",
      "options": [
        "Collapsed into a separate 'Completed' accordion section at the bottom of the task table",
        "Moved to a dedicated 'Vault' tab alongside the Log/Decisions/Reference sections",
        "Hidden from the main view but accessible via a toggle/filter (current behavior + archive panel)",
        "Stay exactly where they are in the table but visually distinct \u2014 no separate storage"
      ],
      "type": "single_select"
    },
    {
      "question": "For document attachments in notes \u2014 this app runs entirely in the browser. Where should files actually be stored?",
      "options": [
        "In the browser (localStorage/IndexedDB) \u2014 fully offline, no server needed, but limited to ~50MB total",
        "Export the whole app as an HTML snapshot (current Export HTML button) \u2014 files bake into the export",
        "Both: store in browser AND bake into HTML exports so nothing is ever lost on export"
      ],
      "type": "single_select"
    },
    {
      "question": "The Deadhang Secure Dashboard (the Flask app) already has AES-256-GCM encryption. Should this task app tie into that, or stay fully self-contained in the browser?",
      "options": [
        "Stay self-contained in the browser \u2014 no Flask dependency",
        "I want it to eventually connect to the Vault but for now keep it browser-only",
        "Skip the browser version \u2014 just add this document-attachment feature INTO the Flask Vault app instead"
      ],
      "type": "single_select"
    }
  ]
}

---

**[USER]**

either number 3 or we store things in a database if it is secure and we want to scale it to more people using... but i also dont mind it being local to each individual.... and the app being able to populate without my tasks inside of it... and then render based on the person using it and their local system

---

**[ASSISTANT]**

That's a solid architecture decision — multi-user, personalized, scalable. Let me nail down the last few details before I build:{
  "questions": [
    {
      "question": "What's the deployment target for the multi-user version?",
      "options": [
        "Add it to the existing Flask Vault app (same Python/SQLite stack, same server)",
        "Standalone new Flask app \u2014 separate from the Vault",
        "Cloud-hosted (Heroku, Railway, Render, etc.) \u2014 I want it accessible from anywhere",
        "Not sure yet \u2014 build the browser-only version now, architect it so it's easy to migrate later"
      ],
      "type": "single_select"
    },
    {
      "question": "For the document attachment + encryption layer (since this will hold legal docs, tax records, etc.):",
      "options": [
        "Use the exact same AES-256-GCM + master key pattern from the Vault \u2014 proven, already built",
        "Browser-side encryption using the Web Crypto API (no server key needed, fully client-side)",
        "Server-side encryption on the Flask backend (like the Vault) \u2014 files never hit storage unencrypted",
        "Keep it simple for now, add encryption as a later phase"
      ],
      "type": "single_select"
    },
    {
      "question": "For completed tasks with attached documents \u2014 what's the retention behavior?",
      "options": [
        "Completed tasks collapse into a permanent 'Completed Archive' accordion \u2014 always accessible, never deleted",
        "Completed tasks move to a separate 'Evidence Vault' section grouped by category (Legal, Tax, Insurance, etc.)",
        "Completed tasks stay in the main table, just visually distinct \u2014 documents accessible from the same row",
        "Completed tasks hide from default view but appear under a 'Show Completed' toggle with full document access"
      ],
      "type": "single_select"
    }
  ]
}

---

**[USER]**

Q: What's the deployment target for the multi-user version?
A: Cloud-hosted (Heroku, Railway, Render, etc.) — I want it accessible from anywhere

Q: For the document attachment + encryption layer (since this will hold legal docs, tax records, etc.):
A: Browser-side encryption using the Web Crypto API (no server key needed, fully client-side)

Q: For completed tasks with attached documents — what's the retention behavior?
A: Completed tasks move to a separate 'Evidence Vault' section grouped by category (Legal, Tax, Insurance, etc.)

---

**[ASSISTANT]**

Good decisions across the board. Here's what I'm building:

**Architecture plan:**
- Cloud-ready Flask backend (PostgreSQL-ready, deployable to Railway/Render) with user auth, per-user task data, and file storage
- Browser-side AES-256-GCM encryption via Web Crypto API — files encrypted in the browser before upload, server never sees plaintext
- Evidence Vault section in the frontend: completed tasks with documents grouped by category, permanently retained
- Task app ships empty — populates from the logged-in user's data, no pre-seeded tasks
- The big HTML task app you already have gets rebuilt as the frontend

This is a substantial full-stack build. Let me start with the backend first, then the frontend.3.9M	/mnt/skills/public
1.1M	/mnt/skills/public/docx
155K	/mnt/skills/public/docx.skill
1.5K	/mnt/skills/public/docx/LICENSE.txt
20K	/mnt/skills/public/docx/SKILL.md
1.1M	/mnt/skills/public/docx/scripts
16K	/mnt/skills/public/file-reading
6.0K	/mnt/skills/public/file-reading.skill
1.5K	/mnt/skills/public/file-reading/LICENSE.txt
14K	/mnt/skills/public/file-reading/SKILL.md
15K	/mnt/skills/public/frontend-design
6.0K	/mnt/skills/public/frontend-design.skill
10K	/mnt/skills/public/frontend-design/LICENSE.txt
4.5K	/mnt/skills/public/frontend-design/SKILL.md
60K	/mnt/skills/public/pdf
18K	/mnt/skills/public/pdf-reading
8.0K	/mnt/skills/public/pdf-reading.skill
1.5K	/mnt/skills/public/pdf-reading/LICENSE.txt
5.5K	/mnt/skills/public/pdf-reading/REFERENCE.md
11K	/mnt/skills/public/pdf-reading/SKILL.md
22K	/mnt/skills/public/pdf.skill
12K	/mnt/skills/public/pdf/FORMS.md
1.5K	/mnt/skills/public/pdf/LICENSE.txt
17K	/mnt/skills/public/pdf/REFERENCE.md
8.0K	/mnt/skills/public/pdf/SKILL.md
22K	/mnt/skills/public/pdf/scripts
1.2M	/mnt/skills/public/pptx
161K	/mnt/skills/public/pptx.skill
1.5K	/mnt/skills/public/pptx/LICENSE.txt
11K	/mnt/skills/public/pptx/SKILL.md
7.0K	/mnt/skills/public/pptx/editing.md
15K	/mnt/skills/public/pptx/pptxgenjs.md
1.1M	/mnt/skills/public/pptx/scripts
3.0K	/mnt/skills/public/product-self-knowledge
1.5K	/mnt/skills/public/product-self-knowledge.skill
3.0K	/mnt/skills/public/product-self-knowledge/SKILL.md
1.1M	/mnt/skills/public/xlsx
148K	/mnt/skills/public/xlsx.skill
1.5K	/mnt/skills/public/xlsx/LICENSE.txt
12K	/mnt/skills/public/xlsx/SKILL.md
1.1M	/mnt/skills/public/xlsx/scripts
{"returncode":0,"stdout":"","stderr":""}File created successfully: /home/claude/deadhang-ops/backend/app.pyFile created successfully: /home/claude/deadhang-ops/backend/requirements.txtFile created successfully: /home/claude/deadhang-ops/backend/ProcfileFile created successfully: /home/claude/deadhang-ops/backend/railway.tomlFile created successfully: /home/claude/deadhang-ops/backend/.env.exampleNow the frontend — the full app with Web Crypto encryption, Evidence Vault, and the dark Deadhang theme:{"returncode":0,"stdout":"frontend done\n","stderr":"/bin/sh: 1: cannot create /home/claude/deadhang-ops/frontend/index.html: Directory nonexistent\n"}{"returncode":0,"stdout":"frontend written\n","stderr":""}

---

**[ASSISTANT]**

Perfect. Clear picture now. Here's exactly what I'm building:

**Architecture decisions:**
- Cloud-hosted Flask app (Railway/Render-ready) with per-user accounts
- Tasks start **empty** — each user builds their own list (or gets seeded from a template)
- Documents attached to notes via **Web Crypto AES-GCM**, encrypted client-side before hitting the server — server never sees plaintext
- Completed tasks with attachments → **Evidence Vault** grouped by category, permanently retained
- Dark Deadhang gold theme throughout

This is a substantial build — full Flask backend + per-user DB + crypto layer + the full task UI. Let me read the skills first, then build it out properly.     1	---
     2	name: frontend-design
     3	description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
     4	license: Complete terms in LICENSE.txt
     5	---
     6	
     7	This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.
     8	
     9	The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.
    10	
    11	## Design Thinking
    12	
    13	Before coding, understand the context and commit to a BOLD aesthetic direction:
    14	- **Purpose**: What problem does this interface solve? Who uses it?
    15	- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
    16	- **Constraints**: Technical requirements (framework, performance, accessibility).
    17	- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?
    18	
    19	**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.
    20	
    21	Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
    22	- Production-grade and functional
    23	- Visually striking and memorable
    24	- Cohesive with a clear aesthetic point-of-view
    25	- Meticulously refined in every detail
    26	
    27	## Frontend Aesthetics Guidelines
    28	
    29	Focus on:
    30	- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
    31	- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
    32	- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
    33	- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
    34	- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.
    35	
    36	NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.
    37	
    38	Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.
    39	
    40	**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.
    41	
    42	Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
    43	{"returncode":0,"stdout":"audit.html\nbase.html\ndashboard.html\ndeadhang-ops\nlogin.html\nnote_form.html\nnote_view.html\nsettings.html\nsetup.html\nstyle.css\n","stderr":""}{"returncode":0,"stdout":"done\n","stderr":""}File created successfully: /home/claude/deadhang_ops/app.pyFile created successfully: /home/claude/deadhang_ops/templates/base.htmlFile created successfully: /home/claude/deadhang_ops/templates/login.htmlFile created successfully: /home/claude/deadhang_ops/templates/register.htmlFile created successfully: /home/claude/deadhang_ops/templates/settings.htmlNow the big one — the dashboard template with the full task UI, Evidence Vault, and Web Crypto layer:File created successfully: /home/claude/deadhang_ops/templates/dashboard.htmlNow the CSS — full Deadhang dark-gold theme:File created successfully: /home/claude/deadhang_ops/static/ops.cssFile created successfully: /home/claude/deadhang_ops/ProcfileFile created successfully: /home/claude/deadhang_ops/railway.tomlFile created successfully: /home/claude/deadhang_ops/render.yamlFile created successfully: /home/claude/deadhang_ops/start_mac_linux.shFile created successfully: /home/claude/deadhang_ops/start_windows.batFile created successfully: /home/claude/deadhang_ops/README.md{"returncode":0,"stdout":"app.py imports OK\n","stderr":""}{"returncode":0,"stdout":"DB init OK\n  Route /api/tasks: OK\n  Route /api/documents/<int:doc_id>: OK\n  Route /dashboard: OK\n  Route /register: OK\n  Route /login: OK\n","stderr":""}{"returncode":0,"stdout":"Procfile\nREADME.md\n__pycache__\napp.py\ninstance\nrailway.toml\nrender.yaml\nrequirements.txt\nstart_mac_linux.sh\nstart_windows.bat\nstatic\nstorage\ntemplates\n{instance,storage,templates,static}\n---\nbase.html\ndashboard.html\nlogin.html\nregister.html\nsettings.html\n---\nops.css\n","stderr":""}{"returncode":0,"stdout":"copied\n","stderr":""}Full build. Here's exactly what you got and how it all fits together:

---

## What's built

**`app.py`** — Flask backend with full REST API:
- Per-user accounts, scrypt password hashing, 5-attempt lockout
- `/api/tasks` — full CRUD, scoped strictly to the logged-in user
- `/api/tasks/{id}/documents` — encrypted blob upload/retrieval
- `/api/documents/{id}` — retrieve or delete a single encrypted doc
- Audit log on every meaningful action
- Railway/Render-ready with persistent volume mounts for `instance/` and `storage/`

**`dashboard.html`** — The full command center UI:
- Tasks start **empty** for each user — no seed data
- Urgency scoring (0–100) with the same pastel color heat-map from the original
- **Tasks view** with filter chips, search, sort, category grouping
- **Evidence Vault** tab — completed tasks grouped by category, permanently archived, never deletable through normal UI
- Task detail modal with full edit fields + document section

**The encryption flow:**
1. You click "Unlock Encryption" in the task modal, enter your password
2. Browser runs PBKDF2-SHA256 (250k iterations) → AES-256-GCM key in memory only
3. You drop your Articles of Organization PDF onto the upload area
4. Browser encrypts it → 12-byte IV prepended to ciphertext → base64 → POST to server
5. Server stores the blob on disk as a `.enc` file — it's opaque noise without your key
6. Mark task Complete → it moves to Evidence Vault, docs stay attached and encrypted
7. In the Vault, click "Decrypt & Download" → browser fetches the blob, decrypts locally, streams the file to your downloads folder

**To deploy to Railway:** push to GitHub, connect repo, add the two persistent volumes (`/app/instance` and `/app/storage`), set `APP_SECRET_KEY` and `FORCE_HTTPS=1`.

**The one critical gotcha** (documented in README and Settings): your encryption key is derived from your password. Change your password = old docs become unreadable. Download them first, then change.