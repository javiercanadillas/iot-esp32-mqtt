#!/bin/false
# Make shellcheck shut up about /bin/false
# shellcheck shell=bash disable=SC1008

# Set the latest Micropython ESP32 firmware URL
export MICROPYTHON_URL="https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin"

# Enter here the right port, which is device-dependent
# Mac OS X example: /dev/cu.usbserial-02J1JMFH
SERIALPORT=/dev/cu.usbserial-0001

# Exports different USB serial communication program startup options
export MINICOM="-D ${SERIALPORT}"
export ESPTOOL_PORT="${SERIALPORT}"
export AMPY_PORT="${SERIALPORT}"
export RSHELL_PORT="${SERIALPORT}"