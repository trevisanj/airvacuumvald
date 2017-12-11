__all__ = ["air_to_vacuum", "vacuum_to_air"]


def vacuum_to_air(lambda_vac):
    """
    Vacuum-to-air wavelength conversion

    Args:
        lambda_vac: vacuum wavelength in Angstrom

    Returns:
        lambda_air: air wavelength in Angstrom

    Source:
        http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion

    Original reference:
        Donald Morton (2000, ApJ. Suppl., 130, 403)

    Example:

    >>> # The following code converts wavenumber=2000 cm**-1 to wavelength in Angstrom
    >>> vacuum_to_air(1e8/2000)
    49986.36934549974
    """

    s = 1e4 / lambda_vac
    n = 1 + 0.0000834254 + 0.02406147 / (130 - s ** 2) + 0.00015998 / (38.9 - s ** 2)
    lambda_air = lambda_vac / n
    return lambda_air


def air_to_vacuum(lambda_air):
    """
    Air-to-vacuum wavelength conversion

    Args:
        lambda_air: air wavelength in Angstrom

    Returns:
        lambda_vac: vacuum wavelength in Angstrom

    Formula author (according to [1]):
        N. Piskunov

    Example:

    >>> # The following code converts wavelength=5500 Angstrom to wavenumber in cm**-1:
    >>> 1e8/air_to_vacuum(5500.)
    18176.768046090445

    Example:

    >>> # The following code reproduces the figure shown in [1] ("comparison of the Morton and the inverse
    >>> # transformation by NP between 2000 Å and 100000 Å.")
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> lambda_vac = 10**np.linspace(np.log10(2000), np.log10(1000000), 2000)
    >>> y = air_to_vacuum(vacuum_to_air(lambda_vac))-lambda_vac
    >>> _ = plt.semilogx(lambda_vac, y)
    >>> _ = plt.xlabel("$\lambda$ in Angstroem")
    >>> _ = plt.ylabel("$\Delta\lambda$")
    >>> _ = plt.xlim([lambda_vac[0]-50, lambda_vac[-1]])
    >>> _ = plt.title("air_to_vacuum(vacuum_to_air($\lambda_{vac}$))-$\lambda_{vac}$")
    >>> _ = plt.tight_layout()
    >>> _ = plt.show()

    Source:
        [1] http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion
    """

    s = 1e4 / lambda_air
    n = 1 + 0.00008336624212083 + 0.02408926869968 / (130.1065924522 - s**2) + 0.0001599740894897 / \
        (38.92568793293 - s**2)
    lambda_vac = lambda_air * n
    return lambda_vac

