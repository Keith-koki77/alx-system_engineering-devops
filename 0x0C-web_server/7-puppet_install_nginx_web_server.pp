#Using puppet for automation

package { 'nginx':
  ensure  => 'installed',
}

# Configures Nginx to listen on port 80
file { 'first content':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

# Configures redirection
file_line { 'install':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://github.com/Keith-koki77 permanent;',
  require => Package['nginx'], 
}

# Ensures Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
