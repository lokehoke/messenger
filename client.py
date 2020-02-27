import click
import socket

@click.command()
@click.option('--ip',
			  default='192.168.1.35',
			  help='ip for connecting',
			  )
def main(ip):
	sock = socket.socket()
	sock.connect((ip, 1337))
	m = 'a'
	while m:
		m = input()
		sock.send(m.encode())
	sock.close()

if __name__ == '__main__':
	main()
