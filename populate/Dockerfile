FROM ubuntu

RUN apt-get update && apt-get install python python-pip -y

ADD . /

RUN pip install -r /requirements.txt

CMD python /main.py