FROM python:3.10
LABEL authors="ular"

RUN git clone git@github.com:raevul/Neobis_Tour.git/Neobis_Tour/neotour

WORKDIR /Neobis_Tour/neotour

RUN ls .

RUN pip install -r requirements.txt

VOLUME /Neobis_Tour/neotour

EXPOSE 8000

ENTRYPOINT ["top", "-b"]