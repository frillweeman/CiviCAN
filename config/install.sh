#!/bin/bash

# run as ROOT (or with sudo)

# prompt user for new hostname
read -p "Would you like to change the hostname? [Y/n] " yn
case $yn in
    [Yy]* )
	read -p "New hostname: " NEWHOST
        ;;
esac

# Message of the Day (displays at login)
cp motd /etc/

# basic setup
raspi-config nonint do_expand_rootfs     # expand FS
raspi-config nonint do_boot_behaviour B2 # autologin command line
raspi-config nonint do_boot_wait 1       # don't wait for network on boot
raspi-config nonint do_ssh 0             # enable SSH


# apt dependencies
apt install -y git pipenv

# copy systemd service units
echo "copying systemd service units"
cp gpio-shutdown.service vehicle.service /etc/systemd/system/

# enable systemd service units
echo "enabling systemd service units"
systemctl enable gpio-shutdown
systemctl enable vehicle

# copy udev rules
echo "copying udev rules"
cp vehicle.rules /etc/udev/rules.d/

# reload udev rules
echo "reloading udev rules"
udevadm control --reload-rules
udevadm trigger

# change hostname
if [[ $NEWHOST ]]; then
	raspi-config nonint do_hostname $NEWHOST
fi

echo "Done. Press any key to restart."

read
reboot
