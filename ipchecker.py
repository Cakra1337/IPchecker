import ipaddress
import socket

print('----- Python IP Checker -----')
def main():
	print('1.Check My Local IP')
	print('2.Coming soon.')
	choose = input('Choose : ')
	if(choose == '1'):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		localIP = s.getsockname()[0]
		print('----local IP : ',localIP)
		print('----IP Version : ',ipaddress.ip_address(localIP).version)
		s.close()

	else:
		print('Coming soon.')
		main()

main()
