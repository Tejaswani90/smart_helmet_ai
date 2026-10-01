# ==============================================
# SMART HELMET AI - EMERGENCY MESSAGE
# ==============================================

def send_emergency_message(latitude, longitude):

    print("\n================================")
    print("      EMERGENCY MESSAGE")
    print("================================")

    message = f"""
ACCIDENT ALERT!

A possible accident has been detected.

GPS Location:
Latitude: {latitude}
Longitude: {longitude}

Google Maps:
https://www.google.com/maps?q={latitude},{longitude}

Please contact the rider immediately.
"""

    print(message)

    print("Emergency message prepared successfully.")
    print("================================")


if __name__ == "__main__":

    latitude = 17.6868
    longitude = 83.2185

    send_emergency_message(latitude, longitude)