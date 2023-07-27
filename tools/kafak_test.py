# consumer
from kafka import KafkaConsumer

consumer = KafkaConsumer('sample')
for message in consumer:
	print(message)
	print(message.value)








#producer
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
for i in range(10):
	producer.send('sample', b'Hello, World!')
	producer.send('sample', key = b'message-two', value = b'This is Kafka-Python')
	print(producer)
	producer.flush()
	time.sleep(2)
