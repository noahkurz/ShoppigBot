import requests
import bs4 as bs
from splinter import Browser
import helpers

#build the URL to attack... 
class supremeBot(object):
    def __init__(self, **info):
        self.base_url = 'https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163'
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
    def findProduct(self):
        try:
            r = requests.get(
                "{}{}{}".format(
                    self.base_url,
                    self.product)).text
            soup = bs.BeautifulSoup(r, 'lxml')

            temp_tuple = []
            temp_link = []

            for link in soup.find_all('a', href=True):
                temp_tuple.append((link['href'], link.text))
            for i in temp_tuple:
                if i[1] == self.info['product'] or i[1] == self.info['color']:
                    temp_link.append(i[0])

            self.final_link = list(
                set([x for x in temp_link if temp_link.count(x) == 2]))[0]
            return True
        except:
            return False

    def visitSite(self):
        self.b.visit(
            "{}".format(
                self.base_url))
        self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7][1]").click()
        self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7][1]").click()
        self.b.find_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7][1]").click()
    def checkoutFunc(self):

        self.b.visit("{}{}".format(self.base_url, self.checkout))

        self.b.fill("order[billing_name]", self.info['namefield'])
        self.b.fill("order[email]", self.info['emailfield'])
        self.b.fill("order[tel]", self.info['phonefield'])

        self.b.fill("order[billing_address]", self.info['addressfield'])
        self.b.fill("order[billing_city]", self.info['city'])
        self.b.fill("order[billing_zip]", self.info['zip'])
        self.b.select("order[billing_country]", self.info['country'])

        self.b.select("credit_card[type]", self.info['card'])
        self.b.fill("credit_card[cnb]", self.info['number'])
        self.b.select("credit_card[month]", self.info['month'])
        self.b.select("credit_card[year]", self.info['year'])
        self.b.fill("credit_card[ovv]", self.info['ccv'])
        self.b.find_by_css('.terms').click()
        #self.b.find_by_value("process payment").click()


if __name__ == "__main__":
    INFO = {
        "driver": "geckodriver",
        "product": "Thermal Zip Up Hooded Sweatshirt",
        "color": "Tangerine",
        "size": "Medium",
        "category": "sweatshirts",
        "namefield": "example",
        "emailfield": "example@example.com",
        "phonefield": "XXXXXXXXXX",
        "addressfield": "example road",
        "city": "example",
        "zip": "72046",
        "country": "GB",
        "card": "visa",
        "number": "1234123412341234",
        "month": "09",
        "year": "2020",
        "ccv": "123"
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
    BOT.visitSite()
    #BOT.checkoutFunc()
