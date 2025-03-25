import requests
import smtplib
import time
import datetime

MY_EMAIL = "Your Email ID"
MY_PASSWORD = "Your-Password"
# MY_LAT = 27.174424
# MY_LNG = 75.953797
MY_LAT = 12.174424
MY_LNG = 135.953797


def send_mail():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Hello\n\nLook Up.")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()["iss_position"]

iss_latitude = float(data["latitude"])
iss_longitude = float(data["longitude"])


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    resp = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    resp.raise_for_status()
    new_data = resp.json()["results"]
    sunrise_hour = int(new_data["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(new_data["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour
    if sunset_hour <= time_now >= sunrise_hour:
        return True


while True:
    time.sleep(60)
    if MY_LNG-5 <= iss_longitude <= MY_LNG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        if is_dark():
            send_mail()
