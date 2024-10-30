import base64, io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from matplotlib import pyplot as plt

# email 발송
def send_approval_email_sync(receiver_email):
    sender_email = "teereal@naver.com"
    sender_password = "WEDVPB9ZUMJF"

    subject = "승인 요청이 승인되었습니다"
    body = "당신의 방문 요청이 승인되었습니다. 감사합니다."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.naver.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"일반 오류 발생: {e}")

# 통계 그래프
def save_graph_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    return f"data:image/png;base64,{graph_url}"