# ==================================================
# SMART HELMET - GPS MODULE
# ==================================================

DEFAULT_LATITUDE = 17.6868
DEFAULT_LONGITUDE = 83.2185


def get_gps_location():
    """
    Returns GPS coordinates and Google Maps link.
    Currently uses simulated GPS coordinates.
    """

    latitude = DEFAULT_LATITUDE
    longitude = DEFAULT_LONGITUDE

    google_maps_link = (
        f"https://www.google.com/maps?"
        f"q={latitude},{longitude}"
    )

    return latitude, longitude, google_maps_link


if __name__ == "__main__":

    latitude, longitude, maps_link = get_gps_location()

    print("\n================================")
    print("         GPS LOCATION")
    print("================================")

    print(f"Latitude : {latitude}")
    print(f"Longitude: {longitude}")

    print("\nGoogle Maps Location:")
    print(maps_link)