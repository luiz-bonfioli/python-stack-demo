from typing import Optional, Tuple, Set

from confluent_kafka import Producer, Message, KafkaError

from src.core.common.exceptions import KafkaPublishException
from src.core.common.logger import get_logger

logger = get_logger(__name__)


class KafkaProducer:

    def __init__(self, kafka_producer: Producer, topic: str):
        self.producer = kafka_producer
        self.topic = topic

    def __publish(self, key: str, message: bytes) -> None:
        self.producer.produce(topic=self.topic,
                              key=key,
                              value=message,
                              callback=self.on_delivery)

    def publish_messages(self, messages: Set[Tuple[str, bytes]]) -> None:
        for key, message in messages:
            logger.debug('Publishing message %s', key)
            self.__publish(key, message)
            logger.debug('Message published!')
        self.producer.flush()

    def on_delivery(self, error: Optional[KafkaError], msg: Message) -> None:
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if error is not None:
            logger.error(f"Message delivery failed {msg.key()}: {error}")
            raise KafkaPublishException(
                topic=msg.topic(),
                published_message=msg.value(),
                error_message=str(error)
            )
        else:
            logger.info(f"Message {msg.key()} delivered to {self.topic} [{msg.partition()}]")
