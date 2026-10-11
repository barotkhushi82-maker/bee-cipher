# bee-cipher
Ambient privacy shield for Bee wearable transcripts
# 🐝 Bee Cipher — Wearable Privacy & Security Shield

> **Live Web Demo:** [bee-cipher.streamlit.app](https://bee-cipher-lv6k9z4ac9wqdnkvqr2g65.streamlit.app)

Bee Cipher is an ambient privacy filter and threat analysis layer built specifically for **Bee Wearable AI** transcript logs. It automatically redacts sensitive Personal Identifiable Information (PII) like passcodes and credit card numbers, while flagging phone scams and vishing patterns in real time.

---

## 🛠️ Key Features
- **PII Redaction Engine (`cipher_engine.py`)**: Sanitizes passcodes, phone numbers, credit card numbers, and emails from continuous transcripts.
- **Vishing & Social Engineering Detection**: Identifies threat triggers, wire transfer demands, and high-pressure scam language.
- **Bee Wearable Log Ingestion (`bee_ingest.py`)**: Reads structured markdown summary exports (`daily/YYYY-MM-DD/summary.md`) and JSON stream payloads.
- **Interactive Web Dashboard (`app.py`)**: Built with Streamlit to visualize transcript sanitization, security threat levels, and privacy audit logs.

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/barotkhushi82-maker/bee-cipher.git](https://github.com/barotkhushi82-maker/bee-cipher.git)
   cd bee-cipher
