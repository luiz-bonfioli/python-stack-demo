# Sensor data alerts system

This is a small example of using kafka to persist and process incoming messages from a sensor through api requests.

## Features

- API to send sensor data
- API to get sensor data alerts
- Streaming of sensor data, kafka producer and consumer

## Requirements

- Python 3.11
- Poetry (for dependency management)

## Installation

To get started with this project, you'll need to have [Poetry](https://python-poetry.org/) installed. If you don't have Poetry installed yet, you can install it by following these steps:

### Install Poetry

You can install Poetry using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -

### Install Dependencies

```bash
poetry install

### Install infra (kafka)

```bash
docker-compose up -d


### Running API
```bash
python --file api_handler.py

### Running Kafka Handler
```bash
python --file kafka_handler.py 

### Sending sensor data

```bash
curl --location 'http://localhost:8080/v1/sensors/c0d14d33-689c-4490-975a-6ae7128f54a9' \
--header 'x-user-id: luiz.bonfioli' \
--header 'Content-Type: application/json' \
--data '{
    "data": 123.577
}'

### Getting alerts

```bash
curl --location 'http://localhost:8080/v1/alerts/c0d14d33-689c-4490-975a-6ae7128f54a9' \
--header 'x-user-id: luiz' \
--data ''
