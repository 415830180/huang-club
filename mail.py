from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from flask import render_template

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(to,ip,code):
    from_addr = "zedonghuang.club@qq.com"
    password = 'xxxxxxxxxxxxxxx'
    to_addr = to
    smtp_server = 'smtp.qq.com'
    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    html = render_template("mail.html",
                            ip=ip, code=code)
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = _format_addr('huang club 官方团队 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('Huang_club 验证信息', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()



