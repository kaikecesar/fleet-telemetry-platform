import random
import time

from utils.helpers import (
    random_choice,
    random_float,
)


class Vehicle:
    def __init__(self, device_eui):
        self.device_eui = device_eui

    def __generate_data():
        data = {
            'device_id': str(random.randint),
            'timestamp': time.time(),
            'location': {
                'lat': random_float(-90, 90, 6),  # TODO - Create a function
                'lng': random_float(-180, 180, 6),  # TODO - Create a function
            },
            'speed': random_float(),
            'engine': {
                'temperature': random_float(),
                'status': 'on',
                'alarm_status': 'ok',
            },
            'fuel_level': random_float(),  # TODO - percent
            'tire_pressure': {
                'front_left': random_float(),
                'front_right': random_float(),
                'rear_left': random_float(),
                'rear_right': random_float(),
            },
            'oil_level': random_float(),
            'battery_level': random_float(),
            'security_belts': {
                'seat_1': True,
                'seat_2': True,
                'seat_3': False
            },
            'brake_status': 'normal',
        }


class FleetSimulator:
    def __init__(self):
        pass