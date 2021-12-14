# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.8
# ---

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import Cdf
import Pmf

# +
import warnings
warnings.filterwarnings('ignore')

# %pylab inline
# -

from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))

quic_cpu = "./cpu_quic.csv"
tcp_cpu = "./cpu_tcp.csv"
quic =  pd.read_csv(quic_cpu,',')
tcp = pd.read_csv(tcp_cpu, ',')

quic.count()

tcp.count()

quic['Progress'] = quic['Timestamp'].apply(lambda x: x * 1000 - quic['Timestamp'].min() * 1000)

quic = quic[~(quic['CPU (%)'] == 0.0) ]

quic.head()

quic.tail()

tcp['Progress'] = tcp['Timestamp'].apply(lambda x: x * 1000 - tcp['Timestamp'].min() * 1000)

tcp = tcp[~(tcp['CPU (%)'] == 0.0) ]

tcp.head()

tcp.tail()

q = Cdf.MakeCdfFromList(quic['CPU (%)'].values)
t = Cdf.MakeCdfFromList(tcp['CPU (%)'].values)

# +
fig = plt.figure(figsize = (10,3))
plt.rcParams['font.size'] = 12
ax = plt.gca()
yticks = np.arange(0,1.1,0.2)

plt.plot(q.xs, q.ps, marker='s', linewidth=0.3, markersize=5, fillstyle='none', color = 'orange')

plt.plot(t.xs, t.ps, marker='s', linewidth=0.3, markersize=5, fillstyle='none', color = 'cyan')

ax = fig.axes[0]
ax.grid(False)
ax.set_yticks(yticks)
ax.set_ylim([0,1.05])
ax.set_xlim([0, 100])
ax.set_xscale('linear')
ax.set_xlabel('CPU Utilsation', fontsize=12)
ax.set_ylabel('CDF', fontsize=12)

plt.legend(['Quic', 'TCP'] , fontsize=11, loc='best')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes', -0.05))
ax.spines['left'].set_position(('axes', -0.05))


plt.title('CPU (%)', fontsize=12, y=1.05)
plt.savefig('CPU_utilisation_CDF.pdf', format='pdf', bbox_inches='tight')

# +
fig = plt.figure(figsize = (10,3))
plt.rcParams['font.size'] = 12
ax = plt.gca()
#yticks = np.arange(0,1.1,0.2)

plt.plot(quic['Progress'], quic['CPU (%)'], marker='s', linewidth=0.3, markersize=5, fillstyle='none', color = 'orange')

plt.plot(tcp['Progress'], tcp['CPU (%)'], marker='s', linewidth=0.3, markersize=5, fillstyle='none', color = 'cyan')

ax = fig.axes[0]
ax.grid(False)
#ax.set_yticks(yticks)
ax.set_ylim([0, 100])
ax.set_xlim([0,325000])
ax.set_xscale('linear')
ax.set_xlabel('Progress in ms', fontsize=12)
ax.set_ylabel('CPU Utilisation', fontsize=12)

plt.legend(['Quic', 'TCP'] , fontsize=11, loc='best')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('axes', -0.05))
ax.spines['left'].set_position(('axes', -0.05))


plt.title('CPU (%) with progress', fontsize=12, y=1.05)
plt.savefig('CPU_Utilisation_Progress.pdf', format='pdf', bbox_inches='tight')
# -




