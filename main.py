import requests
import bs4 as bs
from splinter import Browser
import helpers
import time

#build the URL to attack... 
class shoppingBot(object):
    def __init__(self, **info):
        self.product_url = 'https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163'
        self.login_url = 'https://www.bestbuy.com/identity/global/signin'
        self.checkout_url = 'https://www.bestbuy.com/checkout/r/fulfillment'
        self.info = info

    def startBrowser(self):
        driver = self.info["driver"]
        path = helpers.get_driver_path(driver)
        if driver == "geckodriver":
            self.b = Browser()
        elif driver == "chromedriver":
            print("Chrome is currently not supported...coming soon... working out a few bugs")

    def login(self):
        self.b.visit(
            "{}".format(
                self.login_url
            )
        )
        self.b.find_by_xpath("//*[@id='fld-e']").fill("")#enter ypur emai;
        self.b.find_by_xpath("//*[@id='fld-p1']").fill("")#enter your best buy password associated with the email.
        self.b.find_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[4]/button").click()
    
    def allocateProduct(self):
        self.b.visit(
            "{}".format(
                self.product_url))
        #//TO-DO find a more permanent solution to adding button to cart
        try:
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()   
        except:
            time.sleep(4)
            self.allocateProduct()
        return True
    
    def checkout(self):
        self.b.visit("{}".format(self.checkout_url))
        self.b.visit("{}".format(self.checkout_url))
        self.b.find_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span").click()

    def submitPayment(self):
        try:
            self.b.find_by_xpath("//*[@id='credit-card-cvv']").fill("")#enter the CCV code associated with your best buy account
        except:
            time.sleep(2)
            self.b.find_by_xpath("//*[@id='credit-card-cvv']").fill("")#enter the CCV code associated with your best buy account
        print("we made it to the end!")
        #self.b.find_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button").click()



        


if __name__ == "__main__":
    INFO = {
        "driver": "geckodriver"
    }
    BOT = shoppingBot(**INFO)
    print("Hello, buying Bot at your service!...\n")
    print("Bot starting browser now...\n")
    BOT.startBrowser()
    print("Bot is now starting the process of securing a ps5...\n")
    BOT.login()
    print("Bot is logging in...\n")
    time.sleep(1)
    prodAvail = False
    maxTries = 100
    numTries = 1
    while not prodAvail and numTries <= maxTries:
        prodAvail = BOT.allocateProduct()
        print(numTries)
        numTries = numTries + 1
    #BOT.allocateProduct()
    print("Bot is trying to add product to cart...\n")
    BOT.checkout()
    print("Bot is starting checkout process...\n")
    BOT.submitPayment()
    print("Bot confirms that ps5 is secured.")
