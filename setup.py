import pathlib
from setuptools import setup
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/jquery/dist/'
destdir = DIR / 'miyadaiku_theme_jquery/externals/'
copy_files = [[srcdir, ['jquery*.js'], destdir]]


setup(
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files
)
