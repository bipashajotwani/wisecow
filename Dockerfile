FROM ubuntu:latest

RUN apt-get update && apt-get install -y cowsay fortune netcat-openbsd

ENV PATH="/usr/games:${PATH}"

COPY wisecow.sh /wisecow.sh

RUN chmod +x /wisecow.sh

EXPOSE 4499

CMD ["/wisecow.sh"]