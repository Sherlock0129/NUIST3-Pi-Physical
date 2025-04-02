# NUIST in Python
# Author: Dongxu Xia
# Date: 2025/3/31
# Description: A simple program to control an LED using Raspberry Pi GPIO

# Import required libraries
import RPi.GPIO as GPIO  # Library for GPIO control
import time               # Library for time-related functions

# Set GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Turn LED on
print("LED on")
GPIO.output(18, GPIO.HIGH)  # Set pin 18 to HIGH (3.3V) to turn on LED
time.sleep(1)               # Wait for 1 second

# Turn LED off
print("LED off")
GPIO.output(18, GPIO.LOW)   # Set pin 18 to LOW (0V) to turn off LED
