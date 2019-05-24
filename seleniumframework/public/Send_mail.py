#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import sys

sys.path.append('F:\\PyTesting\\AutoTest\\public')
from public.ConfigParser import ReadConfigFile


def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    global lists
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1]) #多个路径组合后返回
    return file_path


# 格式化邮件地址
def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendMail(file_path):
    read = ReadConfigFile("TestReport")
    item_list = read.get_config_value()
    mail_addr = item_list[3][1] #baoyong@sdgakj.com
    head = item_list[4][1]  #疲劳驾驶测试报告
    smtp_server = 'smtp.qq.com'
    from_mail = '457950238@qq.com'
    mail_pass = 'pfapznjqpozacagh'
    to_mail = item_list[3][1] #wh18620385321@163.com,得到的是字符创
    print(to_mail)
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()
    # Header对中文进行转码
    msg['From'] = formatAddr('测试部 <%s>' % from_mail)
    msg['To'] = to_mail
    msg['Subject'] = Header(item_list[4][1], 'utf-8')
    # plain代表纯文本;html代表网页
    #msg.attach(MIMEText(body, _subtype='html', _charset='utf-8'))
    # 二进制方式模式文件
    #report_path = 'F:\\PyTesting\\AutoTest\\report\\'
    #attachment = new_file(report_path) #F://PyTesting//AutoTest//report//3.txt
    attachment1 = os.path.basename(file_path) #返回最后的文件名 3.txt
    with open(file_path, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=file_path)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename=attachment1)
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        msg.attach(mime)
    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, "25")
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, msg['To'].split(";"), msg.as_string())  # as_string()把MIMEText对象变成str
        print('%s----发送邮件成功------' %time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        s.quit()
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)


if __name__ == "__main__":
    report_path = 'F:\\PyTesting\\AutoTest\\report\\'
    attachment = new_file(report_path)
    print(attachment)
    sendMail(attachment)
