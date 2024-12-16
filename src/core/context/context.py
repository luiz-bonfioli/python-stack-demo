from src.core.context.object_proxy import ObjectProxy


class Context:
    __instances = {}

    def get_alert_service(self):
        from src.domain.alert.alert_service import AlertService
        return ObjectProxy(
            lambda: AlertService(alert_repository=self.get_alert_repository()))

    @staticmethod
    def get_alert_repository():
        from src.domain.alert.alert_repository import AlertRepository
        return ObjectProxy(lambda: AlertRepository())

    def get_sensor_data_service(self):
        from src.domain.sensor_data.sensor_data_service import SensorDataService
        return ObjectProxy(
            lambda: SensorDataService(sensor_data_repository=self.get_sensor_data_repository()))

    @staticmethod
    def get_sensor_data_repository():
        from src.domain.sensor_data.sensor_data_repository import SensorDataRepository
        return ObjectProxy(lambda: SensorDataRepository())

    def get_sensor_data_receiver(self):
        from src.domain.sensor_data_receiver.sensor_data_receiver import SensorDataReceiver
        from src.core.common.config import SENSOR_DATA_TOPIC
        return ObjectProxy(lambda: SensorDataReceiver(self.get_kafka_client(SENSOR_DATA_TOPIC)))

    @staticmethod
    def get_sensor_data_consumer():
        from src.domain.sensor_data_consumer.sensor_data_consumer import SensorDataConsumer
        return ObjectProxy(lambda: SensorDataConsumer())

    @staticmethod
    def get_kafka_client(topic: str):
        from src.core.common.config import KAFKA_BOOTSTRAP_SERVERS
        from src.core.context.object_proxy import ObjectProxy
        from src.core.kafka.kafka_producer import KafkaProducer
        from confluent_kafka import Producer

        return ObjectProxy(
            lambda: KafkaProducer(kafka_producer=Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS}),
                                  topic=topic))


appcontext: Context = Context()
