# Warnings
import warnings
warnings.filterwarnings(action='ignore')

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('numexpr').setLevel(logging.WARNING)

# Scripts
from cnosolarV2 import cell_temperature
from cnosolarV2 import cen
from cnosolarV2 import data
from cnosolarV2 import def_pvsystem
from cnosolarV2 import energia_minima
from cnosolarV2 import gui_config
from cnosolarV2 import gui_protocols
from cnosolarV2 import irradiance_models
from cnosolarV2 import location_data
from cnosolarV2 import pipeline
from cnosolarV2 import production
from cnosolarV2 import pvstructure
from cnosolarV2.pvsyst_tools import pvsyst

if __name__ == '__main__':
    print(f'Successfully executed from {__name__}.')