# create a file
# tacks 0

file { '/tmp/holberton':
path    => '/tmp/holberton',
group   => 'www-data',
owner   => 'www-data',
mode    => '0744',
content => 'I love Puppet',
}
