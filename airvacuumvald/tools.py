from . import airvacuum as av

def lambda2nu(l_air):
    """
    Wavelength (air; angstrom) to wavenumber (vacuum; cm**-1)

    Args:
        l_air: wavelength in angstrom

    Returns:
        nu_vac: wavenumber in cm**-1
    """
    l_vac = av.air_to_vacuum(l_air)
    ret = 1e8/l_vac
    return ret


def nu2lambda(nu_vac):
    """
    Wavenumber (vacuum; cm**-1) to wavelength (air; angstrom)

    Args:
        nu_vac: wavenumber in cm**-1

    Returns:
        l_air: wavelength in angstrom
    """
    l_vac = 1e8/nu_vac
    ret = av.vacuum_to_air(l_vac)
    return ret
