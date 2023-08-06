from zipfile import ZipFile

import click

from agileupstate.ansible import ping_windows, create_windows_inventory, create_linux_inventory
from agileupstate.client import get_version_string, Client
from agileupstate.terminal import print_check_message, print_cross_message
from agileupstate.vault import address, is_ready, create_state, load_state, create_tfstate, load_tfstate, \
    load_vault_file

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(help='CLI to manage pipeline states.')
def cli() -> int:
    pass


@cli.command(help='Display the current version.')
def version() -> None:
    click.echo(get_version_string())


@cli.command(help='Check client configuration.')
def check() -> None:
    click.secho('Checking client configuration', fg='green')
    if is_ready():
        print_check_message('Vault backend is available')
        Client()
    else:
        print_cross_message(f'Vault backend failed from: {address()}', leave=True)


@cli.command(help='Create vault states.')
def create() -> None:
    click.secho('- Create vault states', fg='green')
    create_state()


@cli.command(help='Save tfstates to vault.')
def save() -> None:
    click.secho('- Save tfstates to vault', fg='green')
    state = load_state()
    tfstate_content = state.read_tfstate()
    create_tfstate(state, tfstate_content)


@cli.command(help='Load states from vault.')
def load() -> None:
    click.secho('- Load states from vault', fg='green')
    state = load_state()
    tfstate_content = load_tfstate()
    state.write_tfstate(tfstate_content)


@cli.command(help='Generate cloud init zip file for mTLS data.')
@click.option('--server-path', required=True, help='Vault path to windows WinRM server pfx file.')
@click.option('--client-path', required=True, help='Vault path to windows WinRM client pfx file.')
def cloud_init(server_path, client_path) -> None:
    filename1 = load_vault_file(server_path)
    filename2 = load_vault_file(client_path)
    with ZipFile('cloud-init.zip', 'w') as z:
        z.write(filename1)
        z.write(filename2)
    click.secho('- Writing cloud-init.zip', fg='blue')


@cli.command(help='Create ansible inventory file for WinRM connections.')
@click.option('--ca-trust-path', envvar='SIAB_CA_TRUST_PATH', required=True, help='Vault path ca trust file.')
@click.option('--cert-pem', envvar='SIAB_CERT_PEM', required=True, help='Vault path to client cert pem file.')
@click.option('--cert-key-pem', envvar='SIAB_CERT_KEY_PEM', required=True, help='Vault path to client key pem file.')
def inventory_windows(ca_trust_path, cert_pem, cert_key_pem) -> None:
    click.secho('- Create ansible inventory file for WinRM connections', fg='green')
    state = load_state()
    tfstate_content = state.read_tfstate()
    filename1 = load_vault_file(ca_trust_path)
    filename2 = load_vault_file(cert_pem)
    filename3 = load_vault_file(cert_key_pem)
    create_windows_inventory(state, tfstate_content, (filename1, filename2, filename3))


@cli.command(help='Create ansible inventory file for SSH connections.')
def inventory_linux() -> None:
    click.secho('- Create ansible inventory file for SSH connections', fg='green')
    state = load_state()
    tfstate_content = state.read_tfstate()
    create_linux_inventory(state, tfstate_content)


@cli.command(help='Check connection.')
@click.option('--username', required=True, help='Username for windows access.')
@click.option('--password', required=True, help='Password for windows access.')
def ping(username, password) -> None:
    click.secho(f'- Checking Windows WinRM connection for user {username}', fg='green')
    ping_windows((username, password))


if __name__ == '__main__':
    exit(cli())
