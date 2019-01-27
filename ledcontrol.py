"""
XMas Tree Control for the PiHut GPIO XMas tree.
    Copyright (C) 2019 Aubrey Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero.tools import random_values
from signal import pause
from random import randrange


class LedControl:

    def __init__(self):
        self.tree = None

    def generator(self):
        precision = 0.1
        f = 1 / precision
        while True:
            yield float(randrange(0*f, 1*f, 0.1*f)/f)

    def ledchange(self, led, random, delay, value):
        self.tree = LEDBoard(*range(2, 28), pwm=True)
        print(random)
        print(led)
        print(value)
        print(delay)
        if led in "All":
            print("board")
            if random:
                self.control_board(value, delay, random=1)
                print("Board random")
            else:
                self.control_board(value, delay)
                print("Board")
        else:
            if random:
                self.control_led(int(led) + 1, delay=delay, random=1)
                print("Random")
            else:
                self.control_led(int(led) + 1, value, delay)
                print("Pass")

    def control_led(self, led, value=0, delay=0.1, random=0):
        led = self.tree[led]
        if not random:
            led.source_delay = float(delay)
            led.value = float(value)
        else:
            led.source_delay = float(delay)
            led.source = self.generator()
        pause()

    def control_board(self, value=0, delay=0.1, random=0):
        if not random:
            for led in self.tree:
                led.source_delay = float(delay)
                led.value = float(value)
        else:
            for led in self.tree:
                led.source_delay = 0.1
                led.source = self.generator()
        pause()

