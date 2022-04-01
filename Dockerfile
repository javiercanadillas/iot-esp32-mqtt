FROM eclipse-mosquitto

COPY mosquitto/mosquitto.conf /mosquitto/config/

EXPOSE 1883
EXPOSE 9001
CMD ["mosquitto_sub", "-t", "foo_topic"]