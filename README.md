Ansible Role: Kompose
=====================

[![Build Status](https://travis-ci.com/gantsign/ansible_role_kompose.svg?branch=master)](https://travis-ci.com/gantsign/ansible_role_kompose)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.kompose-blue.svg)](https://galaxy.ansible.com/gantsign/kompose)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_kompose/master/LICENSE)

Role to download and install [Kompose](http://kompose.io) the tool for
converting Docker Compose files to Kubernetes resources.

Requirements
------------

* Ansible >= 2.4

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Kompose version number
kompose_version: '1.16.0'

# SHA256 sum for the redistributable Kompose package (i.e. kompose-linux-amd64.tar.gz)
kompose_redis_sha256sum: 'de5940e74a22199c4eeb34d0b9fdae5ad65cce161e2607c7055899bc87c9c25b'

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

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project uses
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper), which can
install all of them apart for Linux itself.

To test this role run the following command from the project root:

```bash
./moleculew test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)