import pika
import time
import uuid
import json
from datetime import datetime
import os

# Get RabbitMQ host from environment variable, default to 'localhost' if not set
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
# Get message interval from environment variable, default to 5 seconds if not set
MESSAGE_INTERVAL = int(os.getenv('MESSAGE_INTERVAL', 5))


def main():
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST))
    # Open a channel
    channel = connection.channel()
    # Declare a queue named 'test_queue'
    channel.queue_declare(queue='test_queue')

    while True:
        # Create a message with a unique UUID and the current timestamp
        message = {
            "message_id": str(uuid.uuid4()),
            "created_on": datetime.now().isoformat()
        }
        # Publish the message to the 'test_queue'
        channel.basic_publish(exchange='', routing_key='test_queue', body=json.dumps(message))
        # Log the sent message
        print(f" [x] Sent {message}")
        # Wait for the specified interval before sending the next message
        time.sleep(MESSAGE_INTERVAL)


if __name__ == "__main__":
    main()
