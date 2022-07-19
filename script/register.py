import unittest
from random import random

import requests
import logging
from utils import get_bs4_api
from bs4 import BeautifulSoup

from utils import get_assert
from api.loginAPI import loginAPI
from api.registerAPI import registerAPI


class register(unittest.TestCase):
    phone1 = "13888843215"
    password = "test1234"
    amount = "10000"


    def setUp(self) -> None:
        self.registerapi = registerAPI()
        self.session = requests.Session()
        self.logimgapi = loginAPI()

    def tearDown(self) -> None:
        self.session.close()

    def test01_register(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        response = self.registerapi.get_registerapi(self.session)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        logging.info("form : {}".format(form_data))

        response = get_bs4_api(form_data)
        logging.info("response = {}".format(response.text))
        self.assertEqual('NetSave OK', response.text)

    def test02_recharge_verify_code(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')

        r = random()
        response = self.registerapi.get_recharge_verify_code(self.session, str(r))
        logging.info("get recharge verify code reponse = {}".format(response.text))
        self.assertEqual(200, response.status_code)

        response = self.registerapi.get_rechargeapi(self.session, self.amount)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        response = get_bs4_api(form_data)
        logging.info("response :{}".format(response.text))
        self.assertEqual("NetSave OK", response.text)



