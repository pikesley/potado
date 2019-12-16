FROM python:3.7

RUN apt-get update && apt-get install -y make

ENV PROJECT potado

WORKDIR /opt/${PROJECT}
COPY ${PROJECT} /opt/${PROJECT}

RUN pip install --upgrade pip
RUN make install

COPY docker-config/bashrc /root/.bashrc
