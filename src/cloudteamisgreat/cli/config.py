import click

    
# Context settings for CLI    
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help']) 

@click.group(context_settings=CONTEXT_SETTINGS, 
             help='Configure the CLI [info|init]')
def cli():
    pass

@click.command(help='Get exsisting information.')
def info():
    click.echo('Hi, your information:')
    print(info)


@click.command(help='Initialize the credential.')
@click.option('-a', '--apikey', help='API key for CLI.')
def init():
    click.echo('Credential Existed.')


cli.add_command(info)
cli.add_command(init)

