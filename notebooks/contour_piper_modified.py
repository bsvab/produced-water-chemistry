import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Ion info

ions_WEIGHT = {'Ca'  : 40.0780,
               'Mg'  : 24.3050,
               'K'   : 39.0983,
               'Na'  : 22.9898,
               'Cl'  : 35.4527,
               'SO4' : 96.0636,
               'CO3' : 60.0092,
               'HCO3': 61.0171}

ions_CHARGE = {'Ca'  : +2,
               'Mg'  : +2,
               'K'   : +1, 
               'Na'  : +1,
               'Cl'  : -1,
               'SO4' : -2,
               'CO3' : -2,
               'HCO3': -1,}

# Define the plotting function
def plot(df, 
         unit='mg/L', 
         figname='contour-filled Piper diagram', 
         figformat='jpg'):
   
    # Basic data check 
    # -------------------------------------------------------------------------
    # Determine if the required geochemical parameters are defined. 
    if not {'Ca', 'Mg', 'Na', 'K', 
            'HCO3', 'CO3', 'Cl', 'SO4'}.issubset(df.columns):
        raise RuntimeError("""
        Trilinear Piper diagram requires geochemical parameters:
        Ca, Mg, Na, K, HCO3, CO3, Cl, and SO4.
        Confirm that these parameters are provided in the input file.""")
        
    # Determine if the provided unit is allowed
    ALLOWED_UNITS = ['mg/L', 'meq/L']
    if unit not in ALLOWED_UNITS:
        raise RuntimeError("""
        Currently only mg/L and meq/L are supported.
        Convert the unit manually if needed.""")
        
    # Global plot settings
    # -------------------------------------------------------------------------
    # mpl.rcParams['lines.linewidth'] = 1
    mpl.rcParams['lines.markersize'] = 6
    
    # Change default settings for figures
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 10
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 10   
    
    # Plot background settings
    # -------------------------------------------------------------------------
    # Define the offset between the diamond and traingle
    offset = 0.10 
    offsety = offset * np.tan(np.pi / 3.0)
    h = 0.5 * np.tan(np.pi / 3.0)
    
    # Calculate the traingles' location 
    ltriangle_x = np.array([0, 0.5, 1, 0])
    ltriangle_y = np.array([0, h, 0, 0])
    rtriangle_x = ltriangle_x + 2 * offset + 1
    rtriangle_y = ltriangle_y
    
    # Calculate the diamond's location 
    diamond_x = np.array([0.5, 1, 1.5, 1, 0.5]) + offset
    diamond_y = h * (np.array([1, 2, 1, 0, 1])) + (offset * np.tan(np.pi / 3))
    
    # Plot the traingles and diamond
    fig = plt.figure(figsize=(10,10), dpi=100)
    ax = fig.add_subplot(111, aspect='equal', frameon=False, xticks=[], yticks=[])
    ax.plot(ltriangle_x, ltriangle_y, '-k', lw=1.0)
    ax.plot(rtriangle_x, rtriangle_y, '-k', lw=1.0)
    ax.plot(diamond_x, diamond_y, '-k', lw=1.0)
    
    # Plot the lines with the interval of 20%
    interval = 0.2
    ticklabels = ['0', '20', '40', '60', '80', '100']
    for i, x in enumerate(np.linspace(0, 1, int(1/interval+1))):
        # the left traingle
        ax.plot([x, x - x / 2.0], 
                [0, x / 2.0 * np.tan(np.pi / 3)], 
                'k:', lw=1.0)
        ## the bottom ticks
        if i in [1, 2, 3, 4]: 
            ax.text(x, 0-0.03, ticklabels[-i-1], 
                    ha='center', va='center')
        ax.plot([x, (1-x)/2.0+x], 
                 [0, (1-x)/2.0*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the right ticks
        if i in [1, 2, 3, 4]:
            ax.text((1-x)/2.0+x + 0.026, (1-x)/2.0*np.tan(np.pi/3) + 0.015, ticklabels[i], ha='center', va='center', rotation=-60)
        ax.plot([x/2, 1-x/2], 
                [x/2*np.tan(np.pi/3), x/2*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the left ticks
        if i in [1, 2, 3, 4]:
            ax.text(x/2 - 0.026, x/2*np.tan(np.pi/3) + 0.015, ticklabels[i], 
                    ha='center', va='center', rotation=60)
        
        # the right traingle
        ax.plot([x+1+2*offset, x-x/2.0+1+2*offset], 
                [0, x/2.0*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the bottom ticks
        if i in [1, 2, 3, 4]:
            ax.text(x+1+2*offset, 0-0.03, ticklabels[i], 
                    ha='center', va='center')
        ax.plot([x+1+2*offset, (1-x)/2.0+x+1+2*offset],
                 [0, (1-x)/2.0*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the right ticks
        if i in [1, 2, 3, 4]:
            ax.text((1-x)/2.0+x+1+2*offset  + 0.026, (1-x)/2.0*np.tan(np.pi/3) + 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=-60)
        ax.plot([x/2+1+2*offset, 1-x/2+1+2*offset], 
                [x/2*np.tan(np.pi/3), x/2*np.tan(np.pi/3)], 
                'k:', lw=1.0)
        ## the left ticks
        if i in [1, 2, 3, 4]:
            ax.text(x/2+1+2*offset - 0.026, x/2*np.tan(np.pi/3) + 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=60)
        
        # the diamond
        ax.plot([0.5+offset+0.5/(1/interval)*x/interval, 1+offset+0.5/(1/interval)*x/interval], 
                 [h+offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3), offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the upper left and lower right
        if i in [1, 2, 3, 4]: 
            ax.text(0.5+offset+0.5/(1/interval)*x/interval  - 0.026, h+offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3) + 0.015, ticklabels[i], 
                    ha='center', va='center', rotation=60)
            ax.text(1+offset+0.5/(1/interval)*x/interval + 0.026, offset*np.tan(np.pi/3)+0.5/(1/interval)*x/interval*np.tan(np.pi/3) - 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=60)
        ax.plot([0.5+offset+0.5/(1/interval)*x/interval, 1+offset+0.5/(1/interval)*x/interval], 
                 [h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3), 2*h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3)], 
                 'k:', lw=1.0)
        ## the lower left and upper right
        if i in [1, 2, 3, 4]:  
            ax.text(0.5+offset+0.5/(1/interval)*x/interval- 0.026, h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3) - 0.015, ticklabels[i], 
                    ha='center', va='center', rotation=-60)
            ax.text(1+offset+0.5/(1/interval)*x/interval + 0.026, 2*h+offset*np.tan(np.pi/3)-0.5/(1/interval)*x/interval*np.tan(np.pi/3) + 0.015, ticklabels[-i-1], 
                    ha='center', va='center', rotation=-60)
    
    # Labels and title
    plt.text(0.5, -offset, '%' + '$Ca^{2+}$', 
             ha='center', va='center', fontsize=12)
    plt.text(1+2*offset+0.5, -offset, '%' + '$Cl^{-}$', 
            ha='center', va='center', fontsize=12)
    plt.text(0.25-offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Mg^{2+}$',  
             ha='center', va='center', rotation=60, fontsize=12)
    plt.text(1.75+2*offset+offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$SO_4^{2-}$',  
              ha='center', va='center', rotation=-60, fontsize=12)
    plt.text(0.75+offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Na^+$' + '+%' + '$K^+$',  
              ha='center', va='center', rotation=-60, fontsize=12)
    plt.text(1+2*offset+0.25-offset*np.cos(np.pi/30), 0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$HCO_3^-$' + '+%' + '$CO_3^{2-}$',  
              ha='center', va='center', rotation=60, fontsize=12)
    
    plt.text(0.5+offset+0.5*offset+offset*np.cos(np.pi/30), h+offset*np.tan(np.pi/3)+0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$SO_4^{2-}$' + '+%' + '$Cl^-$',  
              ha='center', va='center', rotation=60, fontsize=12)
    plt.text(1.5+offset-0.25+offset*np.cos(np.pi/30), h+offset*np.tan(np.pi/3)+0.25*np.tan(np.pi/3)+offset*np.sin(np.pi/30), '%' + '$Ca^{2+}$' + '+%' + '$Mg^{2+}$', 
              ha='center', va='center', rotation=-60, fontsize=12)
    
     # Convert unit if needed
    if unit == 'mg/L':
        gmol = np.array([ions_WEIGHT['Ca'], 
                         ions_WEIGHT['Mg'], 
                         ions_WEIGHT['Na'], 
                         ions_WEIGHT['K'], 
                         ions_WEIGHT['HCO3'],
                         ions_WEIGHT['CO3'], 
                         ions_WEIGHT['Cl'], 
                         ions_WEIGHT['SO4']])
    
        eqmol = np.array([ions_CHARGE['Ca'], 
                          ions_CHARGE['Mg'], 
                          ions_CHARGE['Na'], 
                          ions_CHARGE['K'], 
                          ions_CHARGE['HCO3'], 
                          ions_CHARGE['CO3'], 
                          ions_CHARGE['Cl'], 
                          ions_CHARGE['SO4']])
    
        tmpdf = df[['Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4']]
        dat = tmpdf.values
        
        meqL = (dat / abs(gmol)) * abs(eqmol)
        
    elif unit == 'meq/L':
        meqL = df[['Ca', 'Mg', 'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4']].values
    
    else:
        raise RuntimeError("""
        Currently only mg/L and meq/L are supported.
        Convert the unit if needed.""")
    
    # Calculate the percentages
    sumcat = np.sum(meqL[:, 0:4], axis=1)
    suman = np.sum(meqL[:, 4:8], axis=1)
    cat = np.zeros((dat.shape[0], 3))
    an = np.zeros((dat.shape[0], 3))
    cat[:, 0] = meqL[:, 0] / sumcat                  # Ca
    cat[:, 1] = meqL[:, 1] / sumcat                  # Mg
    cat[:, 2] = (meqL[:, 2] + meqL[:, 3]) / sumcat   # Na+K
    an[:, 0] = (meqL[:, 4] + meqL[:, 5]) / suman     # HCO3 + CO3
    an[:, 2] = meqL[:, 6] / suman                    # Cl
    an[:, 1] = meqL[:, 7] / suman                    # SO4

    # Convert into cartesian coordinates
    cat_x = 0.5 * (2 * cat[:, 2] + cat[:, 1])
    cat_y = h * cat[:, 1]
    an_x = 1 + 2 * offset + 0.5 * (2 * an[:, 2] + an[:, 1])
    an_y = h * an[:, 1]
    d_x = an_y / (4 * h) + 0.5 * an_x - cat_y / (4 * h) + 0.5 * cat_x
    d_y = 0.5 * an_y + h * an_x + 0.5 * cat_y - h * cat_x
      
    # Kernel density estimation
    from sklearn.neighbors import KernelDensity
    from matplotlib.path import Path
    
    nbins = 500
    cmap = 'Reds'
    clines = 'black'                                                                            # ADDED

    
    kde = KernelDensity(kernel='gaussian', 
                        bandwidth=0.05,
                        metric='euclidean')
    
    x = np.linspace(0,  1 + 2 * offset + 1, nbins)
    y = np.linspace(0,  h * 2 + (offset * np.tan(np.pi / 3)), nbins)
    xx, yy = np.meshgrid(x, y)
    points = np.vstack((xx.flatten(), yy.flatten())).T
    
    # The left triangle
    tupVerts = [(0, 0), 
                (0.5, h), 
                (1, 0), 
                (0,0)]
    kde.fit(np.vstack((cat_x, cat_y)).T)
    p = Path(tupVerts)
    grid = p.contains_points(points)
    mask = grid.reshape(nbins, nbins).flatten()
    
    z = np.exp(kde.score_samples(points))
    z[np.where(mask==False)] = -9999
    zz = z.reshape(xx.shape)
    
    plt.contourf(xx, yy, zz, 
                 levels=np.linspace(0, z.max(), 50), 
                 cmap=cmap)
    
    plt.contour(xx, yy, zz,
                levels=np.linspace(0, z.max(), 15), 
                linestyles='solid', 
                linewidths=0.5, 
                colors=[clines], 
                alpha=0.8, 
                zorder=10)                                                                    # ADDED
    
    # The right triangle
    tupVerts = [(1 + 2 * offset, 0), 
                (1 + 2 * offset + 0.5, h), 
                (2 + 2 * offset, 0), 
                (1 + 2 * offset, 0)]
    kde.fit(np.vstack((an_x, an_y)).T)
    p = Path(tupVerts)
    grid = p.contains_points(points)
    mask = grid.reshape(nbins, nbins).flatten()
    
    z = np.exp(kde.score_samples(points))
    z[np.where(mask==False)] = -9999
    zz = z.reshape(xx.shape)
    
    plt.contourf(xx, yy, zz, levels=np.linspace(0, z.max(), 50), 
                 cmap=cmap)

    plt.contour(xx, yy, zz, levels=np.linspace(0, z.max(), 15), 
                linestyles='solid', 
                linewidths=0.5, 
                colors=[clines], 
                alpha=0.8, 
                zorder=10)                                                                    # ADDED

    # The central diamond
    tupVerts = [(0.5 + offset, h + offset * np.tan(np.pi / 3)), 
                (1.0 + offset, 2 * h + offset * np.tan(np.pi / 3)), 
                (1.5 + offset, h + offset * np.tan(np.pi / 3)), 
                (1.0 + offset, offset * np.tan(np.pi / 3)),
                (0.5 + offset, h + offset * np.tan(np.pi / 3))]
    kde.fit(np.vstack((d_x, d_y)).T)
    p = Path(tupVerts)
    grid = p.contains_points(points)
    mask = grid.reshape(nbins, nbins).flatten()

    z = np.exp(kde.score_samples(points))
    z[np.where(mask==False)] = -9999
    zz = z.reshape(xx.shape)
    
    cf = plt.contourf(xx, yy, zz, levels=np.linspace(0, z.max(), 100), 
                      cmap=cmap)

    cb = plt.colorbar(cf, extend='both', spacing='uniform',
                      orientation='vertical', fraction=0.025, pad=0.05)
    
    cb.ax.set_ylabel('$Density$', rotation=90, labelpad=-75, fontsize=14)
    cb.ax.set_yticks([0, z.max()])
    cb.ax.set_yticklabels(['Low', 'High'], fontsize=12)

    plt.contour(xx, yy, zz, levels=np.linspace(0, z.max(), 15), 
                linestyles='solid', 
                linewidths=0.5, 
                colors=[clines], 
                alpha=0.8, 
                zorder=10)                                                               # ADDED
    
    # Display the info
    cwd = os.getcwd()
    print("Contour-filed Piper plot created. Saving it to %s \n" %cwd)
    
    # Save the figure
    plt.savefig(figname + '.' + figformat, format=figformat, 
                bbox_inches='tight', dpi=300)
    
    return
