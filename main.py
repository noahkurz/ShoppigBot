import requests
import bs4 as bs
from splinter import Browser
import helpers

#build the URL to attack... 
class supremeBot(object):
    def __init__(self, **info):
        self.base_url = 'https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163'
        self.login_url = 'https://www.bestbuy.com/identity/global/signin'
        self.checkout_url = 'https://www.bestbuy.com/checkout/r/fulfillment'
        #self.product = 'site/sony-playstation-5-console/6426149.p?skuId=6426149'
        #self.checkout = '/checkout'
        self.info = info
#this is all good...
    def initializeBrowser(self):
        driver = self.info["driver"]
        path = helpers.get_driver_path(driver)
        if driver == "geckodriver":
            self.b = Browser()
        elif driver == "chromedriver":
            executable_path = {"executable_path": path}
            self.b = Browser('chrome', **executable_path)
#So this is to find multiple products(in my case, so lets skip this for now)
#TO DO...

    def login(self):
        self.b.visit(
            "{}".format(
                self.login_url
            )
        )
        self.b.find_by_xpath("//*[@id='fld-e']").fill("noahkurz19@gmail.com")
        self.b.find_by_xpath("//*[@id='fld-p1']").fill("Sabers7168!")
        self.b.find_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[4]/button").click()
    
    def visitSite(self):
        self.b.visit(
            "{}".format(
                self.base_url))
        #//TO-DO find a more permanent solution to adding button to cart
        try:
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            
        except:
            timeout = 45
            self.b.visit(
            "{}".format(
                self.base_url))
            
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
            self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[8][1]").click()
    def checkout(self):

        self.b.visit("{}".format(self.checkout_url))
        self.b.visit("{}".format(self.checkout_url))
        self.b.find_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span").click()


    def submitPayment(self):
        #self.b.find_by_xpath("//*[@id='credit-card-cvv']").fill("137")
        self.b.find_by_xpath("//*[@id='credit-card-cvv']").fill("137")
        
        

        


if __name__ == "__main__":
    INFO = {
        "driver": "geckodriver"
    }
    BOT = supremeBot(**INFO)
    # Flag to set to true if you want to reload the page continously close to drop.
    #found_product = False
   # max_iter = 10
   # counter = 1
    #while not found_product and counter < max_iter:
    #    found_product = BOT.findProduct()
    #    print("Tried ", counter, " times")
    #    counter += 1
    #if not found_product:
    #    raise Exception("Couldn't find product. Sry bruhhhh")
    BOT.initializeBrowser()

    BOT.login()
    timeout = 45
    #BOT.visitSite()
    timeout = 45
    BOT.checkout()
    BOT.submitPayment()