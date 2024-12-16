import os

APP_DEFAULT_LOG_LEVEL = os.getenv("APP_DEFAULT_LOG_LEVEL", "DEBUG")

WEB_SERVER_HOST = os.getenv("WEB_SERVER_HOST", "0.0.0.0")
WEB_SERVER_PORT = int(os.getenv("WEB_SERVER_PORT", "8080"))

KAFKA_BOOTSTRAP_SERVERS = os.environ.get("MSK_BOOTSTRAP_SERVERS", "localhost:9092")
SENSOR_DATA_TOPIC = os.environ.get("SENSOR_DATA_TOPIC", "sensor.data")
ALERT_TOPIC = os.environ.get("ALERT_TOPIC", "alert.data")