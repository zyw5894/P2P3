import app

class registerAPI():
    def __init__(self):
        self.register_url = app.Base_url + '/trust/trust/register'
        self.get_verify_url = app.Base_url + '/common/public/verifycode/'
        self.get_recharge_url = app.Base_url + '/trust/trust/recharge'

    def get_registerapi(self, session):
        return session.post(self.register_url)

    def get_recharge_verify_code(self, session, r):
        url = self.get_verify_url + r
        response = session.get(url)
        return response

    def get_rechargeapi(self, session, amount):
        data = {"paymentType": "chinapnrTrust",
                "formStr": "reForm",
                "amount": amount,
                "valicode": "8888"}
        return session.post(self.get_recharge_url, data=data)
