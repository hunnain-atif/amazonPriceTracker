# amazonPriceTracker

## General Information
Python script that tracks the price of an Amazon product using a provided URL. The script is timed to run once a day and ideal for use on a small system like Raspberry pi or Ardunio. The script gets the price of the product and compares it to a provided target price. If the price is below the target price the user is sent an email witht he link to the product and a message telling them its time to BUY!

## Technologies / Frameworks
- BeautifulSoup
- smtplib

## Next Steps
- [ ] ability to track multiple products
- [ ] customizable amount of times run (user can choose how often price is checked)
