import click
import socket

@click.command()
@click.option('-ip',
              '--ip',
              default='192.168.1.35',
              )
@click.option(
             '-p',
             '--p',
             default='1337'
             )
def main(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 1337))

    while True:
	m = input()
	sock.send(m.encode())
	sock.close()
        if not m:
            break;

if __name__ == '__main__':
    main()
