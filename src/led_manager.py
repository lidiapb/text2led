from bibliopixel.colors import COLORS
from bibliopixel import Strip
from bibliopixel.drivers.PiWS281X import PiWS281X

import json
import os, sys

class LedManager:
    ROWS = 18 
    COLS = 11
    NUM_PIXELS = ROWS*COLS
    DEFAULT_BRIGHTNESS = 100
    DEFAULT_COLOR = COLORS.blue

    with open('/home/pi/text2led/src/led_mapping.json') as json_file:
        MAPPING = json.load(json_file)
           
    def __init__(self, rows=ROWS, cols=COLS, brightness=DEFAULT_BRIGHTNESS):
        ROWS = rows 
        COLS = cols
        NUM_PIXELS = ROWS*COLS

        driver = PiWS281X(NUM_PIXELS)
        self.layout = Strip (driver, brightness=brightness,threadedUpdate=True)
        self.layout.cleanup_drivers()
        self.layout.start()

    def clear(self):
        self.layout.all_off()
        self.layout.push_to_driver()

    def set_led(self, led, color=DEFAULT_COLOR):
        self.layout.set(self.MAPPING[led], color)

    def send_to_leds(self):
        self.layout.push_to_driver()

    def draw_array(self, led_array):
        #Turn off all leds
        self.clear()

        for led in led_array:
            self.set_led(led)

        self.send_to_leds()


