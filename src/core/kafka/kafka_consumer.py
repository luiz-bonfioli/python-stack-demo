#!/usr/bin/env python

from confluent_kafka import Consumer

from src.core.common.logger import get_logger

logger = get_logger(__name__)


class KafkaConsumer:
    """
    KafkaConsumer is a class that simplifies consuming messages from a Kafka topic
    in a consumer group. It continuously polls for new messages and invokes the
    provided callback functions for successful message consumption and error handling.

    The consumer handles message polling in an infinite loop, allowing for seamless
    real-time message processing. It also gracefully handles shutdown by closing
    the Kafka consumer and committing final offsets.
    """

    def __init__(self, topic: str, group_id: str, config: dict, on_message=None, on_error=None):
        consumer = self.setup(config, group_id, topic)

        # Poll for new messages from Kafka and callback them.
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    # Initial message consumption may take up to
                    # `session.timeout.ms` for the consumer group to
                    # rebalance and start consuming
                    logger.debug("Waiting...")
                elif msg.error():
                    on_error("ERROR: %s".format(msg.error()))
                else:
                    # Extract the (optional) key and value, and callback.
                    on_message(msg.value())
        except KeyboardInterrupt:
            pass
        finally:
            # Leave group and commit final offsets
            consumer.close()

    @staticmethod
    def setup(config, group_id, topic):
        if config:
            config['group.id'] = group_id
        consumer = Consumer(config)
        consumer.subscribe([topic])
        return consumer
