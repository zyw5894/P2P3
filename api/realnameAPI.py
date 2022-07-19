import app
class realnameAPI():
    def __init__(self):
        self.getrealname_url = app.Base_url + '/member/realname/approverealname'
        self.getapprove_url = app.Base_url + '/member/member/getapprove'

    def getrealname(self, session, realname, card_id):
        url = self.getrealname_url
        data = {"realname": realname, "card_id": card_id}
        response = session.post(url, data=data, files={'x':'y'})
        return response

    def getapprove(self, session):
        return session.post(self.getapprove_url)