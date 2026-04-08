import re
import smtplib
import dns.resolver
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime


def validate_email_format(email):
    """使用正则表达式验证邮箱格式是否合法"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def verify_email_smtp(email):
    """通过SMTP验证邮箱是否存在且可接收邮件（模拟握手）"""
    try:
        domain = email.split('@')
        # 获取该域名的MX记录
        print(domain)
        records = dns.resolver.resolve(domain[1], 'MX')
        print(records)
        mx_record = str(records.exchange)
        print(mx_record)

        # 连接到MX服务器进行模拟握手
        server = smtplib.SMTP(mx_record, 25, timeout=10)
        server.helo()
        server.mail('test@example.com')
        code, message = server.rcpt(email)
        print(code, message)
        server.quit()

        # 返回码250表示邮箱存在
        return code == 250
    except Exception:
        return False


def check_email_availability(email):
    """综合验证邮箱"""
    if not validate_email_format(email):
        return False
    return verify_email_smtp(email)

if __name__ == '__main__':
    print(verify_email_smtp('inclelee@163.com'))