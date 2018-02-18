pkg_dnf = {
    'chrony': {},
}

svc_systemd = {
    'chronyd': {
        'needs': ['pkg_dnf:chrony'],
    },
}
