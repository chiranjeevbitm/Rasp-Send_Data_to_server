## Remote Data Logging
	 Overview:
	 1.A network of Temperature and humidity sensor connected with Raspberry Pi
	 2.Read data from the sensor
	 3.Send it to a Server
	 4.Save the data in the server and Plot the data



## 1.A network of Temperature and humidity sensor connected with Raspberry Pi
`		
 	Requirements
	`	DHT Sensor
		4.7K ohm resistor 
		Jumper wires
		Raspberry Pi 
			

## 2.Read data from the sensor
Used the Adafruit library for DHT22 sensor to read the sensor data
main.py (python program which reads the Temperature and humidity from sensor)
for more goto-
https://github.com/chiranjeevbitm/IOT-project-Temperature-Dependent-Auto-Cooling-System-

## 3.Sending Data to a Server
    Steps---

          Sending data to server using socket programming 
          Create a client and server 
          Establish connection between the two
          Send data from the client to the server
          Save the data in a file

         Here we write python program for the client and server
         Here I have used raspian OS on Raspberry pi as the client side and 
         My own laptop as the server(program is being ran on anaconda)
         As I run the Iot_client.py on the raspberry pi it starts sending the data to the server(Laptop in my case)

## 4.Save the data in the server and Plot the data

	 	  From the server side(on Laptop)
	 	  Run the program Iot_server.py which contains functions For plotting the real time data by matplotlib and save these data in Datalog.txt


Server address and port address might change according to uses.
    
  For learning How to configure Client and Server read--

   1.https://pymotw.com/2/socket/udp.html

   2.https://tutorialedge.net/python/udp-client-server-python/






