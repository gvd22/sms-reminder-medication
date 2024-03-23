from twilio.rest import Client
from datetime import datetime
import time

# Connection to twilio
account_sid = ''
auth_token = ''

zwei = "02:00:00"
acht = "08:00:00"
vierzehn = "14:00:00"
zwanzig = "20:00:00"

def schedule():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if current_time == zwei:
        message = "Es ist " + zwei + " Uhr, wenn du Schmerzen hast kannst du jetzt medikament 1000mg nehmen"
        messagecreation(message)
    elif current_time == acht:
        message = "Es ist " + acht + " Uhr, du musst jetzt medikament 1000mg, medikament 600mg, 2x Tabletten medikament, medikament 40mg nehmen" \
                                    "und medikament 1g "
        messagecreation(message)
    elif current_time == vierzehn:
        message = "Es ist " + vierzehn + " Uhr, du musst jetzt medikament 1000mg und medikament 600mg nehmen"
        messagecreation(message)
    elif current_time == zwanzig:
        message = "Es ist " + zwanzig + " Uhr, du musst medikament 1000mg, medikament 600mg, 2x Tabletten medikament und medikament 1g nehmen"
        messagecreation(message)
    time.sleep(1)


def messagecreation(message):
    sendmessage(message)

def sendmessage(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='messagesid',
        body=message,
        to='phonenumber'
    )

    print(message.sid)

while True:
    schedule()
