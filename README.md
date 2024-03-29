Ansible Role: Kompose
=====================

[![Tests](https://github.com/gantsign/ansible_role_kompose/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_kompose/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.kompose-blue.svg)](https://galaxy.ansible.com/gantsign/kompose)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_kompose/master/LICENSE)

Role to download and install [Kompose](http://kompose.io) the tool for
converting Docker Compose files to Kubernetes resources.

Requirements
------------

* Ansible Core >= 2.12

* Linux Distribution

    * Debian Family

        * Debian

            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

    * RedHat Family

        * Rocky Linux

            * 8

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Kompose version number
kompose_version: '1.29.0'

# SHA256 sum for the redistributable Kompose package (i.e. kompose-linux-amd64.tar.gz)
kompose_redis_sha256sum: '1167e6cc3c3aac346616f6b0232739ae438ea6a1e0aeae0b938831f96298eb55'

# Mirror to download the Kompose from
kompose_mirror: 'https://github.com/kubernetes/kompose/releases/download/v{{ kompose_version }}'

# Directory to store files downloaded for Kompose
kompose_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.kompose
```

Tab Completion for Zsh
----------------------

### Using Ansible

We recommend using the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role to enable
tab completion for Kompose (this must be configured for each user).

```yaml
- hosts: servers
  roles:
    - role: gantsign.kompose

    - role: gantsign.antigen
      users:
        - username: example
          antigen_bundles:
            - name: kompose
              url: gantsign/zsh-plugins
              location: kompose
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen bundle gantsign/zsh-plugins kompose
```

### Manual configuration

To manually configure Zsh add the following to your `.zshrc`:

```bash
eval "$(kompose completion zsh)"
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
