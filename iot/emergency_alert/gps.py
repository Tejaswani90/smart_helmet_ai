# Smart Helmet GPS Simulator

def get_gps_location():

    # Simulated GPS coordinates
    latitude = 17.6868
    longitude = 83.2185

    print("\n================================")
    print("         GPS LOCATION")
    print("================================")

    print(f"Latitude : {latitude}")
    print(f"Longitude: {longitude}")

    google_maps_link = (
        f"https://www.google.com/maps?q={latitude},{longitude}"
    )

    print(f"\nGoogle Maps Location:")
    print(google_maps_link)

    return latitude, longitude, google_maps_link


if __name__ == "__main__":
    get_gps_location()