from paho.mqtt import client as mqtt_client
import secrets as sc
import random

server = sc.SERVER
port = sc.PORT
topic = sc.TOPIC
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = sc.USER
password = sc.PASS


def connect_mqtt() -> mqtt_client:

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Server!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(server, port)
    return client


def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        response = msg.payload.decode()

        with open(f'{sc.PATH}/response.JSON', 'w') as file:
            file.write(response)
        print(f"Received!")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()