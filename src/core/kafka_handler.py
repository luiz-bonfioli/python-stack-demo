from src.core.common.config import SENSOR_DATA_TOPIC, KAFKA_BOOTSTRAP_SERVERS
from src.core.context.context import appcontext
from src.core.kafka.kafka_consumer import KafkaConsumer

config = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'auto.offset.reset': 'earliest'
}

if __name__ == '__main__':
    sensor_data_consumer = appcontext.get_sensor_data_consumer()

    KafkaConsumer(topic=SENSOR_DATA_TOPIC,
                  group_id="sensor.data.consumer",
                  config=config,
                  on_message=sensor_data_consumer.read_sensor_data,
                  on_error=sensor_data_consumer.sensor_data_error)
