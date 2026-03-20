def generate_reply(email):
    return f"""Hi,

Thank you for your message.

I understand your requirement:
"{email}"

I’d be happy to help you with this. Let’s connect and discuss the details so I can provide the best solution.

Best regards,  
Pratik
"""

def main():
    print("=== AI Email Reply Generator ===\n")
    email = input("Enter client message:\n")
    
    reply = generate_reply(email)
    
    print("\n--- Generated Reply ---\n")
    print(reply)

if __name__ == "__main__":
    main()
