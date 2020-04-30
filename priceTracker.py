from bs4 import BeautifulSoup
import time 
import smtplib
import requests

#user info for the product they want to track, the price they are looking for
#and their email information
TARGET_PRICE = 20.00
EMAIL_ADDRESS = 'YOUR_GMAIL_EMAIL_ADDRESS_HERE'
HEADERS = {"User-Agent": "YOUR USER AGENT HERE"}
URL = "YOUR DESIRED PRODUCT AMAZON LINK HERE"

#uses a BeautifulSoup to parse amazon html response to recieve product title and price
def getPrice():
    response = requests.get(
        URL,
        headers = HEADERS
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    productTitle = soup.find(id="productTitle").get_text().strip()
    productPrice = soup.find(id="priceblock_ourprice").get_text().strip()[5:10]
    print(productTitle)
    return productPrice

#Checks price against target price
def checkPrice():
    price = float(getPrice())
    if price > TARGET_PRICE:
        variance = price - TARGET_PRICE
        print("The item is too expensive, currently {} dollars over budget".format(variance))
    else:
        print("It is time to BUY!")
        sendNotification()

#Called when TARGET_PRICE <= ACTUAL_PRICE to send an email to the user from their own email account
def sendNotification():
    email_subject = "Its time to buy your Amazon product"
    email_text = "Subject:"+email_subject+'\n\n'+"""The Amazon product that you were tracking is now below your target price point, 
click on the link to go to the product"""'\n'+URL
    
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'YOUR EMAIL PASSWORD HERE')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_text)

if __name__ == "__main__":
    while True:
        checkPrice()
        #Will loop throught the process once everyday
        time.sleep(86400)
    