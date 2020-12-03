import RPi.GPIO as GPIO
import dht11

print(__name__)
def main():
	#init GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()

	#read data using pin14
	#TODO: make pin number a cmd line arg
	instance = dht11.DHT11(pin = 14)
	result = instance.read()

	if result.is_valid():
		print("Temperature: %-3.1f C" % result.temperature)
		print("Humidity: %-3.1f %%" % result.humidity)
	else:
		print("Error: %d" % result.error_code)

if __name__ == "__main_":
	main()
