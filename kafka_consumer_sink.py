from kafka import KafkaConsumer
import json
import sys
from cassandra.cluster import Cluster

bootstrap_servers = ['localhost:9092']
topicname = 'counts'
consumer = KafkaConsumer(topicname, bootstrap_servers = bootstrap_servers,auto_offset_reset='earliest',group_id="test-consumer-group")
cluster = Cluster(['127.0.0.1'], port = 9042)
session = cluster.connect('console')
try:
    for message in consumer:
        entry = json.loads(message.value)
        #entry = json.loads(json.loads(message.value))['log']
        session.execute(
                """
            INSERT INTO cctv_vehicle_counts (timeuuid_id, lgu_code , sensor_id  , time_saved , total , car , bus , truck , jeepney , bike , tryke , others )
            VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)
            """,(entry['timeuuid_id'],entry['lgu_code'],entry['sensor_id'],entry['time_saved'],entry['total'],entry['car'],entry['bus'],entry['truck'],entry['jeepney'],entry['bike'],entry['tryke'],entry['others']))
except KeyboardInterrupt:
    sys.exit()