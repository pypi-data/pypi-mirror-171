"""
Python API to access PDG data.

The Python package pdg provides access to the particle physics data
published by the  Particle Data Group (PDG) in the Review of Particle Physics.
For general information about PDG and the Review of Particle Physics
please visit https://pdg.lbl.gov.

PLEASE NOTE: This package is still under active development and the
data provided by the present version should not be used in scientific publications.
"""
__author__ = 'Particle Data Group'
__version__ = '0.0.3'


import os
from pdg.api import PdgApi


# Constants
SQLITE_FILENAME = 'pdg.sqlite'      # Default SQLite database file used by this API
MIN_SCHEMA_VERSION = 0.0            # Minimum schema version required by this version of the API


def connect(database_url=None):
    """Connect to PDG database and return configured PDG API object."""
    if database_url is None:
        return PdgApi('sqlite:///%s' % os.path.join(os.path.dirname(__file__), SQLITE_FILENAME))
    else:
        return PdgApi(database_url)
