
# 📄 Document Verification System using QR Scanner

Welcome to the **Document Verification System** — a secure and efficient solution for verifying documents using QR code technology. Each document is embedded with a unique QR code linked to its metadata in the database. By scanning the QR, authenticity can be instantly validated, ensuring a **tamper-proof and hassle-free verification process**.

---

## 🔍 Overview

Manual verification of documents is often time-consuming and prone to fraud. This project introduces an automated **QR-based document verification system**, combining **Flask, MySQL, OpenCV, and QR libraries** to deliver a reliable solution. It provides a seamless workflow for **document upload, QR generation, and verification** through scanning.

---

## 💡 Key Features

📤 **Admin-only document upload system**
🔐 **Unique QR code generation** for each uploaded document
📷 **Real-time QR scanning** using OpenCV & Pyzbar
💾 **Database-backed storage** (MySQL) for document records and verification logs
⚡ **Instant verification results** (Authentic ❌ Invalid)
🛡️ **Prevents tampering & fraud** with secure QR linking

---

## 🧠 Verification Logic

The system validates documents using the following workflow:

| Step | Action                           | Result                     |
| ---- | -------------------------------- | -------------------------- |
| 1️⃣  | Admin uploads document           | Unique ID generated        |
| 2️⃣  | System stores metadata in DB     | QR code created with ID    |
| 3️⃣  | QR attached to document          | Saved in system            |
| 4️⃣  | Scanner reads QR at verification | Extracted ID checked in DB |
| 5️⃣  | Match found ✅                    | Document marked authentic  |
| 6️⃣  | No match ❌                       | Document flagged invalid   |

---

## 🚀 Tech Stack

**Frontend:** HTML, CSS, Bootstrap
**Backend:** Python (Flask)
**Database:** MySQL
**QR Generation:** Python `qrcode`
**QR Scanning:** OpenCV, Pyzbar
**Other Tools:** Werkzeug (secure file handling)

---

## 📂 Project Structure

Document-Verification-QR/
│── app.py            # Main Flask app
│── templates/        # HTML templates (upload, verify, result)
│── static/           # CSS, JS, styling
│── uploads/          # Uploaded documents
│── qrcodes/          # Generated QR codes
│── database.sql      # MySQL schema
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
```


## 🌟 Aspirational Goal

As a **CSE student passionate about new and emerging technologies**, I built this project to explore how **computer vision and database systems** can enhance **document security**. My goal is to create innovative solutions that **reduce manual effort, eliminate fraud, and make verification faster, smarter, and more trustworthy** in real-world scenarios.

---

## 📌 Future Enhancements

🔄 Blockchain-based immutable verification
📱 Mobile app for QR scanning on-the-go
🔔 SMS/Email alerts on verification results
🌐 Deployment on AWS/GCP for scalability

---

⭐ If you like this project, don’t forget to **star the repo** and share feedback!

---

👉 Do you also want me to draft this in a **project report style (Abstract → Objective → Methodology → Code Snapshots → Conclusion)** like we did for your To-Do List project? That would make it perfect for academic submission.

