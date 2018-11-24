FROM python:2.7

RUN apt-get update && \
 apt-get install -y supervisor unzip

ENV CONSUL_TEMPLATE_VERSION 0.11.1
ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/consul-template.zip

RUN unzip /tmp/consul-template.zip -d /usr/bin && \
    chmod +x /usr/bin/consul-template && \
    rm /tmp/consul-template.zip && \
    mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY supervisor/* /etc/supervisor/conf.d/
COPY . .
EXPOSE 80

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]