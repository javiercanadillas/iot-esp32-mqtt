from umqtt.simple import MQTTClient

config_file = "mqtt_config.json"

def get_mqtt_client_config(configfile):
    import ujson, os, sys
    try:
        os.stat(configfile)
        with open(configfile, 'r') as f:
            mqtt_data = ujson.load(f)
            print(mqtt_data)
            return(mqtt_data['mqtt_broker_ip'], mqtt_data['client_id'])
    except OSError:
        print("Cannot obtain config file")
        sys.exit()

def main(mqtt_broker_ip, client_id="umqtt_client"):
  c = MQTTClient(client_id, mqtt_broker_ip, port=1883, user=None, password=None, keepalive=30, ssl=False, ssl_params={})
  c.connect()
  c.publish(b"TEMPERATURE", b"Some Temperature")
  c.disconnect()

if __name__ == "__main__":
  mqtt_broker_ip, client_id = get_mqtt_client_config(config_file)
  main(mqtt_broker_ip, client_id)