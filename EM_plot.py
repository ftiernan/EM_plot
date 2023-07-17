import numpy as np
import matplotlib.pyplot as plt
from nm_to_rgb import _wavelength_to_rgb

lmin, lmax = 250,1000
x = np.linspace(lmin, lmax, 1000)

# the wave
w_peak = .3
f_mult = 2
offset = 1.0
wv = offset + (w_peak*np.sin(  5 * np.pi * f_mult*x / (lmax + lmin - x)  ))

fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(15)

ax = fig.add_subplot(111, fc='w')
ax.spines['bottom'].set_position(('data',0))
ax.set_xticks([270, 330, 390, 450, 510, 570,710, 780,850, 910, 980])
ax.set_xticklabels(['$10^{2}$Hz', '$10^{4}$Hz', '$10^{6}Hz$', '$10^{8}Hz$', '$10^{10}Hz$','$10^{12}Hz$',
                    '$10^{16}Hz$','$10^{18}Hz$','$10^{20}Hz$','$10^{22}Hz$','$10^{24}Hz$'])

ax1 = ax.twiny()
ax1.spines['top'].set_position(('data',.4))
ax1.set_xticks([ 300, 380, 510, 610, 760, 860, 950])
ax1.set_xticklabels(['$10^{3}$m', '1m', '$10^{6}nm$', '$10^{3}nm$', '1nm$','$10^{-3}nm$','$10^{-5}nm$']) 
# E = hc/lambda
h = 4.135e-15
c = 3e8
hc = h*c
p_energy = [hc/10e3,hc/1,hc/10e-3,hc/10e-6,hc/10e-9,hc/10e-12,hc/10e-14]
#wave_l = np.array([1,2])
#photon_e= h*c/wave_l

print('energy = ',p_energy)
# expect energy =  [1.2405e-10, 1.2405e-06, 0.00012405, 124.05, 124050.00000000001, 12405000.0]
ax2 = ax.twiny()
ax2.spines['top'].set_position(('data', 1.4))
ax2.set_xticks([ 300, 380, 510, 610, 760, 860, 950])
ax2.set_xticklabels(['$1.24 x 10^{-10}$eV', '$1.24 x 10^{-6}$eV', '$1.24 x 10^{-4}$eV', '$1.24 x 10^{-1}$eV',
                     '$1.24 x 10^{2}$eV','$1.24 x 10^{5}nm$','$1.24 x 10^{7}$eV']) 


ax.plot(x, wv, c='k', lw=2)


ax.set_xlim(lmin,lmax)
ax1.set_xlim(lmin,lmax)
ax2.set_xlim(lmin,lmax)
ax.set_ylim(-2,2)

#label and delimit the different regions
e_arr = 1.7
ax.text(530, e_arr-.05, 'Energy increases', color='k', fontdict={'fontsize':14})
ax.annotate('',(300, e_arr), (520, e_arr), arrowprops={'arrowstyle': '-','color':'k','lw':2})
ax.annotate('',(650, e_arr), (950, e_arr), arrowprops={'arrowstyle': '<-','color':'k','lw':2})

ax.text(255, 1.8, 'The EM Spectrum', color='k', fontdict={'fontsize':16})

ax.text(620, -.75, 'Visible Light', color='k', fontdict={'fontsize':14})

ax.text(480, -1.35, '$4x10^{14}Hz$', color='k', fontdict={'fontsize':14})
ax.text(770, -1.35, '$7x10^{14}Hz$', color='k', fontdict={'fontsize':14})

ax.text(300, 0.05, 'Radio waves', color='k', fontdict={'fontsize':10})
ax.text(425, 0.05, 'Microwaves', color='k', fontdict={'fontsize':10})
ax.text(550, 0.05, 'Infrared', color='k', fontdict={'fontsize':10})
ax.text(680, 0.05, 'Ultraviolet', color='k', fontdict={'fontsize':10})
ax.text(825, 0.05, 'X rays', color='k', fontdict={'fontsize':10})
ax.text(930, 0.05, 'Gamma rays', color='k', fontdict={'fontsize':10})

ax.annotate('',(500, -.83), (632, .000), arrowprops={'arrowstyle': '-','color':'k','lw':2})
ax.annotate('',(800, -.83), (658, .000), arrowprops={'arrowstyle': '-','color':'k','lw':2})

# add lines
#ax.axvline(400, -2, 2, c='k', ls='--')
#ax.axvline(750, -2, 2, c='k', ls='--')
# Horixontal axis across center
#ax.axhline(c='k')

ax.yaxis.set_visible(False)
#ax.set_xlabel(r'$\lambda\;/\mathrm{nm}$')

# add color


    # want to plot 400nm to 700nm in 20 blocks
rg_start1 = 630  # x start
rg_stop1 = 660  # x stop
rg_step1 = (rg_stop1 - rg_start1)/20


rg_start2 = 500  # x start
rg_stop2 = 800  # x stop
rg_step2 = (rg_stop2 - rg_start2)/20

rgb_steps = (700 - 400)/20

rgb_color = ['']*20   # creates an empty string array

for i in range(20):
    rgb_color[i] = _wavelength_to_rgb(700 - i*rgb_steps)
    
#print('colors = ',rgb_color)

for i in range(20):
    ax.axvspan(rg_start1 + i*rg_step1, rg_start1 + rg_step1*(i + 1), .5,.595,color=rgb_color[i], ec='none', alpha=1)
    
for i in range(20):
    ax.axvspan(rg_start2 + i*rg_step2, rg_start2 + rg_step2*(i + 1), .2,.295,color=rgb_color[i], ec='none', alpha=1)

    


plt.show()
