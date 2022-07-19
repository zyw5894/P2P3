import logging
import unittest
import requests

import app
from utils import get_assert, BD_Butile
from api.loginAPI import loginAPI
from api.realnameAPI import realnameAPI
from api.registerAPI import registerAPI
from utils import get_bs4_api
from api.tenderAPI import tenderAPI
import random

class lctest(unittest.TestCase):
    phone1 = "13888843217"
    imgVerifyCode = "8888"
    password = "test1234"
    realname = "李四"
    card_id = "370683198207280323"
    amount1 ='10000'
    amount2 = '100'
    def setUp(self) -> None:
        self.logimgapi = loginAPI()
        self.session = requests.Session()
        self.realnameapi = realnameAPI()
        self.registerapi = registerAPI()
        self.tenderapi = tenderAPI()
    @classmethod
    def tearDown(cls) -> None:
        cls.session.close()
        sql1 = ""
        BD_Butile.detele(app.DB_NAME1,sql1)


    def test01_getimg(self):
        # 图片验证
        r = random.randint(100000, 999999)
        response = self.logimgapi.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        # 短信验证
        response = self.logimgapi.getsendSms(session=self.session, phone=self.phone1, imgVerifyCode=self.imgVerifyCode)
        logging.info("register response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '短信发送成功')
        # 注册
        response = self.logimgapi.getreg(session=self.session, phone=self.phone1, password=self.password)
        logging.info("register response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '注册成功')
        # 登录
        response = self.logimgapi.getlogin(session=self.session, phone=self.phone1, password=self.password)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '登录成功')
        # 登录状态
        response = self.logimgapi.getislogin(session=self.session)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, 'OK')
        # 身份认证
        response = self.realnameapi.getrealname(self.session, self.realname, self.card_id)
        logging.info("response = {}".format(response.json()))
        get_assert(self, response, 200, 200, '提交成功!')
        # 查询认证
        response = self.realnameapi.getapprove(self.session)
        logging.info("response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)
        # 申请开户
        response = self.registerapi.get_registerapi(self.session)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        logging.info("form : {}".format(form_data))
        # 开户成功
        response = get_bs4_api(form_data)
        logging.info("response = {}".format(response.text))
        self.assertEqual('UserRegister OK', response.text)
        # 获取验证码
        r = random.random()
        response = self.registerapi.get_recharge_verify_code(self.session, str(r))
        logging.info("get recharge verify code reponse = {}".format(response.text))
        self.assertEqual(200, response.status_code)
        # 请求充值
        response = self.registerapi.get_rechargeapi(self.session, self.amount1)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        # 充值成功
        response = get_bs4_api(form_data)
        logging.info("response :{}".format(response.text))
        self.assertEqual("NetSave OK", response.text)
        # 请求投资
        response = self.tenderapi.tenderapi(self.session, self.amount2)
        logging.info("response = {}".format(response.json()))
        form_data = response.json().get("description").get("form")
        response = get_bs4_api(form_data)
        # 投资成功
        logging.info("response = {}".format(response.text))
        self.assertEqual("InitiativeTender OK", response.text)
        # 查看投资列表
        print("/////" * 10)
        response = self.tenderapi.mytenderlistapi(self.session, "tender")
        logging.info("response tender:{}".format(response.json()))
        response = self.tenderapi.mytenderlistapi(self.session, "recover")
        logging.info("response recover:{}".format(response.json()))
        print("/////" * 10)
        response = self.tenderapi.mytenderlistapi(self.session, "recover_yes")
        logging.info("response recover_yes:{}".format(response.json()))
        print("/////" * 10)
        response = self.tenderapi.mytenderlistapi(self.session, status="over", page="1")
        logging.info("response over:{}".format(response.json()))