__all__ = ["air_to_vacuum", "vacuum_to_air"]


def vacuum_to_air(λvac):
    """
    Vacuum-to-air wavelength conversion

    Args:
        λvac: vacuum wavelength in Angstrom

    Returns:
        λair: air wavelength in Angstrom

    Source:
        http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion

    Original reference:
        Donald Morton (2000, ApJ. Suppl., 130, 403)

    Example:

    >>> # The following code converts wavenumber=2000 cm**-1 to wavelength in Angstrom
    >>> vacuum_to_air(1e8/2000)
    49986.36934549974
    """
    # if λvac <= 0:
    #     raise ValueError("λvac must be > 0")

    s = 1e4 / λvac
    n = 1 + 0.0000834254 + 0.02406147 / (130 - s ** 2) + 0.00015998 / (38.9 - s ** 2)
    λair = λvac / n
    return λair


def air_to_vacuum(λair):
    """
    Air-to-vacuum wavelength conversion

    Args:
        λair: air wavelength in Angstrom

    Returns:
        λvac: vacuum wavelength in Angstrom

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
    >>> λvac = 10**np.linspace(np.log10(2000), np.log10(1000000), 2000)
    >>> y = air_to_vacuum(vacuum_to_air(λvac))-λvac
    >>> _ = plt.semilogx(λvac, y)
    >>> _ = plt.xlabel("$\lambda$ in Angstroem")
    >>> _ = plt.ylabel("$\Delta\lambda$")
    >>> _ = plt.xlim([λvac[0]-50, λvac[-1]])
    >>> _ = plt.title("air_to_vacuum(vacuum_to_air($\lambda_{vac}$))-$\lambda_{vac}$")
    >>> _ = plt.tight_layout()
    >>> _ = plt.show()

    Source:
        [1] http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion
    """
    # if λair <= 0:
    #     raise ValueError("λair must be > 0")

    s = 1e4 / λair
    n = 1 + 0.00008336624212083 + 0.02408926869968 / (130.1065924522 - s**2) + 0.0001599740894897 / \
        (38.92568793293 - s**2)
    λvac = λair * n
    return λvac

