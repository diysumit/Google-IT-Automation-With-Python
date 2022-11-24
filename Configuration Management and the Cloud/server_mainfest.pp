class flutter{
    package{"flutter":
        ensure => present,
    }
}

class python{
    package{"python3":
        ensure => present,
    }
    package{"python-pip":
        ensure => present,
    }
    package{"tensorflow":
        ensure => present,
    }
    package{"python-pandas":
        ensure => present,
    }
    package{"python-numpy":
        ensure => present,
    }
}

include flutter
include python
