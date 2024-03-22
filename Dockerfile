FROM python:3.9

RUN pip install flask

COPY app.py /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
