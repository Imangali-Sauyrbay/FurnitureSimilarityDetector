from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import requests
import urllib.parse

from subprocess import CREATE_NO_WINDOW


def img_loaded(MIN_WIDTH):
    def __(driver):
        try:
            element = driver.find_element(By.CLASS_NAME, "MMImage-Origin")
            if int(element.get_attribute('naturalWidth')) >= MIN_WIDTH:
                return element
        except NoSuchElementException:
            return False
        return False
    return __

class ImageDriver:
    url = "https://yandex.kz/images/search?text={0}"
    next_btn_selector = '.CircleButton_type_next'
    anchor_to_original_selector = '.MMOrganicSnippet-Title.MMSidebar-SectionTitle'
    instance = None

    @staticmethod
    def get_instance(*args, **kwargs):
        if not ImageDriver.instance:
            ImageDriver.instance = ImageDriver(*args, **kwargs)

        return ImageDriver.instance

    def __init__(self, min_width=580, delay=10):
        self.min_width = min_width
        self.delay = delay
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.init_page()

    def init_page(self):
        self.load_page('hello')
        WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="serp-item__link"')))

    def load_page(self, query):
        self.driver.get(self.url.format(self.encode_str(query)))
        result = WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="serp-item__link"')))
        result.click()
        self.next_btn = WebDriverWait(self.driver, self.delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'CircleButton_type_next')))

    def next_image(self):
        try:
            el = WebDriverWait(self.driver, self.delay).until(img_loaded(self.min_width))
            a = self.driver.find_element(By.CSS_SELECTOR, self.anchor_to_original_selector)
            img_url = el.get_attribute('src')
            data = requests.get(img_url)
            self.next_btn.click()
            return data.content, a.get_attribute('href')
        except:
            self.next_btn.click()
            return self.next_image()


    def encode_str(self, string):
        return urllib.parse.quote_plus(string)

    def close(self):
        self.driver.quit()

