# comparison of MESA and mppnp abundance profiles for the 14th thermal
# pulse convection zone of the Set1.1 2Msun, Z=0.01 AGB sequence. The
# mass range shown includes the top of the CO code, the He-shell flash
# convection zone, the (now extinct) H-burning shell and the bottom of
# the convective envelope. The H-free core mass is 0.572Msun for that
# model.

# useage: either with ed in the ipython session or
#        $ mpython < example_figure.py

read_new=True
CADC_DIR='/tmp/nugrid/'
NUGRID_PYTHON_DIR=''  # point python to the nugrid python tools, in case 
                      # anyone does not have them already in the proper 
                      # location.  
if read_new:
    sys.path.append(NUGRID_PYTHON_DIR)
    import mesa
    import nugridse as ns
    mesa_LOGS=CADC_DIR+'data/set1/set1.1/see_wind/M2.00Z1.0e-02/LOGS'
    m=mesa.star_log(mesa_LOGS)
    s=ns.se(CADC_DIR+"data/set1/set1.1/ppd_wind/M2.00Z1.0e-02.standard/H5_out")
    p24k=mesa.mesa_profile(mesa_LOGS,24000)

m.kippenhahn(1,'model')
savefig('kippenhahn.png')

figure(2)
p24k.plot('mass','c12',legend='$^{12}\mathrm{C}$ MESA',shape='o',logy=True)
s.plot('mass','C-12',fname=24000,shape='-',legend='$^{12}\mathrm{C}$ mppnp',logy=True)
p24k.plot('mass','n14',legend='$^{14}\mathrm{N}$ MESA',shape='s',logy=True)
s.plot('mass','N-14',fname=24000,shape='-.',legend='$^{14}\mathrm{N}$ mppnp',logy=True)
legend(loc=6)
xlim(0.52984261186264314, 0.5764659209157128)
ylim(-5.27, -0.084)
ylabel('$\\log(X)$')
xlabel('$m_\mathrm{r} / \mathrm{M}_\odot$')
title('')
savefig('example_figure.pdf')
