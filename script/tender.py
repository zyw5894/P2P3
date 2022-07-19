import logging
import unittest
import requests
from api.tenderAPI import tenderAPI
from utils import get_assert
from api.loginAPI import loginAPI
from utils import get_bs4_api

class tender(unittest.TestCase):
    amount = "100"
    phone1 = "13888843215"
    password = "test1234"
    def setUp(self) -> None:
        self.session = requests.Session()
        self.tenderapi = tenderAPI()
        self.logimgapi = loginAPI()

    def tearDown(self) -> None:
        self.session.close()

    def test01_tender(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        response = self.tenderapi.tenderapi(self.session, self.amount)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        response = get_bs4_api(form_data)
        logging.info("response = {}".format(response.text))
        self.assertEqual("InitiativeTender OK", response.text)

    def test02_m(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        response = self.tenderapi.mytenderlistapi(self.session, "recover")
        logging.info("response :{}".format(response.json()))
        print("/////" * 10)
        response = self.tenderapi.mytenderlistapi(self.session, "recover_yes")
        logging.info("response :{}".format(response.json()))
        print("/////"*10)
        response = self.tenderapi.mytenderlistapi(self.session, status="over", page="1")
        logging.info("response :{}".format(response.json()))

