---
{
  "chunk_id": "Claude-Batch-2026-07-05__Claude-Admin_dashboard_redesign.md__chunk-0002",
  "archive_id": "Claude-Batch-2026-07-05",
  "archive_filename": "Claude-Batch-2026-07-05.zip",
  "source_path": "Claude-Admin_dashboard_redesign.md",
  "chunk_index": 2,
  "chunk_count_for_source": 7,
  "char_start": 11392,
  "char_end": 23388,
  "source_sha256": "8e46af326a7ee59ea0e5723b08fe807dff0c880c1e15da18fcb3bcded8dceec1",
  "test_or_generated_note": "Generated from archived memory source. Original archive remains unchanged."
}
---

user_id, action, target_type, target_id, details, ip_address, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
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
