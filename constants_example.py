# this file contains vehicle-specific information
# rename this to "constants.py" after cloning and change the parameters below

# time (in seconds) after ignition is switched off until the Pi executes a shutdown
SHUTDOWN_TIMER = 30.0

# pin which PTT relay is connected to
C2E_RELAY_PIN = 11

# path to the DBC file for this vehicle
DBC_FILE_PATH = "/home/pi/opendbc/honda.dbc"