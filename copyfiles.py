#!/usr/bin/env python3

import pathlib
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/jquery/dist/'
destdir = DIR / 'miyadaiku_theme_jquery/externals/'
copy_files = [[srcdir, ['jquery*.js'], destdir]]

setuputils.copyfiles(copy_files)
