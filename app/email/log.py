import logging
import logging.handlers

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'test@mail.com'
to_email = 'メールアドレス'
username = 'メールアドレス'
password = 'パスワード'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logging.info('test')
logger.critical('critical')

# ユースケースとしては、直接メールアドレスに送るのではなく、ログ解析ソフトにログを送って、メールにまとめて送信することが多い。