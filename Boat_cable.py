import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.flipkart.com/boat-a320-1-5-m-usb-type-c-cable/p/itma010289de41cb?pid=ACCFUGAC4WYMSHYE&lid=LSTACCFUGAC4WYMSHYEOXI6YN&marketplace=FLIPKART'

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(attrs="B_NuCI").get_text()
    price = soup.find(attrs="_30jeq3 _16Jk6d").get_text()
    converted_price = float(price[1:4])
    print(title.strip())
    print(converted_price)

    if converted_price < 100:
        send_mail()

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('senders_mail','2_factor_verification_code_for_apps')

    subject= "It is Christams time, Price is is less than 650"
    body= "check the link https://www.flipkart.com/ambrane-cbc-15-2-4a-1-5m-sync-fast-charge-tough-nylon-braided-usb-1-5-m-type-c-cable/p/itmf8p2zztznngac?pid=ACCF8P2ZGNPAJ425&lid=LSTACCF8P2ZGNPAJ4251726UR&marketplace=FLIPKART "
    msg =f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'senders_mail',
        'recievers_mail',
        msg
    )

    print('Email Has been Sent!')
    server.quit()
while True:
    check_price()
    time.sleep(60*30)
