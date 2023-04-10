# A puppet script to setup an nginx server

-> exec { 'update apt':
  command => '/usr/bin/env apt-get update'
}

-> package { 'install nginx':
  ensure  => installed
  command => '/usr/bin/env apt-get install nginx'
}

-> file { 'create /data directory':
  ensure => directory,
  path   => '/data',
  mode   => '0774'
}

-> file { 'create test directory':
  ensure => directory,
  path   => '/data/web_static/releases/test'
}

-> file { 'create shared directory':
  ensure => directory,
  path   => '/data/web_static/shared'
}

-> file { 'create index.html file':
  ensure => file,
  path   => '/data/web_static/releases/test',
  name   => 'index.html',
  content => 'Hello world'
}

-> exec { 'create symbolink link':
  command => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  requires => File['create index.html file']
}
