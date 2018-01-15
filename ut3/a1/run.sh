#!/bin/bash

source /home/sdelquin/.virtualenvs/vmweb/bin/activate
uwsgi --ini /home/sdelquin/imw/vmweb/uwsgi.ini
