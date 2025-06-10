# Sanjeevani.AI – AI Agents for Autonomous Medicine Verification & Supply Distribution

Sanjeevani.AI is an intelligent health supply chain dashboard for health workers and administrators. It enables secure, transparent, and efficient medicine verification and distribution using AI and digital tools.

---

## 🚀 Features

- **Medicine Inventory Management:** Track and manage medicine stock, batches, and expiry.
- **Task Management:** Assign and update health worker tasks (Mark Done/Undo).
- **AI-based Verification (Mocked):** Simulate AI verification of medicine authenticity.
- **QR/Barcode Scanning (Mocked):** Display scanned batch details for traceability.
- **Supply Chain Tracking (Mocked):** Show current location/status of medicine batches.
- **Storage Condition Monitoring (Mocked):** Display temperature and humidity data.
- **Chain-of-Custody Logging (Mocked):** Show batch movement history.
- **Route Optimization (Mocked):** Display optimized delivery routes.
- **Alerts & Notifications:** Highlight expiring medicines and important events.
- **Incident Reporting:** Allow health workers to report issues.
- **CSV Export:** Download inventory data for offline use.
- **Buy & SMS (Mocked):** Simulate medicine purchase and send mock SMS to users.
- **Profile Management:** Health worker profile and secure logout.

---

## 🛠️ Tech Stack

- Django, Python, Bootstrap, Chart.js
- Mocked AI, IoT, and blockchain features for demo purposes

---

## ⚡ Quick Start

### 1. Clone the repository

```sh
git clone https://github.com/snehaamujri/Sanjeevani-ai.git
cd Sanjeevani-ai
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply migrations

```sh
python manage.py migrate
```

### 5. Run the development server

```sh
python manage.py runserver 0.0.0.0:8000
```

### 6. Access the app

Open your browser and go to [http://localhost:8000/](http://localhost:8000/)

---

## 📦 Project Structure

- `dashboard/` – Django app with templates and views
- `requirements.txt` – Python dependencies
- `manage.py` – Django management script

---

## 📝 Notes

- Most advanced features (AI, QR, supply chain, etc.) are **mocked** for demo/hackathon purposes.
- For deployment, ensure you have a valid `requirements.txt` and follow platform-specific instructions.

---

## 📄 License

This project is for demo and educational purposes.
