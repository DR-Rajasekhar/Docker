FROM ubuntu:20.04
LABEL owner="raajasekharr@gmail.com"
LABEL version="1.0"
ARG VERSION='1.4.5'
RUN apt update
RUN apt install -y nginx jq curl wget unzip
COPY index.html /var/www/html/index.nginx-debian.html
COPY style.css /var/www/html/style.css
COPY scorekeeper.js /var/www/html/scorekeeper.js
ADD error.html /var/www/html/error.html
ADD https://releases.hashicorp.com/terraform/${VERSION}/terraform_${VERSION}_linux_amd64.zip /usr/local/bin/terraform.zip
RUN cd /usr/local/bin/ && unzip terraform.zip && rm -rf *.zip && terraform version