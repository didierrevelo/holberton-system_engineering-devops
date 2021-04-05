# task 2
#create a manifest

exec { 'pkill killmenow':
  command   => '/usr/bin/pkill killmenow',
}
