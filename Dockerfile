FROM python:3
WORKDIR /home/cara/CS172
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY...
CMD [ "python", "-u", "./kafka_consumer_sink.py" ]