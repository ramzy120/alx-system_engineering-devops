# fix Apache server
exec { 'correct-wp-locale-reference':
  command => 'find /var/www/html/ -type f -exec sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" {} +',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -R "class-wp-locale.phpp" /var/www/html/',
}
