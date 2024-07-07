import pika
import json
import os

# Get RabbitMQ host from environment variable, default to 'localhost' if not set
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')


def callback(ch, method, properties, body):
    # Deserialize the received message
    message = json.loads(body)
    # Log the received message
    print(f" [x] Received {message}")


def main():
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST))
    # Open a channel
    channel = connection.channel()
    # Declare a queue named 'test_queue'
    channel.queue_declare(queue='test_queue')

    # Set up a consumer on the 'test_queue' with the callback function
    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    # Log that the consumer is waiting for messages
    print(' [*] Waiting for messages. To exit press CTRL+C')
    # Start consuming messages
    channel.start_consuming()


if __name__ == "__main__":
    main()
