FROM python:3.8

EXPOSE 8080
WORKDIR /TO-DO-LIST

COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]