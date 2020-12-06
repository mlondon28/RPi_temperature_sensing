import RPi.GPIO as GPIO
import dht11

def convert_c_to_f(degreesC):
	return degreesC * 1.8 + 32

def main():
	print("Starting main function") 
	#init GPIO
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()

	#read data using pin14
	instance = dht11.DHT11(pin = 14)
	result = instance.read()

	if result.is_valid():
		print("Temperature (C): %-3.1f C" % result.temperature)
		print("Temperature (F):	{}".format(convert_c_to_f(result.temperature)))
		print("Humidity: %-3.1f %%" % result.humidity)
	else:
		print("Error: %d" % result.error_code)

if __name__ == "__main__":
	main()
