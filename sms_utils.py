import smtplib
from email.mime.text import MIMEText

# Replace this with your Fast2SMS API key
FAST2SMS_API_KEY = "Vq0XFPtTauicZNMQYGU8efoKldI72BvRHsAry1Ez6mwCxnhjOSOVmBPbQfrACzDpwLJ7vZNjMWKYFT6q"

def send_sms(to, message):
    print(f"[MOCK SMS] To: {to} | Message: {message}")
    return {"status": "success", "message": "SMS sent (simulated for demo)"}

# Example usage
result = send_sms(
    "6303387736",
    "Hello Sneha, your medicine (Batch CIPLA-XYZ123) has been verified successfully. Stay healthy! - Sanjeevani.AI"
)
print(result)
