# -*- coding: utf-8 -*-
import sys
from kafka import KafkaConsumer
import json
from cassandra.cluster import Cluster

#cluster = Cluster(['127.0.0.1'], port = 9042)
#session = cluster.connect('console')

consumer = KafkaConsumer(
    'counts',         #cctv_vehicle_counts
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = 'latest',
    enable_auto_commit = True
    )

for message in consumer:
    message = message.value
    print(message)
    



    