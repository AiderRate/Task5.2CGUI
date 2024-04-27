import tkinter as tk
import RPi.GPIO as GPIO

# Define LED GPIO pins
RED_PIN = 18
GREEN_PIN = 12
BLUE_PIN = 17

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Setup PWM for LEDs
red_pwm = GPIO.PWM(RED_PIN, 100)  # Frequency: 100 Hz
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# Function to turn off all LEDs
def turn_off_all():
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()

# Function to set intensity of LED
def set_led_intensity(led_pwm, intensity):
    if intensity == 0:
        led_pwm.stop()
    else:
        led_pwm.start(intensity)

# Create GUI
def create_gui():
    root = tk.Tk()
    root.title("LED Intensity Control")

    # Function to handle slider movement
    def on_slider_move(led_pwm, value):
        set_led_intensity(led_pwm, value)

    # Create sliders for each LED
    red_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Red", command=lambda value: on_slider_move(red_pwm, int(value)))
    red_slider.pack()
    
    green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Green", command=lambda value: on_slider_move(green_pwm, int(value)))
    green_slider.pack()
    
    blue_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Blue", command=lambda value: on_slider_move(blue_pwm, int(value)))
    blue_slider.pack()

    # Create exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()
    root.mainloop()

if __name__ == "__main__":
    create_gui()
