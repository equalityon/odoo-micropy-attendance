# Personal attendance management on Odoo ERP using an ESP-C3-32S :raccoon:
![ESP Board](/assets/micro_odoo.png?raw=true)

**Set of Micropython scripts to check attendance state and the possibility to checking in or checking out**

# Setup of the program
## Customizing files

After downloading the repo, the first thing you must do is to configure the parameters to connecting to you Odoo database, this are located on the **odoo_data.py** file

    odoo_config = {
    # The jsonrpc must be available
    'url': 'https://URL_OF_YOUR_ODOO_WEB.org' + '/jsonrpc',
    'database': 'database_to_connect',
    'user': 'mail_of_the_user',
    'password': 'user_password',
    'uid': -1, # Calculated with user and password
    'hr_id': -1, # Calculated with UID
    }

For working it must have an internet connection, so ensure that you fille the **wifi_networks.py** file

    networks_availables = {
    'NET1': 'PASSWORD_OF_NET_1',
    'NET2': 'PASSWORD_OF_NET_2',
    # ... Every net you want
    }

On **att_check.py** file you can find the basic configuration for using the On board led (Pin3 -> Red; Pin4 -> Green; Pin5 -> Blue) and a button connected to the PIN 7 (For no particular reason) which will be used to check In and Out.

## Copying files

Connect the ESP module with an USB cable and use ampy (Or any other program you like) to copy the files.

    # Asuming ttyUSB0 as you esp controller
    ampy -p /dev/ttyUSB0 put att_check.py
    ampy -p /dev/ttyUSB0 put esp_utils.py
    ampy -p /dev/ttyUSB0 put odoo_data.py
    ampy -p /dev/ttyUSB0 put odoo_functions.py
    ampy -p /dev/ttyUSB0 put wifi_networks.py
    ampy -p /dev/ttyUSB0 put boot.py

## Final results

If everything is done correctly, after a board reset now the script **boot.py** will start running and you will be ale to see the status of the attendance of the configured user.

### Checked OUT

A red color will be displayed

### Checked IN
 
A green color will be displayed

