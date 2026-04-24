This system is not just a simulation — it has been successfully integrated with a real Gmail inbox.

🔗 How it works in practice:
Connects to Gmail via IMAP
Fetches real incoming emails
Analyzes content using AI logic (classification, priority, summarization)
Generates automated responses
Sends replies back via SMTP

✅ Verified real-world flow:
Tested with real emails (including external senders)
Successfully processed and categorized messages
Generated and returned automated responses

⚙️ Tech stack used for integration:
IMAP (email retrieval)
SMTP (email sending)
Python backend (Flask API)
Custom AI Email Engine

This demonstrates a complete end-to-end automation pipeline, not just a standalone model.

# 🚀 AI Email Automation System

A lightweight AI-powered email automation system that classifies, summarizes, prioritizes, and responds to incoming emails.

This project is designed as a practical backend + AI logic exercise, simulating real-world customer support workflows.

---

## 🧠 Features

### ✅ Email Classification
Automatically detects the intent of the email:
- Support
- Sales
- Spam
- General

---

### 📝 Email Summarization
Extracts key meaning from messages:
- Technical issues
- Authentication problems
- Payment/refund requests
- Urgency signals

---

### ⚡ Priority Scoring
Assigns priority based on content:
- **HIGH** → urgent / financial / login issues  
- **MEDIUM** → standard support  
- **LOW** → general inquiries  

---

### 🤖 Auto Response Generation
Generates replies based on:
- Email category
- Selected tone (professional / friendly)

---

## 🏗️ Architecture

- Flask API
- Modular service layer (`EmailEngine`)
- Rule-based AI logic (no external paid APIs)
- Clean separation of concerns

---

## 📡 API Endpoint

### POST `/email-assist`

#### Request:
```json
{
  "email": "I cannot login and need urgent help",
  "tone": "friendly"
}
