# RabbitMQ Test Task

## Overview
This project demonstrates a simple RabbitMQ setup with a producer and consumer using Python and Docker.

## Requirements
- Docker
- Docker Compose

## Setup and Running

1. Clone the repository:
    ```sh
    git clone git@github.com:wasxxm/RabbitMQTest.git
    cd RabbitMQTest
    ```

2. Build and start the services using Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. The producer will send a message every 5 seconds, and the consumer will log each received message.

## Viewing Logs

After running the Docker Compose command, you can see the logs from both the producer and consumer directly in your terminal. The producer logs when it sends a message, and the consumer logs when it receives a message.

Example log output:

producer_1 | [x] Sent {'message_id': '123e4567-e89b-12d3-a456-426614174000', 'created_on': '2024-07-08T12:34:56.789Z'}

consumer_1 | [x] Received {'message_id': '123e4567-e89b-12d3-a456-426614174000', 'created_on': '2024-07-08T12:34:56.789Z'}


## Accessing RabbitMQ Management UI

You can also view the messages and the status of the queues using the RabbitMQ Management UI:

1. Open your web browser and go to `http://localhost:15672`.
2. Log in using the default credentials:
   - Username: `guest`
   - Password: `guest`
3. Navigate to the `Queues` tab to see the `test_queue`.
4. Click on `test_queue` to see details about the queue, including the number of messages and their content.

## Configuration
- You can change the message interval by setting the `MESSAGE_INTERVAL` environment variable in the `docker-compose.yml` file.

## Running Docker Compose in Detached Mode

If you prefer to run Docker Compose in detached mode (in the background), use the following command:
```sh
docker-compose up -d --build

