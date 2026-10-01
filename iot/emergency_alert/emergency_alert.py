import time
import threading


def normal_mode():
    print("\n================================")
    print("       SMART HELMET AI")
    print("================================")
    print("Prediction: NORMAL")
    print("Green LED: ON")
    print("Red LED: OFF")
    print("Buzzer: OFF")
    print("Status: Rider is safe")


def accident_mode():
    print("\n================================")
    print("       SMART HELMET AI")
    print("================================")
    print("Prediction: ACCIDENT")
    print("\nWARNING! ACCIDENT DETECTED!")
    print("Red LED: ON")
    print("Green LED: OFF")
    print("Buzzer: ON")

    print("\nRIDER SAFETY CHECK")
    print("-------------------------")
    print("You have 15 seconds.")
    print("Type YES and press Enter if you are safe.")

    response = {"value": None}

    def get_response():
        answer = input("\nRider response: ").strip().upper()
        response["value"] = answer

    thread = threading.Thread(target=get_response, daemon=True)
    thread.start()

    for remaining in range(15, 0, -1):

        if response["value"] == "YES":
            print("\nSafety confirmation received!")
            cancel_alert()
            return

        print(f"Time remaining: {remaining} seconds")
        time.sleep(1)

    if response["value"] == "YES":
        cancel_alert()
    else:
        print("\nNo safety confirmation received.")
        send_emergency_alert()


def cancel_alert():
    print("\n================================")
    print("       ALERT CANCELLED")
    print("================================")
    print("Rider confirmed: I'M SAFE")
    print("Red LED: OFF")
    print("Green LED: ON")
    print("Buzzer: OFF")
    print("No emergency alert was sent.")
    print("================================")


def send_emergency_alert():
    print("\n================================")
    print("       EMERGENCY ALERT")
    print("================================")
    print("Red LED: ON")
    print("Buzzer: ON")
    print("Emergency alert triggered!")
    print("GPS location will be obtained.")
    print("Emergency message will be sent.")
    print("================================")


def main():
    print("\n================================")
    print("       SMART HELMET AI")
    print("================================")
    print("1. Normal condition")
    print("2. Accident condition")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        normal_mode()

    elif choice == "2":
        accident_mode()

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()