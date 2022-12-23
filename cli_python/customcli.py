import click

@click.command()
@click.option("--name",prompt="Enter your name: ",help="Enter The name of user")
def customcli(name):
    click.echo(f"Hello {name}")

if __name__=="__main__":
    customcli()