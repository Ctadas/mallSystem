from __future__ import absolute_import, unicode_literals
import pymysql   
pymysql.install_as_MySQLdb()

# 告诉Django在启动时别忘了检测我的celery文件
from .celery import app as celery_ap
__all__ = ['celery_app']