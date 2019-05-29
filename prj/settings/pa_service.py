from .common import *

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'logistex018$prj_db',                               # DB 이름
        'USER':     'logistex018',                                      # DB 사용자 이름
        'PASSWORD': 'mysql2019',                                        # DB 비밀번호
        'HOST':     'logistex018.mysql.pythonanywhere-services.com',    # DB 서버 주소
        'PORT':     '',             # DB 포트 (생략하면 MySQL 디폴트 포트 3306 자동 지정)
        'OPTIONS':  {'charset': 'utf8mb4',
                     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # ***
                    },
    }
}