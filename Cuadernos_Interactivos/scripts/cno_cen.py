get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, './scripts')
import cno_plots_metrics

units = {'kW': 1000, 'MW': 1000000}

def get_cen(ac, perc, decimals, curve=True):
    pac = np.sort(ac)
    pac_max = np.max(ac)

    # Calculate the proportional values of samples
    p = 1. * np.arange(len(ac)) / (len(ac) - 1)

    # CEN
    cen_per = np.round(np.percentile(ac, perc) / units['MW'], decimals) # MW
    cen_pmax = np.round(np.max(ac) / units['MW'], decimals) # MW

    print(f'Pac Max. = {cen_pmax} MW\nCEN ({perc} %) = {cen_per} MW')

    if curve == True:
        plt.plot(pac, p, label=f'Pac Max. = {cen_pmax} MW\nCEN ({perc} %) = {cen_per} MW')

        cno_plots_metrics.plot_specs(title='Capacidad Efectiva Neta',
                                     ylabel=f'Percentil',
                                     xlabel='Potencia AC, $W$',
                                     rot=0, 
                                     ylim_min=0, ylim_max=None, 
                                     xlim_min=None, xlim_max=None, 
                                     loc='best')
        plt.legend(loc='best', bbox_to_anchor=(1,1), fontsize=10);
        
    return cen_per, cen_pmax