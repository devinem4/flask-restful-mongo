FROM python:3.7
WORKDIR /src/app
ADD ./requirements.txt /src/app
RUN pip install -r requirements.txt

ADD ./api.py /src/app
EXPOSE 5000
ENTRYPOINT ["python","api.py"]
