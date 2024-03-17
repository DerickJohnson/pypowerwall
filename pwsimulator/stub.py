# pyPowerWall Module - Proxy Server Tool
# -*- coding: utf-8 -*-
"""
 Python module to interface with Tesla Solar Powerwall Gateway

 Author: Jason A. Cox
 For more information see https://github.com/jasonacox/pypowerwall

 Powerwall Simulator Stub Tool
    This tool will emulate the Powerwall API calls for testing purposes. 
    Handlers are created for these API endpoints:
    /api/login/Basic
    /api/status
    /api/meters/aggregates 
    /api/system_status/soe 
    /api/devices/vitals - Returns 404: Firmware 23.44.0+ does not support

 TLS Note: This uses a self-signed https certificate generated by this:
 openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 3650 -nodes

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import json

# Create Simulator
server_address = ('0.0.0.0', 443)
print('pyPowerwall - Powerwall Simulator - Running')

class handler(BaseHTTPRequestHandler):
    # POST Handler
    def do_POST(self):
        message = "ERROR!"
        valid = False
        # Login
        if self.path == '/api/login/Basic':
            valid = True
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('set-cookie', 'AuthCookie=1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer==; Path=/')
            self.send_header('set-cookie', 'UserRecord=1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer123456==; Path=/')
            self.end_headers()
            message = '{"email":"test@example.com","firstname":"Tesla","lastname":"Energy","roles":["Home_Owner"],"token":"1234567890qwertyuiopasdfghjklZXcvbnm1234567890Qwertyuiopasdfghjklzxcvbnm1234567890qwer==","provider":"Basic","loginTime":"2021-10-17T00:39:09.852064316-07:00"}'              
            # TODO: Add check for right login credentials or send 401
            # self.send_response(401)
            # self.send_header('Content-type','application/json')
            # message = '{"code":401,"error":"bad credentials","message":"Login Error"}'
        #
        # Error 
        if (not valid):
            self.send_response(403)
            self.send_header('Content-type','application/json')
            self.end_headers()
            message = '{"code":403,"error":"Unable to GET to resource","message":"User does not have adequate access rights"}'

        # Send Response
        self.wfile.write(bytes(message, "utf8"))

    # GET Handler
    def do_GET(self):
        message = "ERROR!"
        valid = False
        # Handlers
        #
        # Status - SOE
        if self.path == '/api/status':
            valid = False
            if('cookie' in self.headers and '1234567890qwertyuiopasdfghjklZXcvbnm' in self.headers['cookie']):
                # Valid Login
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                payload = {'din': '1232100-00-E--TG123456789ABC', 'start_time': '2024-03-11 09:12:41 +0800', 'up_time_seconds': '127h34m16.275122187s', 'is_new': False, 'version': '23.44.0 9064fc6a', 'git_hash': '4064fc6a5b32425509f91f19556f2431cb7f6872', 'commission_count': 0, 'device_type': 'teg', 'teg_type': 'unknown', 'sync_type': 'v2.1', 'cellular_disabled': False, 'can_reboot': True}
                # convert payload to json
                message = json.dumps(payload)
                valid = True
        #
        # Meters - Aggregates
        elif self.path == '/api/meters/aggregates':
            valid = False
            if('cookie' in self.headers and '1234567890qwertyuiopasdfghjklZXcvbnm' in self.headers['cookie']):
                # Valid Login
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                message = '{"site":{"last_communication_time":"2021-10-17T07:23:34.290637169-07:00","instant_power":1345,"instant_reactive_power":-439,"instant_apparent_power":1414.830731925201,"frequency":0,"energy_exported":687.6503234502925,"energy_imported":887602.0847810425,"instant_average_voltage":210.20168600655896,"instant_average_current":12.47,"i_a_current":0,"i_b_current":0,"i_c_current":0,"last_phase_voltage_communication_time":"0001-01-01T00:00:00Z","last_phase_power_communication_time":"0001-01-01T00:00:00Z","timeout":1500000000,"num_meters_aggregated":1,"instant_total_current":12.47},"battery":{"last_communication_time":"2021-10-17T07:23:34.289652105-07:00","instant_power":-60,"instant_reactive_power":330,"instant_apparent_power":335.4101966249685,"frequency":60.019999999999996,"energy_exported":136540,"energy_imported":161080,"instant_average_voltage":242.95,"instant_average_current":0.6000000000000001,"i_a_current":0,"i_b_current":0,"i_c_current":0,"last_phase_voltage_communication_time":"0001-01-01T00:00:00Z","last_phase_power_communication_time":"0001-01-01T00:00:00Z","timeout":1500000000,"num_meters_aggregated":2,"instant_total_current":0.6000000000000001},"load":{"last_communication_time":"2021-10-17T07:23:34.289652105-07:00","instant_power":1540.5,"instant_reactive_power":-131,"instant_apparent_power":1546.0599115170148,"frequency":0,"energy_exported":0,"energy_imported":1120094.4344575922,"instant_average_voltage":210.20168600655896,"instant_average_current":7.328675755492901,"i_a_current":0,"i_b_current":0,"i_c_current":0,"last_phase_voltage_communication_time":"0001-01-01T00:00:00Z","last_phase_power_communication_time":"0001-01-01T00:00:00Z","timeout":1500000000,"instant_total_current":7.328675755492901},"solar":{"last_communication_time":"2021-10-17T07:23:34.290245943-07:00","instant_power":240,"instant_reactive_power":-20,"instant_apparent_power":240.8318915758459,"frequency":60.012,"energy_exported":257720,"energy_imported":0,"instant_average_voltage":242.4,"instant_average_current":0.9488448844884488,"i_a_current":0,"i_b_current":0,"i_c_current":0,"last_phase_voltage_communication_time":"0001-01-01T00:00:00Z","last_phase_power_communication_time":"0001-01-01T00:00:00Z","timeout":1000000000,"num_meters_aggregated":1,"instant_total_current":0.9488448844884488}}'
                valid = True
        #
        # Battery - SOE
        elif self.path == '/api/system_status/soe':
            valid = False
            if('cookie' in self.headers and '1234567890qwertyuiopasdfghjklZXcvbnm' in self.headers['cookie']):
                # Valid Login
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                message = '{"percentage":23.975388097174584}'
                valid = True
        #
        # Vitals - Firmware 23.44.0+ does not support this API
        elif self.path == '/api/devices/vitals':
            valid = False
            if('cookie' in self.headers and '1234567890qwertyuiopasdfghjklZXcvbnm' in self.headers['cookie']):
                # Valid Login
                self.send_response(404)
                self.send_header('Content-type','application/json')
                self.end_headers()
                message = '{"code":404,"error":"File Not Found","message":"Firmware does not support vitals API"}'
                valid = True
        # 
        # Simulator doesn't support API Requested
        else:
            valid = False
            if('cookie' in self.headers and '1234567890qwertyuiopasdfghjklZXcvbnm' in self.headers['cookie']):
                # Valid Login
                print("Simulator doesn't support API Requested: " + self.path)
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                message = None
                valid = True
        #
        # Error 
        if (not valid):
            print(self.headers['cookie'])
            self.send_response(403)
            self.send_header('Content-type','application/json')
            self.end_headers()
            message = '{"code":403,"error":"Unable to GET to resource","message":"User does not have adequate access rights"}'
            print(message)
        #
        # Send Response
        self.wfile.write(bytes(message, "utf8"))

try:
    with HTTPServer(server_address, handler) as server:
        server.socket = ssl.wrap_socket(server.socket,
                               server_side=True,
                               certfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
        server.serve_forever()
except:
    print(' CANCEL \n')


