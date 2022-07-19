import json
import logging
import os
import requests
from bs4 import BeautifulSoup
import pymysql
import app


def get_assert(self,response,status_code,status,description ):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertEqual(description, response.json().get("description"))


def get_bs4_api(form_data):
    soup = BeautifulSoup(form_data, "html.parser")
    third_url = soup.form['action']
    logging.info("third_url={}".format(third_url))
    data = {}
    for input in soup.find_all('input'):
        data.setdefault(input['name'], input['value'])
    logging.info("data={}".format(data))
    response = requests.post(third_url, data=data)
    return response

class BD_Butile:
    @classmethod
    def get_conn(cls,db_name):
        conn = pymysql.connect(app.BASE_URL, app.DB_USERNAME, app.DB_PASSWORD, db_name, autocommit=True)
        return conn

    @classmethod
    def close(cls, cursor=None, conn=None):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    @classmethod
    def detele(cls,db_name,sql):
        try:
            conn = cls.get_conn(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            conn.rollback()
        finally:
            cls.close(cursor, conn)


def read_data(filename,method_name,param_name):

   file = app.Base_dir + "/data/" + filename
   test_case_data = []
   with open(file, encoding="utf-8") as f:
       file_data = json.load(f)
       test_data_list = file_data.get(method_name)
       for test_data in test_data_list:
           test_params = []
           for param in param_name.split(","):
               test_params.append(test_data.get(param))
           test_case_data.append(test_params)
   print(test_case_data)
   return test_case_data









