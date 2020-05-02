#!/bin/bash

# run as ROOT (or with sudo)

# copy systemd service units
echo "copying systemd service units"
cp gpio-shutdown.service vehicle.service /etc/systemd/system/

# enable systemd service units
echo "enabling systemd service units"
systemctl enable gpio-shutdown
systemctl enable vehicle

echo "Done."
