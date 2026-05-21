import requests


def get_weather(city):

    # URL for wttr.in weather service
    url = f"https://wttr.in/{city}?format=j1"

    try:
        # Send request
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Extract weather information
        current = data["current_condition"][0]

        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        weather_desc = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        # Display weather
        print("\n🌤️ WEATHER DASHBOARD")
        print("=" * 40)

        print(f"\n📍 City: {city.title()}")

        print("\nCurrent Weather:")
        print("─" * 40)

        print(f"Temperature:   {temperature}°C")
        print(f"Feels Like:    {feels_like}°C")
        print(f"Condition:     {weather_desc}")
        print(f"Humidity:      {humidity}%")
        print(f"Wind Speed:    {wind_speed} km/h")

        print("\n✅ Weather data loaded successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

while True:

    city = input("\nEnter city name (or type quit): ")

    if city.lower() == "quit":
        print("\n👋 Exiting program...")
        break

    get_weather(city)