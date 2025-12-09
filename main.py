import schedule 
import time
import requests
from twilio.rest import Client


def get_weather(latitude,longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response=requests.get(base_url)
    data=response.json()
    return data

def send_message(body):
    account_sid="account_sid" //via TWILIO
    auth_token="auth_token" //via TWILIO
    from_phone_number="phone_number"  //le twilio va veux generer un from_numero
    to_phone_number="to_phone_numbe" //ajouter votre numero de telephone

    client=Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("text message sent")

def send_weather_update():
    latitude=36.48
    longitude=10.6
    weather_data=get_weather(latitude,longitude)
    temperature_celsius=weather_data["hourly"]["temperature_2m"][0]
    relative_humidity=weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed=weather_data["hourly"]["windspeed_10m"][0]

    weather_info=(
        f"Good Morning!\n"
        f"Current Weather in M:\n"
        f"Temperature: {temperature_celsius:.2f}°C\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind Speed: {wind_speed} km/h"
    )

    send_message(weather_info)

def main():
    schedule.every().day.at("19:28").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
        


if __name__=="__main__":
    main()
send_message("TEST")
