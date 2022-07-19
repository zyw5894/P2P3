import requests
import app
class loginAPI():
    def __init__(self):
        self.getImgCode_url = app.Base_url + '/common/public/verifycode1/'
        self.getsendSms_url = app.Base_url + '/member/public/sendSms'
        self.getreg_url = app.Base_url + '/member/public/reg'
        self.getislogin_url = app.Base_url + '/member/public/islogin'
        self.getlogin_url = app.Base_url + "/member/public/login"

    # 图片验证码
    def getImgCode(self, session, r):
        url = self.getImgCode_url + r
        response = session.get(url)
        return response
    # 短信验证码
    def getsendSms(self,session,phone,imgVerifyCode):
        url = self.getsendSms_url
        data = {'phone':phone,"imgVerifyCode":imgVerifyCode,'type':"reg"}
        response = session.post(url,data=data)
        return response
    # 注册
    def getreg(self, session, phone, password, imgVerifyCode="8888", phoneCode="666666", dyServer="on", invite_phone=''):
        url = self.getreg_url
        data = {"phone": phone,
                "password": password,
                "verifycode": imgVerifyCode,
                "phone_code": phoneCode,
                "dy_server": dyServer,
                'invite_phone': invite_phone}
        response = session.post(url, data=data)
        return response

    # 登录
    def getlogin(self, session, phone, password):
        url = self.getlogin_url
        data = {
            "keywords": phone,"password": password,
        }
        response = session.post(url, data=data)
        return response
    # 查看登录状态
    def getislogin(self,session):
        url = self.getislogin_url
        response = session.post(url)
        return response


