import re

class BeeCipherEngine:
    def __init__(self):
        # Patterns for Redacting Sensitive PII
        self.pii_patterns = {
            "credit_card": r'\b(?:\d[ -]*?){13,16}\b',
            "password": r'(?i)\b(?:password|passcode|pin)\s*[:=]?\s*([a-zA-Z0-9!@#$%^&*]+)',
            "phone_number": r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }
        
        # High-Risk Vishing / Scam Indicators
        self.scam_keywords = [
            "urgent bank transfer", "verify your account immediately",
            "gift card payment", "irs tax audit", "wire funds now",
            "suspicious activity on account", "do not hang up"
        ]

    def redact_pii(self, transcript_text: str) -> str:
        """Redacts sensitive PII from Bee wearable conversation streams."""
        sanitized_text = transcript_text
        for pii_type, pattern in self.pii_patterns.items():
            sanitized_text = re.sub(pattern, f"[REDACTED_{pii_type.upper()}]", sanitized_text)
        return sanitized_text

    def detect_scam(self, transcript_text: str) -> dict:
        """Scans transcript for social engineering pressure tactics."""
        lower_text = transcript_text.lower()
        detected_threats = [phrase for phrase in self.scam_keywords if phrase in lower_text]
        
        is_high_risk = len(detected_threats) > 0
        risk_score = min(100, len(detected_threats) * 35)
        
        return {
            "is_high_risk": is_high_risk,
            "risk_score": risk_score,
            "detected_threats": detected_threats
        }

# Example execution test
if __name__ == "__main__":
    raw_sample = "Hey, my password is Secret123 and please wire funds now for my bank transfer."
    engine = BeeCipherEngine()
    
    redacted = engine.redact_pii(raw_sample)
    scam_analysis = engine.detect_scam(raw_sample)
    
    print("--- RAW TRANSCRIPT ---")
    print(raw_sample)
    print("\n--- SANITIZED TRANSCRIPT ---")
    print(redacted)
    print("\n--- THREAT ASSESSMENT ---")
    print(scam_analysis)
