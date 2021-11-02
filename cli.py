import pyfiglet
import click

result = pyfiglet.figlet_format("Password Vault")
print(result)

import click

@click.command()
def hello():
    click.echo('Hello there')


if __name__ == '__main__':
    hello()