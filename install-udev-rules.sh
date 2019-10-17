#!/bin/bash

sudo cp 99-camera-udev.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger
