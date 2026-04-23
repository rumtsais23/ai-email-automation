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
