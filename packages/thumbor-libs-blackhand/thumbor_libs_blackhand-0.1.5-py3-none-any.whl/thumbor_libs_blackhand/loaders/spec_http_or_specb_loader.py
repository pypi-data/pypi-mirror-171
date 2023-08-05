#!/usr/bin/python
# -*- coding: utf-8 -*-
# Blackhand library for Thumbor
# Licensed under the GNU/GPL license:
# https://fsf.org/

from thumbor.loaders import http_loader
from thumbor_libs_blackhand.loaders import specb_file_fallback_file_loader
import re
import urllib.parse

async def load(context, path):
    testurl=urllib.parse.unquote(path)

    if re.search('^http[s]?://', testurl):
      return await http_loader.load(context, path)
    else:
      return await specb_file_fallback_file_loader.load(context, path)

