import app


class tenderAPI():
    def __init__(self):
        self.tender_url = app.Base_url + "/trust/trust/tender"
        self.mytenderlist_url = app.Base_url + '/loan/tender/mytenderlist'

    def tenderapi(self, session, amount):
        data = {
        "id": "642",
        " depositCertificate": "-1",
        "amount": amount
        }
        return session.post(self.tender_url, data=data)

    def mytenderlistapi(self, session, status, page=""):
        data = {
            "status": status,
            "page": page
        }
        return session.post(self.mytenderlist_url,data=data)