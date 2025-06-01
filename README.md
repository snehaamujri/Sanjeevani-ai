
# Sanjeevani.AI 💊🤖

**AI-powered medicine verification & distribution system using Django**

Sanjeevani.AI is a healthtech backend built for the AI Agents Hackathon 2025. It allows health workers to scan medicine batch IDs, verify their authenticity (simulated with blockchain data), and notify patients via SMS/WhatsApp.

## 🔧 Features

- ✅ Batch verification using simulated NFT (blockchain.json)
- 📦 Django-based backend
- 📲 Twilio SMS integration for patient notification
- 🔐 Secure, scalable design for real-world rural healthcare

## 📂 Project Structure
-sanjeevani-ai/
├── blockchain.json # Simulated NFT data
├── sanjeevani_core/ # Django project core
├── verification/ # App handling verification and reporting
├── sms_utils.py # Twilio messaging logic
├── manage.py


## 🚀 Endpoints

- `GET /verify/<batch_id>/` → Check if medicine batch is authentic
- `POST /send-report/` → Send SMS to patient after verification

## 🛠 Built With

- Python 3
- Django
- Twilio API (for SMS)
- JSON (mock blockchain)

---

### 👩‍💻 Contributors
- Sneha Amujuri [@snehaamujri](https://github.com/snehaamujri)
- Team Sanjeevani.AI 🚑💚

---



