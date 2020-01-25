import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def check_podman_installed(host):
    podman = host.package('podman')
    assert podman.is_installed


def check_podman_available(host):
    command = host.run('podman info')
    assert command.succeeded
