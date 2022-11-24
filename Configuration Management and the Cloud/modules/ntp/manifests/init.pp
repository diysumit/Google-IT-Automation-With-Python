class ntp{
  package { 'ntp':
    ensure => latest,
    # ensure => installed,
    # ensure => present,
  }
  file { '/etc/ntp.conf':
    # ensure => present,
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify => Service['ntp'],
  }
  service { 'ntp':
    enable => true,
    ensure => running,
    require => File['/etc/ntp.conf'],
    # hasrestart => true,
    # hasstatus  => true,
    # pattern => 'ntp',
  }
}

include ntp
