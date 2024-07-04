# netbox plugin example
This prototype plugin simply reads netbox ip addresses and displays it in a view as table with a button to export the data to PDF.
I did this to investigate how to create plugins in netbox in order to create PDF reports since this isn't a feature of netbox.

## Installation
1. Activate netbox venv: `source /opt/netbox/venv/bin/activate`
2. Install with pip: `sudo /opt/netbox/venv/bin/python3 -m pip install --editable .`
3. Add plugin to netbox's `configuration.py` `PLUGIN` list
4. Run netbox dev server: `python3 /opt/netbox/netbox/manage.py runserver 0.0.0.0:8001 --insecure`
