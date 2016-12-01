FROM registry.aliyuncs.com/21epub/ubuntu-python-env
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt  -i http://pypi.douban.com/simple/
RUN mkdir -p /var/log/nobody/info
RUN mkdir -p /var/log/nobody/error
EXPOSE 8000
ADD . /opt/project
WORKDIR /opt/project
ENV 'C_FORCE_ROOT' 'true'
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["gunicorn", "--worker-class=gevent", "personal_website.wsgi:application", "-b", "0.0.0.0:8080"]
#gunicorn --worker-class=gevent weixin_article.wsgi:application -b 127.0.0.1:8000&
#CMD ["gunicorn_thrift", "datastorage.thrift_app:app", "-b", "0.0.0.0:9090", "-k", "thrift_gevent", "-w", "2"]
#CMD ["/usr/bin/supervisord"]