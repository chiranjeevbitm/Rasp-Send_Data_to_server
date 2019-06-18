def sensordata():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	sensor = Adafruit_DHT.AM2302
	humidity, temperature = Adafruit_DHT.read_retry(sensor,17)
	return(humidity, temperature)

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create UDP socket server_address = ('10.14.3.194', 10001)
	try:
		while (1):
			h,t = sensordata()
			message = str(h)+','+str(t)						#Send Data
			print >>sys.stderr, 'sending "%s"' % message sent = sock.sendto(message, server_address)
	finally:
		print >>sys.stderr, 'closing socket' sock.close()

