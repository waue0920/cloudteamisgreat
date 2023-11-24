import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS, help='Manage user [list|token]')
def cli():
    pass

@click.command(help='list ')
@click.option('-t', '--type', help='the type ', 
              required=True, type=click.Choice(['ds', 'org']))
@click.option('-d', '--detail', help='the detail', is_flag=True)
def list(type, detail):
    click.echo(filtered_list)


@click.command(help='show user\'s info')
def token():
    click.echo("hi")

cli.add_command(list)
cli.add_command(token)
