FROM python

WORKDIR /rpa

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "arquivo.py"]