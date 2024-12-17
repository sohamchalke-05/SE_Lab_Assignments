"""Required moduled installed"""
import smtplib
import random
from validate_email_address import validate_email

def generate_otp(length=6):
    """Generate a random OTP of specified length (default is 6)."""
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8.")
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email(email, otp):
    """Send OTP to the specified email address."""
    
    
    if not validate_email(email):
        raise ValueError("Invalid email address.")

    message = f"Your One-Time Password (OTP) is: {otp}"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('youremail@example.com', 'yourpassword')  
            smtp.sendmail("your eamil",email,message)
            print(f"OTP sent to {email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    """Main function to generate and send OTP."""
    email = input("Enter the recipient's email address: ")
    try:
        otp = generate_otp(length=6) 
        send_email(email, otp)
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
