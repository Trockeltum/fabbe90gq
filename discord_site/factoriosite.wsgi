#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/pi/website/discord_site/")

from mainscript import app as application
application.secret_key = 'you-will-never-guess'
