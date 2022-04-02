## Setting up the environment

Create a new Python virtual environment. Once done, install dependencies:
```bash
pip install -r requirements.txt
```

Then, check your ESP32 usb port, update your `env.sh` file accordingly, and source it:
```bash
source env.sh
```

Copy the `credentials-sample.json` file into `src/credentials.json` and edit this last file to match the SSID and password of the WiFi where both your ESP32 and the computer hosting the Mosquitto container will be connecting to.

```bash
cp ./credentials-sample.json src/credentials.json
vi src/credentials.json
```

## Installing Mosquitto MQTT Broker

We'll install Mosquitto MQTT Broker for this test using the official Docker image.

```bash
docker pull eclipse-mosquitto
```

Then, spin up a new container using the image you just downloaded:

```bash
docker run -d  --name mqtt -p 1883:1883 -p 9001:9001 -v "$(pwd)/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf" eclipse-mosquitto
```

And finally, enter the container and create a new topic in Mosquitto MQTT to test our client code:

```bash
docker exec -it mqtt /bin/sh
mosquitto_sub -t TEMPERATURE
```

The file `Mosquitto.conf` we've just mounted into our container should be like this:

```text
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
allow_anonymous true
connection_messages true
log_type all
listener 1883
```

## Creating a Micropython MQTT client

Open the file `src/mqtt_config.json` and put there your computer IP. This is the IP of the MQTT server, the one you're device will be connecting to.

Now, connect your device to your PC and copy with `ampy` the files under `src/` to your device:

```bash
for f in "$(ls src/)"do; ampy put "src/$f"; done
```

- `boot.py` contains the logic to connect your ESP32 to the WiFi network.
- `credentials.json` contains the SSID and password for your WLAN
- `main.py` contains the main program to execute that implements a MicroPython MQTT cient.

## Going further

Now, modify the code so you can send the data from your SHTx sensor. Use the `SHT31.py` library that's in the `src` folder.

You're now one step closer to connecting your device to the Cloud!

## Links
- [Eclipse Mosquitto Project page](https://mosquitto.org)
- [HiveMQ Community Edition](https://github.com/hivemq/hivemq-community-edition)
- [Eclipse Mosquitto Official Docker image](https://hub.docker.com/_/eclipse-mosquitto/)
- [Micropython MQTT Simple module documentation](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple)
