import esp_utils as utils
from odoo_data import odoo_config
from odoo_functions import call
import gc
# Connect to wifi
utils.do_connect()
# Urequests installation in case not done
utils.check_and_install_urequests()
# Get user id for use from now on
odoo_config['uid'] = call(odoo_config.get('url'), "common", "login", 
    odoo_config.get('database'), odoo_config.get('user'), odoo_config.get('password'))

# Get hr user id for check in and out
odoo_config['hr_id'] = call(odoo_config.get('url'), "object", "execute", 
    odoo_config.get('database'), odoo_config.get('uid'), odoo_config.get('password'),
    'hr.employee', 'search_read', [['user_id', '=', odoo_config.get('uid')]], ['id'])[0]['id']
# Get hw mng
from machine import Pin, Timer

# Check if hr_id is checked in or out and update color
def check_and_update(config):
    gc.collect()
    state = call(config.get('url'), "object", "execute", config.get('database'), 
        config.get('uid'), config.get('password'), 'hr.employee', 'search_read', 
        [['id', '=', config.get('hr_id')]],['attendance_state'])[0]['attendance_state']
    if state == 'checked_out':
        # Red when checked out
        Pin(3, Pin.OUT).on()
        Pin(4).off()
    else:
        # Green when checked in
        Pin(3).off()
        Pin(4, Pin.OUT).on()
        
# Just check in or out
def check_in_out(config):
    call(config.get('url'), "object", "execute", 
        config.get('database'), config.get('uid'), config.get('password'), 'hr.employee', 'attendance_manual', 
        [config.get('hr_id')],['hr_attendance.hr_attendance_action_my_attendances'])

# Debounce because crappy button
def debounce(pin):
    # Start or replace a timer for 200ms, and trigger on_pressed.
    tim2.init(mode=Timer.ONE_SHOT, period=200, callback=lambda t:check_in_out(odoo_config))

# Fist timer for checking if checked_out
tim0 = Timer(0)
tim0.init(period=1500, mode=Timer.PERIODIC, callback=lambda t:check_and_update(odoo_config))

# Timer 2, because timer 1 broke or something, and don't work
tim2 = Timer(2)
# Setup the button input pin with a pull-up resistor.
# Register an interrupt on falling button input.
# 7 Because
Pin(7, Pin.IN, Pin.PULL_UP).irq(debounce, Pin.IRQ_FALLING)


