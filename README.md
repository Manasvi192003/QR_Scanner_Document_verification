📄 Document Verification System using QR Scanner
🚀 Overview

This project is a Document Verification System built using Flask, MySQL, OpenCV, and QR code technology. It provides a secure and efficient way to verify official documents by embedding QR codes that store encrypted document identifiers. A QR scanner can then be used to validate authenticity, ensuring tamper-proof and quick verification.

The solution aims to replace manual document checks with an automated and technology-driven approach, reducing errors, fraud, and processing time.

🎯 Features

🔐 Secure Document Upload (admin-only upload system)

📦 QR Code Generation for each uploaded document

📷 QR Scanner Integration using OpenCV for real-time document verification

💾 Database Integration with MySQL to store document metadata and verification history

⚡ Fast & Hassle-Free Verification process

🛡️ Tamper-proof system – QR ensures document integrity

🛠️ Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript (Bootstrap for UI)

Database: MySQL

QR Code Generation: Python qrcode library

QR Code Scanning: OpenCV + pyzbar

Other Tools: Werkzeug (for secure file handling)

⚙️ How It Works

Admin uploads a document via the portal.

A unique ID is generated and stored in the database.

A QR code containing this ID is generated and attached to the document.

During verification, a QR scanner reads the code.

The system cross-checks the ID with the database.

✅ If it matches → The document is verified as authentic.
❌ Otherwise → It is flagged as invalid or tampered.

📂 Project Structure
document-verification-qr/
│── app.py                # Flask backend
│── static/               # CSS, JS, images
│── templates/            # HTML templates
│── uploads/              # Uploaded documents
│── qrcodes/              # Generated QR codes
│── database.sql          # MySQL schema
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

🚀 Installation & Setup

Clone the Repository

git clone https://github.com/your-username/document-verification-qr.git
cd document-verification-qr


Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt


Setup MySQL Database

Import database.sql into MySQL

Update your app.py with DB credentials

Run Flask Server

python app.py


Server runs on: http://127.0.0.1:5000/

📸 Screenshots (Optional if you add later)

Document Upload Page

QR Code Generated Example

Verification Success/Failure Page

🌟 Aspirational Goal

As a CSE student passionate about emerging technologies, I built this project to explore secure identity verification systems that solve real-world problems. By blending machine learning, databases, and computer vision, I aim to design systems that make daily processes smarter, faster, and more secure, reducing human effort and ensuring trust in digital workflows.

📌 Future Enhancements

🔄 Blockchain integration for immutable verification

📱 Mobile app version for on-the-go scanning

🔔 Email/SMS alerts on document verification

🌐 Deployment on cloud platforms (AWS/GCP/Azure)
