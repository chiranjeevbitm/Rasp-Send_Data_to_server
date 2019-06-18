def coverage_plot(data,i):
	hum=data.split(",")[0]
	tem=data.split(",")[1]
	print 'temp='+(str(tem))+'iter='+str(i)
	plt.ion()
	fig=plt.figure(num=1,figsize=(6,6))
	plt.title(' IoT Temperature and Humidity Monitor') ax = fig.add_subplot(121)
	ax.plot(tem,i, c='r', marker=r'$\Theta$') 
	plt.xlabel('Temperature ($^\circ$C)')
	ax.grid()
	ax = fig.add_subplot(122) ax.plot(hum,i, c='b', marker=r'$\Phi$') plt.xlabel('Humidity ($\%$)')
	ax.grid()
	fig.show()
	fig.canvas.draw()
	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('10.14.3.194', 10001) sock.bind(server_address)

i=0
while True:
	data, address = sock.recvfrom(4096) 
	with open("DataLog.txt","a") as f:
		mess=str(data) 
		f.write(mess) 
		coverage_plot(mess,i) 
		print mess
		i+=1 
	f.close()