# data_simulation/sensor_simulator.py

import random

def simulate_sensor_data():
    vibration = random.uniform(0.0, 1.5)
    seismic = random.uniform(0.0, 1.5)
    intrusion_detected = vibration > 1.0 or seismic > 1.0

    return {
        'vibration': round(vibration, 2),
        'seismic': round(seismic, 2),
        'intrusion_detected': intrusion_detected
    }
