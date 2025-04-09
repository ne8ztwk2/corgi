FROM python:3.12-bookworm

WORKDIR /corgi

COPY .  /corgi

RUN sed -i 's|http://deb.debian.org/debian|https://mirrors.tuna.tsinghua.edu.cn/debian|g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && \
    pip install --no-cache-dir -r requirements.txt -i  https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple && \
    playwright install --with-deps && \
    apt-get clean 



