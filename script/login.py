import logging
import unittest
import requests
from utils import get_assert
from api.loginAPI import loginAPI
import random

class login(unittest.TestCase):
    phone1 = "13888843215"
    imgVerifyCode = "8888"
    password = "test1234"
    def setUp(self) -> None:
        self.logimgapi = loginAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()


    def test01_getimg(self):
        r = random.random()
        response = self.logimgapi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test02_getimg2(self):
        r = random.randint(100000, 999999)
        response = self.logimgapi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test03_getsendSms(self):
        r = random.randint(100000, 999999)
        response = self.logimgapi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        response =self.logimgapi.getsendSms(session=self.session, phone=self.phone1,imgVerifyCode=self.imgVerifyCode)
        self.assertEqual(200, response.status_code)
        self.assertEqual("短信发送成功", response.json().get("description"))

    def test04_getreg(self):
        r = random.randint(100000, 999999)
        response = self.logimgapi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        response = self.logimgapi.getsendSms(session=self.session, phone=self.phone1, imgVerifyCode=self.imgVerifyCode)
        logging.info("register response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("短信发送成功", response.json().get("description"))
        response = self.logimgapi.getreg(session=self.session, phone=self.phone1, password=self.password)
        logging.info("register response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("status"))
        self.assertEqual("注册成功", response.json().get("description"))

    def test05_login(self):
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("status"))
        self.assertEqual("登录成功", response.json().get("description"))
        # 查看登录状态
        response = self.logimgapi.getislogin(session=self.session)
        logging.info("response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("status"))
        self.assertEqual("OK", response.json().get("description"))
        get_assert(self,response,200,200,"OK")




