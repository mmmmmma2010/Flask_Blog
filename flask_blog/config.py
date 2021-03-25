import os



class Config :
    SECRET_KEY='29ef65552e0e8c053fd2ebcb1d71481a'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME= 'mmmmmma20102@gmail.com'#os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= '201019962011'#os.environ.get('EMAIL_PASS') 