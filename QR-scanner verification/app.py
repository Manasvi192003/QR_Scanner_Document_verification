from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import qrcode
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
from flask import session, flash
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for login sessions

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['QR_FOLDER'] = 'static/qrcodes'

# Ensure upload folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QR_FOLDER'], exist_ok=True)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Change if your MySQL password is set
        database="qr_verification"
    )


@app.route("/")
def home():
    return render_template("home.html")
# Admin upload route
@app.route('/admin/upload', methods=['GET', 'POST'])
def admin_upload():
    if not session.get("admin_logged_in"):
        flash("Login required.")
        return redirect(url_for("admin_login"))
    if request.method == 'POST':
        name = request.form['student_name']
        student_id = request.form['student_id']
        doc_type = request.form['doc_type']
        file = request.files['document']

        if file:
            filename = f"{student_id}_{file.filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Generate unique document ID (we'll get this from DB after insert)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO documents (student_name, student_id, doc_type, image_path) VALUES (%s, %s, %s, %s)",
                           (name, student_id, doc_type, file_path))
            conn.commit()
            doc_id = cursor.lastrowid

            # Generate QR Code with doc ID
            qr_data = f"DOCID:{doc_id}"
            qr_img = qrcode.make(qr_data)
            qr_filename = f"qr_{doc_id}.png"
            qr_path = os.path.join(app.config['QR_FOLDER'], qr_filename)
            qr_img.save(qr_path)

            # Save QR path to database
            cursor.execute("UPDATE documents SET qr_path = %s WHERE id = %s", (qr_path, doc_id))
            conn.commit()
            cursor.close()
            conn.close()

            flash("Document uploaded and QR generated successfully!", "success")
            return redirect(url_for("home"))

    return render_template("admin_upload.html")

# Home page – user uploads QR
@app.route('/verify', methods=['GET', 'POST'])
def verify_document():
    if request.method == 'POST':
        qr_file = request.files['qr_image']
        if qr_file:
            # Save temporary
            filename = f"temp_{datetime.now().timestamp()}.png"
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            qr_file.save(path)

            # Read QR using OpenCV
            img = cv2.imread(path)
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecode(img)

            if data.startswith("DOCID:"):
                doc_id = data.split(":")[1]

                # Check DB
                conn = get_db_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM documents WHERE id = %s", (doc_id,))
                doc = cursor.fetchone()
                conn.close()

                if doc:
                    return render_template("result.html", result="✅ Document is Verified", doc=doc)
                else:
                    return render_template("result.html", result="❌ Document Not Found / Fake")

            return "QR code invalid or not readable"

    return render_template("verify.html")

# Check if admin already exists
def admin_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin")
    exists = cursor.fetchone()
    conn.close()
    return exists is not None

# Get admin details
def get_admin(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM admin WHERE username=%s", (username,))
    admin = cursor.fetchone()
    conn.close()
    return admin

@app.route("/admin/signup", methods=["GET", "POST"])
def admin_signup():
    if admin_exists():
        flash("Admin already exists. Please log in.", category="signup")
        return redirect(url_for("admin_login"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_pw = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()
        conn.close()

        flash("Admin registered. Please log in.", category="signup")
        return redirect(url_for("admin_login"))

    return render_template("admin_signup.html")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = get_admin(username)
        if admin and check_password_hash(admin[1], password):
            session["admin_logged_in"] = True
            return redirect(url_for("admin_upload"))
        else:
            flash("Invalid credentials", category="login")
            return redirect(url_for("admin_login"))

    return render_template("admin_login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Logged out successfully.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

