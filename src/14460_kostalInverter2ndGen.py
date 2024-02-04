# coding: utf-8

import requests  # To not delete this module reference!!
import requests.auth
import json
from datetime import datetime

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class KostalInverter2ndGen14460(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "kostalInverter2ndGen14460")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE,())
        self.PIN_I_SWITCH=1
        self.PIN_I_FETCH_INTERVAL=2
        self.PIN_I_INVERTER_IP=3
        self.PIN_O_INVERTER_STATUS=1
        self.PIN_O_DC_ENERGY=2
        self.PIN_O_DC_AC_CONVERTED_ENERGY=3
        self.PIN_O_DAILY_YIELD=4
        self.PIN_O_TOTAL_YIELD=5
        self.PIN_O_L1_VOLTAGE=6
        self.PIN_O_L1_CURRENT=7
        self.PIN_O_L1_POWER=8
        self.PIN_O_L2_VOLTAGE=9
        self.PIN_O_L2_CURRENT=10
        self.PIN_O_L2_POWER=11
        self.PIN_O_L3_VOLTAGE=12
        self.PIN_O_L3_CURRENT=13
        self.PIN_O_L3_POWER=14
        self.PIN_O_GRID_FREQ=15
        self.PIN_O_DC1_VOLTAGE=16
        self.PIN_O_DC1_CURRENT=17
        self.PIN_O_DC1_POWER=18
        self.PIN_O_DC2_VOLTAGE=19
        self.PIN_O_DC2_CURRENT=20
        self.PIN_O_DC2_POWER=21
        self.PIN_O_DC3_VOLTAGE=22
        self.PIN_O_DC3_CURRENT=23
        self.PIN_O_DC3_POWER=24

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.DEBUG = self.FRAMEWORK.create_debug_section()
        self.interval = None

        self.registers = [
            {'output': self.PIN_O_INVERTER_STATUS, 'dxNum': 16780032, 'calc': None, 'name': 'Inverter Status', 'lastVal': 0},
            {'output': self.PIN_O_DC_ENERGY, 'dxNum': 33556736, 'calc': None, 'name': 'DC Power', 'lastVal': 0},
            {'output': self.PIN_O_DC_AC_CONVERTED_ENERGY, 'dxNum': 67109120, 'calc': None, 'name': 'DC-AC Power', 'lastVal': 0},
            {'output': self.PIN_O_DAILY_YIELD, 'dxNum': 251658754, 'calc': lambda x: x / 1000, 'name': 'Daily yield', 'lastVal': 0},
            {'output': self.PIN_O_TOTAL_YIELD, 'dxNum': 251658753, 'calc': None, 'name': 'Total yield', 'lastVal': 0},
            {'output': self.PIN_O_L1_VOLTAGE, 'dxNum': 67109378, 'calc': None, 'name': 'L1: voltage', 'lastVal': 0},
            {'output': self.PIN_O_L1_CURRENT, 'dxNum': 67109377, 'calc': None, 'name': 'L1: current', 'lastVal': 0},
            {'output': self.PIN_O_L1_POWER, 'dxNum': 67109379, 'calc': None, 'name': 'L1: power', 'lastVal': 0},
            {'output': self.PIN_O_L2_VOLTAGE, 'dxNum': 67109634, 'calc': None, 'name': 'L2: voltage', 'lastVal': 0},
            {'output': self.PIN_O_L2_CURRENT, 'dxNum': 67109633, 'calc': None, 'name': 'L2: current', 'lastVal': 0},
            {'output': self.PIN_O_L2_POWER, 'dxNum': 67109635, 'calc': None, 'name': 'L2: power', 'lastVal': 0},
            {'output': self.PIN_O_L3_VOLTAGE, 'dxNum': 67109890, 'calc': None, 'name': 'L3: voltage', 'lastVal': 0},
            {'output': self.PIN_O_L3_CURRENT, 'dxNum': 67109889, 'calc': None, 'name': 'L3: current', 'lastVal': 0},
            {'output': self.PIN_O_L3_POWER, 'dxNum': 67109891, 'calc': None, 'name': 'L3: power', 'lastVal': 0},
            {'output': self.PIN_O_GRID_FREQ, 'dxNum': 67110400, 'calc': None, 'name': 'grid frequency', 'lastVal': 0},
            {'output': self.PIN_O_DC1_VOLTAGE, 'dxNum': 33555202, 'calc': None, 'name': 'DC1: voltage', 'lastVal': 0},
            {'output': self.PIN_O_DC1_CURRENT, 'dxNum': 33555201, 'calc': None, 'name': 'DC1: current', 'lastVal': 0},
            {'output': self.PIN_O_DC1_POWER, 'dxNum': 33555203, 'calc': None, 'name': 'DC1: power', 'lastVal': 0},
            {'output': self.PIN_O_DC2_VOLTAGE, 'dxNum': 33555458, 'calc': None, 'name': 'DC2: voltage', 'lastVal': 0},
            {'output': self.PIN_O_DC2_CURRENT, 'dxNum': 33555457, 'calc': None, 'name': 'DC2: current', 'lastVal': 0},
            {'output': self.PIN_O_DC2_POWER, 'dxNum': 33555459, 'calc': None, 'name': 'DC2: power', 'lastVal': 0},
            {'output': self.PIN_O_DC3_VOLTAGE, 'dxNum': 33555714, 'calc': None, 'name': 'DC3: voltage', 'lastVal': 0},
            {'output': self.PIN_O_DC3_CURRENT, 'dxNum': 33555713, 'calc': None, 'name': 'DC3: current', 'lastVal': 0},
            {'output': self.PIN_O_DC3_POWER, 'dxNum': 33555715, 'calc': None, 'name': 'DC3: power', 'lastVal': 0}
            # Before enabling this please consider the value limit of 25 values per request.
            # Idea of optimization then: Calculate the power values of DC the LBS instead of requesting them
            # {'output': self.PIN_O_HOME_POWER_PV, 'dxNum': 83886336, 'calc': lambda x: x if x else 0, 'name': 'Actual home consumption PV', 'lastVal': 0},
            # {'output': self.PIN_O_HOME_POWER_GRID, 'dxNum': 83886848, 'calc': lambda x: x if x else 0, 'name': 'Actual home consumption grid', 'lastVal': 0},
            # {'output': self.PIN_O_HOME_ENERGY_TODAY, 'dxNum': 251659266, 'calc': lambda x: x if x else 0, 'name': 'todays home energy consumption', 'lastVal': 0},
            # {'output': self.PIN_O_HOME_ENERGY_TOTAL, 'dxNum': 251659009, 'calc': lambda x: x if x else 0, 'name': 'total home energy consumption', 'lastVal': 0}
        ]

    def on_init(self):
        self.interval = self.FRAMEWORK.create_interval()
        self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
        if bool(self._get_input_value(self.PIN_I_SWITCH)):
            self.interval.start()

    def on_input_value(self, index, value):
        if index == self.PIN_I_SWITCH:
            if bool(value):
                self.interval.start()
            else:
                self.interval.stop()
        elif index == self.PIN_I_FETCH_INTERVAL:
            self.interval.stop()
            self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
            if bool(self._get_input_value(self.PIN_I_SWITCH)):
                self.interval.start()

    ####

    def on_interval(self):
        ip_address = str(self._get_input_value(self.PIN_I_INVERTER_IP))
        url = "http://{0}/api/dxs.json".format(ip_address)
        get_params = "&".join(map(lambda x: "dxsEntries=" + str(x['dxNum']), self.registers))
        request_url = url + '?' + get_params

        try:
            response = requests.request("GET", request_url, headers={'Connection': 'close'})
        except Exception as exception:
            act_time = datetime.now()
            self.DEBUG.set_value("ConnErr", str(act_time) + ": " + str(exception))
            return None

        if response.status_code == 200:
            jsonbody = json.loads(response.text)
            entries = jsonbody['dxsEntries']
            map(self.set_response_to_outputs, entries)
            self.DEBUG.set_value("ConnErr", "")
        else:
            self.DEBUG.set_value("ConnErr", "Received HTTP status: " + str(response.status_code))

    def set_response_to_outputs(self, entry):
        output_entry = next(iter(filter(lambda x: x['dxNum'] == entry['dxsId'], self.registers)), None)

        if output_entry['calc']:
            value = output_entry['calc'](entry['value'])
        else:
            value = entry['value']
        if value != output_entry['lastVal'] and self._can_set_output():  # Send by change check
            self._set_output_value(output_entry['output'], value)
            self.DEBUG.set_value(output_entry['name'], value)
            output_entry['lastVal'] = value
