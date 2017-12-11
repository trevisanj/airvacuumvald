import sys
import os
from setuptools import setup, find_packages
from glob import glob

setup(
    name="airvacuumvald",
    packages=["airvacuumvald"],
    include_package_data=True,
    version='0.17.12.11.0',
    license='GNU GPLv3',
    platforms='any',
    description='Python implementation of the air-to-vacuum and vacuum-to-air wavelength '
                'conversion used by VALD (Vienna Atomic Line Database)',
    author='Julio Trevisan',
    author_email='juliotrevisan@gmail.com',
    url='https://github.com/trevisanj/airvacuumvald',
    keywords= ["astronomy", "astrophysics", "vald", "vald3", "air", "vacuum", "wavelength",
               "atomic lines"],
    install_requires=[],
    scripts=[]
)
