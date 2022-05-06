from requests import Session

class LoginApi:

    @staticmethod
    def login(session:Session,url,params):
        resp = session.get(url=url,params=params)
        return resp.json()

    @staticmethod
    def get_account(session:Session,url,data,headers):
        resp = session.post(url=url,data=data,headers=headers)
        return resp.json()
