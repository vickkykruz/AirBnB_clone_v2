# Configuration of the web servwe

index_content = "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>"

package {  'nginx':
  ensure   => 'present',
  provider => 'apt',
}

# Create the directory
file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $index_content,
}

# Create the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

exec { 'remove_existing_link':
  command     => '/bin/rm -f /data/web_static/current',
  onlyif      => '/bin/test -L /data/web_static/current',
  refreshonly => true,
}

exec { 'create_symbolic_link':
  command => '/bin/ln -sf /data/web_static/releases/test/ /data/web_static/current',
  require => File['/data/web_static/current'],
}

# Give ownership to the User and Group
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

exec { 'chown_data_directory':
  command     => '/bin/chown -R ubuntu:ubuntu /data',
  refreshonly => true,
  subscribe   => File['/data'],
}

# Update the nginx configuration
file_line { 'nginx_configuration':
  path    => '/etc/nginx/sites-enabled/default',
  line    => "location /hbnb_static {\n\talias /data/web_static/current/;\n\tindex index.html index.htm;\n}\n",
  match   => '^\s*location \/ {',
  after   => '^.*',
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['create_symbolic_link'],  # Adjust the dependency as needed
}
