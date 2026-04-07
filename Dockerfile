FROM python:3.12-slim

# Установка OpenJDK 21 (вместо 17), curl, tar и Allure
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-21-jre-headless \
        curl \
        tar && \
    curl -L -o allure.tgz https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz && \
    tar -zxvf allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.32.0/bin/allure /usr/bin/allure && \
    rm allure.tgz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/workspace
COPY requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt