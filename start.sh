#!/bin/bash
cd /Volumes/SSD_M2/code/odoo
source venv/bin/activate
python3 odoo-bin -c odoo.conf "$@"
