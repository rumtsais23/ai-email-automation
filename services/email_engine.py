class EmailEngine:

    def analyze(self, text: str, email_type: str = "reply", tone: str = "professional"):

        text_lower = text.lower()

        # 1. CLASSIFICATION
        if any(word in text_lower for word in ["error", "issue", "problem", "help"]):
            category = "support"
        elif any(word in text_lower for word in ["price", "plan", "buy", "purchase"]):
            category = "sales"
        elif any(word in text_lower for word in ["win", "free", "prize", "click here"]):
            category = "spam"
        else:
            category = "general"

        # 2. RESPONSE
        if email_type == "reply":

            if category == "support":
                response = "Hi, support reply..."
            elif category == "sales":
                response = "Hi, sales reply..."
            elif category == "spam":
                response = "Spam detected"
            else:
                response = "General reply"

        else:
            response = text

        # 3. SUMMARY (CALL FUNCTION HERE)
        summary_result = self.summarize(text)

        # 4. Priority
        priority = self.get_priority(text, category)
        
        # 5. OUTPUT
        return {
            "category": category,
            "priority": priority,
            "summary": summary_result["summary"],
            "response": response,
            "confidence": 80 if category != "general" else 60
        } 


    def summarize(self, text: str):

        text_lower = text.lower()
        summary_parts = []

        if any(w in text_lower for w in ["error", "issue", "problem", "bug"]):
            summary_parts.append("user reports technical issue")

        if any(w in text_lower for w in ["login", "password", "access"]):
            summary_parts.append("authentication related problem")

        if any(w in text_lower for w in ["refund", "money", "payment"]):
            summary_parts.append("payment or refund request")

        if any(w in text_lower for w in ["urgent", "asap", "immediately"]):
            summary_parts.append("high urgency request")

        if not summary_parts:
            summary = "general inquiry with no specific issue detected"
        else:
            summary = ", ".join(summary_parts)

        return {"summary": summary}
    def get_priority(self, text: str, category: str):

        text_lower = text.lower()
        score = 0

        # urgency signals
        if any(w in text_lower for w in ["urgent", "asap", "immediately"]):
            score += 40

        # financial issues = high priority
        if any(w in text_lower for w in ["refund", "money", "payment"]):
            score += 35

        # login issues = medium-high
        if any(w in text_lower for w in ["login", "password", "access"]):
            score += 25

        # category boost
        if category == "support":
            score += 10

        # final classification
        if score >= 60:
            return "HIGH"
        elif score >= 30:
            return "MEDIUM"
        else:
            return "LOW"