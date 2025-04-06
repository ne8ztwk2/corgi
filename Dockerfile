FROM python:3.12-bookworm

WORKDIR /corgi

COPY . /corgi

RUN chmod +x /corgi/run.sh

CMD ["/bin/bash","/corgi/run.sh"]
