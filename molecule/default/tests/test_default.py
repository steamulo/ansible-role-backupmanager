import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_crontab(host):
    resp = host.run("crontab -l").stdout
    assert "/usr/sbin/backup-manager" in resp
