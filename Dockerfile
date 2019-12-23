FROM python:3.8

RUN apt-get update && apt-get install -y make

ENV PROJECT potado

WORKDIR /opt/${PROJECT}
COPY ${PROJECT} /opt/${PROJECT}

RUN pip install --upgrade pip
RUN make install

COPY docker-config/bashrc /root/.bashrc

COPY ./entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
