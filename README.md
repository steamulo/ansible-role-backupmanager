[![Build Status](https://travis-ci.com/STEAMULO/ansible-role-backupmanager.svg?branch=master)](https://travis-ci.com/STEAMULO/ansible-role-backupmanager)

Backup Manager
=========

Installation and basic configuration of backup-manager

Role Variables
--------------

- **bm_user**: user who possess rights on archives and execute the s3-cmd
- **bm_user_remove_shell**: remove the shell access for the user (enabled by default!)
- **bm_backup_schedule**: backup schedule object
     starthou
     startmin
     startday
     tag
     disable

### General vars

- **bm_archive_method**: The backup method to use. 
    Available methods are:
    - tarball
    - tarball-incremental
    - mysql
    - pgsql
    - none
- **bm_tarball_directories**: Target paths to backup without spaces in their name (list separated with spaces)
- **bm_repository_root**: Where to store the archives
- **bm_tarball_blacklist**: Files to exclude when generating tarballs, you can put absolute or relative paths, Bash wildcards are possible.
- **bm_tarballinc_masterdatetype**: Which frequency to use for the master tarball possible values: weekly, monthly
- **bm_tarballinc_masterdatevalue**: Day of creation of the full archive (1 for monday, 7 for sunday) for a weekly frequency and from 1 to 31 for a monthly frequency)
- **bm_archive_ttl**: Number of days we have to keep an archive (Time To Live)
- **bm_archive_prefix**: Prefix of every archive on that box
- **bm_upload_method**: Method of upload
    Available methods are:
    - ssh
    - rsync (needs to implemented)
    - scp
    - ssh-gpg (needs to implemented)
    - ftp (needs to implemented)
- **bm_upload_destination**: Path of the upload

### S3 upload (beware we don't use native s3 upload of backup-manager)

- **bm_upload_s3_bucket**: The bucket to upload to. This bucket must be dedicated to backup-manager. Don't put the path here (see bm_upload_destination), just the bucket !!!
- **bm_upload_s3_access_key**: The S3 access key provided to you
- **bm_upload_s3_secret_key**: The S3 secret key provided to you
- **bm_upload_s3_ttl**: You can specify a time to live for archives uploaded on S3. If not set, no purging is done on S3.
- **bm_upload_s3_endpoint_url**: Alternative S3 api endpoint
- **bm_upload_s3_host_bucket**: Alternative bucket url
- **bm_upload_s3_excludes**: List of exclude pattern for upload

### SSH upload

- **bm_upload_ssh_user**: The user to use for the SSH connections/transfers
- **bm_upload_ssh_key**: The private key to use for opening the connection
- **bm_upload_ssh_hosts**: Specific ssh hosts 
- **bm_upload_ssh_port**: Port to use for SSH connections (leave blank for default one)
- **bm_upload_ssh_destination**: Destination for ssh uploads (overrides bm_upload_destination)
- **bm_upload_ssh_purge**: Purge archives on remote hosts before uploading?
- **bm_upload_ssh_ttl**: If you set bm_upload_ssh_purge, you can specify a time to live for archives uploaded with SSH. This can let you use different ttl's locally and remotely
                         By default, bm_archive_ttl will be used.

### Mysql Vars

- **bm_mysql_databases**: The list of databases to backup. Wildcard: __ALL__ (will dump all the databases in one archive)
- **bm_mysql_adminlogin**: The user who is allowed to read every databases filled in bm_mysql_databases
- **bm_mysql_adminpass**: Its password
- **bm_mysql_host**: The host where the database is
- **bm_mysql_port**: The port where MySQL listen to on the host
- **bm_mysql_extra_options**: Extra options to append to mysqldump

### PostgreSQL Vars

- **bm_pgsql_databases**: The list of databases to backup. Wildcard: __ALL__ (will dump all the databases in one archive)
- **bm_pgsql_adminlogin**: The user who is allowed to read every databases filled in bm_pgsql_databases
- **bm_pgsql_adminpass**: Its password
- **bm_pgsql_host**: The host where the database is
- **bm_pgsql_port**: The port where PostgreSQL listen to on the host
- **bm_pgsql_extra_options**: Extra options to append to pg_dump

Example Playbook
------------

An example can be found under the [molecule folder](molecule/default/playbook.yml)

Development
------------

This role use the [molecule framework](https://molecule.readthedocs.io/en/stable/) in order to simplify the development process.

Requirements:
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

Setup your local environnement with python virtualenv prior to using molecule :

```virtualenv ~/.virtualenv/backupmanager && source ~/.virtualenv/backupmanager/bin/activate && pip install -r requirements.txt```

Use ```molecule converge``` to create a local environnement and ```molecule login``` to log into the test machine.

Before any commit ensure that every test are passing with ```molecule test```

License
------------

BSD

Author Information
------------

Steamulo - http://www.steamulo.com