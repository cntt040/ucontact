FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python-dev libpq-dev curl
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install requests==2.5.3
RUN pip install pycouchdb==1.13
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
VOLUME /src/logs
EXPOSE 8000
#CMD ["python", "main.py"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
