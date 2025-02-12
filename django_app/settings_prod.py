from .settings import *

# 운영환경에서는 반드시 False로 설정
DEBUG = True

#  elastic beanstalk 도메인 붙여 넣기
ALLOWED_HOSTS = ['eb-django-app-env.eba-tauze2ug.ap-northeast-2.elasticbeanstalk.com']