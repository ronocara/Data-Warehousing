# Data-Warehousing
 big data streaming pipeline and integration platform project using kafka and Cassandra connectors.


This school project required us to build a Data Streaming Pipeline and Integration Platform with the following requirements:

   - from 10 different data producers that will be sent to a Kafka topic.
   - make a database using Cassandra to store data from the producers.
   - A Python program that fetches the latest batch of data that arrived in Kafka and then sends (saves) this batch of data to Cassandra)

This project was implemented on my local computer using Ubuntu. The project documentation is as follows:
 
------------------------
<br>
<p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/dataWH1.png?raw=true" alt="kafka and zookeper">
   <br> Kafka and Zookeeper first need to be run in the terminal
  <br(terminal commands available in 'Notes')
</p>
 
 10 different producers are now simultaneously run to sen  data produced to a topic in Kafka.
 The producers sends data of different vehicle records, such as their time and date of arrival, vehicle type, and lgu code. 
 <br><br>
 <p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/producer.png?raw=true" alt="producer output">
   <br>Sample output from producer
</p>
<br><br>
The data will be read by the consumer 
 <br>
 
 <p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/consumer.png?raw=true" alt="consumer output">
   <br>Sample output from consumer
</p>

A dataase will now be made using Cassandra to store all the data from the producers. A python program 'kafka_consumer_sink.py' will now be used to fetch the latest batch of data that arrived in Kafka to the be sent and saved to the Cassandra database. 

<p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/cass-table.png?raw=true" alt="consumer output">
   <br>Cassandra database before fetching data
</p>

<p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/cass-table2.png?raw=true" alt="consumer output">
   <br>Cassandra database after fetching data
</p>
