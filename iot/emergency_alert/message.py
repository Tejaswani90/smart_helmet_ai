def create_emergency_message(latitude, longitude):

    google_maps_link = (
        f"https://www.google.com/maps?q={latitude},{longitude}"
    )

    message = f"""
SMART HELMET EMERGENCY ALERT

Accident detected!

The rider did not confirm that they are safe.

Rider Status: EMERGENCY

GPS Location:
Latitude: {latitude}
Longitude: {longitude}

Location:
{google_maps_link}

Please contact the rider immediately.
"""

    return message


if __name__ == "__main__":

    latitude = 17.6868
    longitude = 83.2185

    message = create_emergency_message(
        latitude,
        longitude
    )

    print("================================")
    print("       EMERGENCY MESSAGE")
    print("================================")

    print(message)