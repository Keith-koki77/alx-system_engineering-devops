#!/usr/bin/env bash
#Puppet script to make changes to our configuration file.

file { 'SSH client configuration':
  path    => '/etc/ssh/ssh_config',
  ensure  => present,
  
  content => "
    Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    ",
}
