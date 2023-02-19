from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
from urllib.request import urlopen as uReq
import certifi
import ssl
import re
context = ssl.create_default_context(cafile=certifi.where())


# response= requests.get(ineuron_url)
# print(response.text)

class Scrapper:



    def ineuron_func(self):
        # self.input_string= input("enter your query")
        # ineuron_url = "https://ineuron.ai/"+ self.input_string
        # print(ineuron_url)
        self.uClient = uReq("https://ineuron.ai/courses", context=context, )

        self.ineuron_home_pag= self.uClient.read()
        print(self.ineuron_home_pag)

        self.uClient.close()

        self.ineuron_html_page=BeautifulSoup(self.ineuron_home_pag,"html.parser")
        # print(self.ineuron_html_page.get("class"))

obj=Scrapper()

obj.ineuron_func()