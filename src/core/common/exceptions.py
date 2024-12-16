class KafkaPublishException(Exception):
    def __init__(self, topic: str, published_message: str, error_message: str) -> None:
        message = f'Error to send message {published_message} to topic {topic}, ERROR - {error_message}'
        self.topic = topic
        self.published_message = published_message
        self.error_message = error_message
        super().__init__(message)
