import unittest
import requests
import logging
from utils import get_assert
from api.loginAPI import loginAPI
from api.realnameAPI import realnameAPI


class realname(unittest.TestCase):
    phone1 = "13888843215"
    password = "test1234"
    realname = "李四"
    card_id = "41080119930228457x "
    def setUp(self) -> None:
        self.session = requests.Session()
        self.realnameapi = realnameAPI()
        self.logimgapi =loginAPI()

    def tearDown(self) -> None:
        self.session.close()

    def test01_getrealname(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        response = self.realnameapi.getrealname(self.session, self.realname, self.card_id)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '提交成功!')

    def test02_getapprove(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        response = self.realnameapi.getapprove(self.session)
        logging.info("response = {}".format(response.json()))


