FROM python:3.12.0
FROM public.ecr.aws/amazonlinux/amazonlinux:latest


RUN yum update -y && \
yum install -y httpd
RUN echo 'Hello World!' > /var/www/html/index.html

RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
chmod 755 /root/run_apache.sh

EXPOSE 5000

CMD /root/run_apache.sh

COPY . /Bot

WORKDIR /Bot

RUN pip install -r requirements.txt

EXPOSE 5000


RUN mkdir ~/.taipy

RUN cp config.toml ~/.taipy/config.toml


ENTRYPOINT ["taipy", "run"]

CMD ["main.py"]