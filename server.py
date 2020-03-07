import click
import socket

@click.command()
@click.option('-p',
              '--port',
              default='1337',
              )
def main(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
        sock.listen()

	while True:
            conn, addr = sock.accept()
            print(f'connected:{addr}:{port}')
            data = conn.recv(1024)
            if not data:
                break
            print(f'massage is: {data.decode()}')

        sock.close()

if __name__ == '__main__':
	main()
