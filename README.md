# Sensor data alerts system

This is a small example of using kafka to persist incoming messages from a sensor through api requests.

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
