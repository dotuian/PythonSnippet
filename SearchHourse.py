#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: SearchHourse.py

import urllib2
import time
import datetime
import os
import codecs

import smtplib
from email import Encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.base import MIMEBase

from bs4 import BeautifulSoup

# ==========================================
# pip install beautifulsoup4
# pip install email
# ==========================================

class SearchHourse :

    def __init__(self):
        self.SMTP = "mail.xxxx.jp"
        self.PORT = "587"
        self.USERNAME ="xxxx@xxxx.jp"
        self.PASSWARD = 'xxxx'
        self.TO = ["xxxx@outlook.com"]

    def create_message(self, from_addr, to_addr, subject, body, mime=None, attach_file=None):
        """
            create mail message
        """
        message = MIMEMultipart()
        message["From"] = from_addr
        message["To"] = to_addr
        message["Date"] = formatdate()
        message["Subject"] = subject
        #body = MIMEText(body, 'html')
        #body = MIMEText(body.encode('utf-8'), 'html','utf-8')
        body = MIMEText(body.encode('utf-8'), 'plain','utf-8')
        message.attach(body)

        if mime != None and attach_file != None:
            attachment = MIMEBase(mime['type'],mime['subtype'])
            file = open(attach_file['path'])
            attachment.set_payload(file.read())
            file.close()
            Encoders.encode_base64(attachment)
            message.attach(attachment)
            attachment.add_header("Content-Disposition","attachment", filename=attach_file['name'])

        return message

    def send(self, from_addr, to_addrs, msg):
        """
            send mail message
        """
        smtpobj = smtplib.SMTP(self.SMTP, self.PORT)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.USERNAME, self.PASSWARD)
        smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
        smtpobj.close()

    def search(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = ""
        count = 0

        homepage = 'http://www.ur-net.go.jp/akiya/tokyo/20_2810.html'

        url = "http://chintai.sumai.ur-net.go.jp/kanto/html_list.ashx"
        url += "?{timestamp}&DCD=281&FLOORPLAN&KUID=URK1452840344209chrome&PAGE&PRICE"
        url += "&RANK&SCD=20&SKCD=0&SORT&SORTYPE&SYSTEM&TYPE=3&VIEW=1"
        url = url.replace("{timestamp}", str(time.time()))

        if os.name == 'nt': #is windows
            path = "d:/" + datetime.datetime.now().strftime('%Y-%m-%d') + ".tmp"
        elif os.name == 'posix': # is linux
            path = "/home/shoukii/hy/" + datetime.datetime.now().strftime('%Y-%m-%d') + ".tmp"

        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")

        #割引制度有無
        for link in soup.select('dl.ft_system'):
            # 割引制度の個数
            count = len(link.find_all('dd'))
            # 割引制度項目
            message += ', '.join(x.string for x in link.select("dd"))

        #割引制度明細
        for link in soup.select('ul.tb_list_type table.tbList'):
            type = ""
            rent=""
            number=""
            discount=False
            # 間取り
            for value in link.select('td.rm_type'):
                type = value.string
            # 家賃
            for value in link.select('td.rm_yachin > span'):
                rent = value.string
            # 号棟
            for value in link.select('td.rm_number > a > div.sp_i > div'):
                number = value.get_text()[:-5]
            # 割引対象
            for value in link.select('td.rm_applay > p > a > img'):
                discount = True
            if discount :
                message += "\r\n%s %s %s " %(type, number, rent)

        #メール送信
        if self.check(count, path, message):
            # メール内容
            msg = self.create_message(self.USERNAME, self.TO[0], "Search House By Python", message + "\r\n" + homepage)
            # 送信
            self.send(self.USERNAME, self.TO, msg)
            print(msg.as_string())

            #ファイルに書き込む
            self.put_all_content(path, message)
        else:
            print("%s %s \r\n %s\r\n\r\n" %(now, 'No Send',  message))

    def __len__(self):
        return 0

    def check(self, count, path, message):
        if not os.path.exists(path) and count > 0:
            return True

        str = self.get_all_content(path)
        if os.path.exists(path) and self.get_all_content(path) != message:
            return True

        return False

    def get_all_content(self, path):
        content = ""
        for line in codecs.open(path, 'r', "utf_8") :
            content += line
        return content

    def put_all_content(self, path, content):
        file = codecs.open(path, 'w', "utf_8")
        file.write(content)
        file.close()

if __name__ == "__main__":
    object = SearchHourse()
    object.search()
