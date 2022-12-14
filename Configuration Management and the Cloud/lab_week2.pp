class packages {
   package { 'python-requests':
       ensure => installed,
   }
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
  if $facts[os][family] == "RedHat" {
  #Resource entry
     package { 'nodejs':
       ensure => installed,
     }
  }
}

class machine_info {
  if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
 file { 'machine_info':
       path => $info_path,
       content => template('machine_info/info.erb'),
   }
}

node default {
   class { 'packages': }
   class { 'machine_info': }
   class { 'reboot': }
}

if $facts[uptime_days] > 30 {d
        exec { 'reboot':
           command => $cmd,
        }
    }

class reboot {
      if $facts[kernel] == "windows" {
        $cmd = "shutdown /r"
      } elsif $facts[kernel] == "Darwin" {
        $cmd = "shutdown -r now"
      } else {
        $cmd = "reboot"
      }
      if $facts[uptime_days] > 30 {
        exec { 'reboot':
          command => $cmd,
         }
       }
    }
