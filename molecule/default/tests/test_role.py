import re


def test_dir(host):
    dir = host.file('/usr/local/bin')
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'


def test_file(host):
    installed_file = host.file('/usr/local/bin/kompose')
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_version(host):
    version = host.check_output('kompose version')
    pattern = '^[0-9\\.]+'
    assert re.search(pattern, version)
