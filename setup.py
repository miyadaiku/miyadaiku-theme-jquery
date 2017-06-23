import os
import pathlib
from setuptools import setup, find_packages
from miyadaiku.common import setuputils

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

requires = [
    "miyadaiku"
]




setup(
    name="miyadaiku.themes.jquery",
    version="0.0.5",
    author="Atsuo Ishimoto",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    description='jQuery files for miyadaiku static site generator',
    long_description=setuputils.read_file(DIR, 'README.rst'),
    packages=list(setuputils.list_packages(DIR, 'miyadaiku')),
    package_data={
        '': setuputils.SETUP_FILE_EXTS,
    },
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass={'bdist_wheel': setuputils.bdist_wheel_ext},
    pre_wheel='npm install',
)
