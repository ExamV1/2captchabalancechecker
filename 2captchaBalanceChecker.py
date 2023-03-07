import requests
import os
import time

def get_balance(api_key):
    url = f"https://2captcha.com/res.php?key={api_key}&action=getbalance"
    response = requests.get(url)
    if response.status_code == 200:
        if response.text.startswith("ERROR"):
            return None
        else:
            return float(response.text)
    else:
        return None

while True:
    api_key = input("Enter your 2captcha API key: ")
    balance = get_balance(api_key)
    if balance is not None:
        break
    else:
        print("Incorrect API key. Please try again.")

print(f"Press Enter to refresh your balance.\n You cureently have ${balance:.2f}")

while True:
    command = input()
    if command.lower() == "quit":
        break
    elif command == "":
        print("Refreshing balance", end="", flush=True)
        for _ in range(6):
            time.sleep(0.1)
            print(".", end="", flush=True)
        print()
        os.system("cls" if os.name == "nt" else "clear")
        balance = get_balance(api_key)
        if balance is not None:
            print(f"Your balance is: ${balance:.2f}")
        else:
            print("Failed to get balance. Please check your API key and try again.")
        print("Press Enter to refresh the balance")