# License
'''
Code by Adyasa
April 28,2020
Released under GNU GPL
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import control

#if using termux
#import subprocess
#import shlex
#end if


Num =[25]
Den =[1,6,5,0]
s1 = signal.lti(Num,Den) 
w, mag, phase = signal.bode(s1)
sys = control.tf(25, [1, 6, 5, 0])
gm, pm, wg, wp = control.margin(sys) #These are the gain margin(not in dB),phase margin,gain cross over frequency and phase crossover frequency

fig=subplot(2,1,1)
plt.semilogx(w, mag)  
plt.axhline(y = 0,xmin=0,xmax= 4.25226694)
plt.axvline(x = 2.04,ymin =0,color = 'r',linestyle='dashed')
plt.axvline(x = 2.24,ymin=0,linestyle='dashed')
plt.axvline(x = 0.378,ymin=0,color='g',linestyle='dashed')
plt.text(2.24,0,'(2.04,0)')
plt.text(0.378,21.8,'(0.378,21.8)')
plt.xlabel('Magnitude Plot')
plt.grid()
fig=subplot(2,1,2)
plt.semilogx(w, phase) 
plt.axhline(y = -180,xmin=0)
plt.axvline(x = 2.04,ymin =0,color = 'r',linestyle='dashed')
plt.axvline(x = 2.24,ymin=0,linestyle='dashed')
plt.axvline(x = 0.378,ymin=0,color ='g',linestyle='dashed')
plt.text(0.378,-115,'(0.378,-115)')
plt.text(2.04,-180,'(2.24,-180)')
plt.xlabel('Phase Plot')
plt.xlabel('Frequency')
plt.grid()
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11048_1.pdf')
#plt.savefig('./figs/ee18btech11048_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11048_1.pdf"))
#else
#plt.show()
