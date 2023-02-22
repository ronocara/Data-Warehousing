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
 <br>
 <p align="center">
    <img src="https://github.com/ronocara/Data-Warehousing/blob/main/readme-pics/producer.png?raw=true" alt="producer output">
   <br>Sample output from producer
</p>
<br><br>
