class KafkaPublishException(Exception):
    """
    Custom exception raised when an error occurs while publishing a message to a Kafka topic.

    This exception is designed to provide detailed information about the failure of
    a message publication, including the topic, the message that was attempted to be
    published, and the associated error message from Kafka.
    """
    def __init__(self, topic: str, published_message: str, error_message: str) -> None:
        message = f'Error to send message {published_message} to topic {topic}, ERROR - {error_message}'
        self.topic = topic
        self.published_message = published_message
        self.error_message = error_message
        super().__init__(message)
