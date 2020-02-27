import click
import socket

def main(port=1337):
	sock = socket.socket()
	sock.bind(('', port))
	sock.listen(1)
	conn, addr = sock.accept()
	
	print(f'connected:{addr}:{port}')
	
	
	while True:
		data = conn.recv(1024)
		if not data:
			break
		print(f'massage is: {data.decode()}')
	sock.close()

if __name__ == '__main__':
	main()
