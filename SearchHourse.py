#!/usr/bin/python

import urllib2
import time
import datetime
import os.path

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
        self.TO = ["to@xxxx.com"]

    def create_message(self, from_addr, to_addr, subject, body, mime=None, attach_file=None):
        """
        """
        message = MIMEMultipart()
        message["From"] = from_addr
        message["To"] = to_addr
        message["Date"] = formatdate()
        message["Subject"] = subject
        body = MIMEText(body)
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
        """
        smtpobj = smtplib.SMTP(self.SMTP, self.PORT)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.USERNAME, self.PASSWARD)
        smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
        smtpobj.close()

    def search(self):
        homepage = 'http://www.ur-net.go.jp/akiya/tokyo/20_2810.html'

        url = "http://chintai.sumai.ur-net.go.jp/kanto/html_list.ashx?{timestamp}&VIEW=1&TYPE=3&SCD=20&DCD=281&SKCD=0&SORT=%22%22&SORTYPE=%22%22&PRICE=%22%22&SYSTEM=%22%22&FLOORPLAN=%22%22&RANK=%22%22&KUID=URK1452840344209chrome"
        url = url.replace("{timestamp}", str( time.time()))

        path = "/home/shoukii/hy/" + datetime.datetime.now().strftime('%Y-%m-%d-%H') + ".hy"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if os.path.exists(path) :
            print("%s : Already been sent \n\n"  %( now ))
            return

        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")
        for link in soup.select('dl.ft_system'):
        #for link in soup.select('dl'):
            value = link.find_all('dd')
            if len(value) > 0 and not os.path.exists(path):
                body = ', '.join(str(x) for x in value)
                body += "\n\n"
                body += homepage

                # create message
                msg = self.create_message(self.USERNAME, self.TO[0], "Search House By Python", body)
                print("%s \n %s \n\n"  %(now, msg.as_string()))
                # send message
                self.send(self.USERNAME, self.TO, msg)

                #
                file = open(path, 'w+')

    def __len__(self):
        return 0

if __name__ == "__main__":
    object = SearchHourse()
    object.search()
