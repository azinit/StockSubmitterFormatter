class PapaStocker(object):
    SERVICE_URL = "https://papastocker.ru/keysMaker"

    def __init__(self, limit=50):
        from webdriver_manager.chrome import ChromeDriverManager
        self.browser_path = ChromeDriverManager().install()
        self.browser      = None
        self.limit        = limit
        self.is_running   = False

    """
    ..............................................................................................................
    ................................................ GET KEYWORDS ................................................
    ..............................................................................................................
    """

    def run(self):
        from selenium import webdriver
        if not self.is_running:
            self.is_running = True
            self.browser = webdriver.Chrome(self.browser_path)
            self.browser.get(self.SERVICE_URL)

    def get_keywords(self, term):
        from tkinter import Tk

        browser = self.browser
        if browser is not None:
            # Send term
            queries = browser.find_element_by_id("id_queries")
            queries.clear()
            queries.send_keys(term)

            pickup_btn = browser.find_element_by_class_name("keyerSubmitBtn2")
            pickup_btn.click()
            # Get and copy keys
            copy_btn = browser.find_element_by_class_name("btn_copyKeys")
            copy_btn.click()
            data = Tk().clipboard_get().split(", ")
            return data
        else:
            print("BROWSER IS NONE")
            return None

    def close(self):
        self.browser.close()

    # def __get_keywords(self):
    #     """ Sending request for stocker """
    #     from fios.web import webkit
    #     import requests
    #     from bs4 import BeautifulSoup
    #     # soup = webkit.soupify(self.SERVICE_URL)
    #
    #     self.term = "paper list"
    #     url = self.SERVICE_URL
    #
    #     headers = {
    #         # 'accept': 'text/html,application/xhtml+xml,application/xml',
    #         "cookie": "",
    #         "referer": "https://papastocker.ru/keysMaker",
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    #     }
    #
    #     payload = {
    #         "csrfmiddlewaretoken": "",
    #         "queries": self.term,
    #         "exclude": "",
    #         "imagetype": "popular",
    #         "mplusmode": False,
    #     }
    #
    #     with requests.Session() as session:
    #         r       = session.get(url, headers=headers)
    #         print(r.cookies)
    #         soup    = BeautifulSoup(r.content, "html.parser")
    #         csrf    = soup.find("input", attrs={"name": "csrfmiddlewaretoken"})["value"]
    #         payload["csrfmiddlewaretoken"] = csrf
    #         headers["cookie"] = "csrftoken={csrf}; _ym_uid=1565100046641853535; _ym_d=1565100046; _ym_isad=1; sessionid=o0izo4s25qgnnxowz3c7g6lu80uhgswf; _ym_visorc_41615454=w".format(
    #             csrf=csrf
    #         )
    #
    #         # headers['cookie'] = '; '.join([x.name + '=' + x.value for x in r.cookies])
    #         # headers['content-type'] = 'application/x-www-form-urlencoded'
    #         # r = requests.post(url, data=payload, headers=headers)
    #         # headers['cookie'] = '; '.join([x.name + '=' + x.value for x in r.cookies])
    #         driver = self.init_driver()
    #         copy_btn = driver.find_element_by_class_name("btn_copyKeys")
    #         print(copy_btn)
    #         # print(r.text)
    #         # print(r.status_code)
    #
    #         # r = session.post(
    #         #     url=url,
    #         #     data=payload,
    #         #     headers=headers,
    #         #     proxies={"http": proxy}
    #         # )
    #         # input(r.status_code)
    #         # print(r.text)
    #     return -1

    # def init_driver(self):
    #     from selenium import webdriver
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--ignore-certificate-errors')
    #     options.add_argument("--test-type")
    #     # options.binary_location = "/usr/bin/chromium"
    #     driver = webdriver.Chrome(chrome_options=options)
    #     driver.get(self.SERVICE_URL)
    #     return driver
    #
    # def run_browser(self, terms):
    #     import time
    #     from tkinter import Tk
    #
    #     browser = self.init_browser()
    #     for term in terms:
    #         # Send term
    #         queries         = browser.find_element_by_id("id_queries")
    #         queries.clear()
    #         queries.send_keys(term)
    #
    #         pickup_btn      = browser.find_element_by_class_name("keyerSubmitBtn2")
    #         pickup_btn.click()
    #         # Get and copy keys
    #         copy_btn = browser.find_element_by_class_name("btn_copyKeys")
    #         copy_btn.click()
    #         data = Tk().clipboard_get().split(", ")
    #         print(term, len(data), data)
    #         time.sleep(1)
    #         # input("...")


if __name__ == '__main__':
    expected = ["male, strength, white, people, cape, adult, design, standing, red, confident, hero, superhero, super, girl, style, blue, fun, rescue, beautiful, graphic, wind, symbol, cloak, cute, satin, office, winner, imagination, idea, childhood, career, vector, isolated, man, business, costume, 3d, power, businessman, concept, character, illustration, flying, woman, cloth, strong, employee, silk, cartoon, success"]
    terms = ["Red cape", "Businessman icon", "Medical icon", "Future technology icon"]
    stocker = PapaStocker("")
    stocker.run_browser(terms)
    # actual = stocker.get_keywords()
    # print(actual)
