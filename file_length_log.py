#!/usr/bin/env python
# coding: utf-8

# In[27]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

with open('lengths.txt') as infile:
    txt = infile.read()

def split_line(line):
    parts = line.split()
    f = parts[0].split('/')[-1]
    num = int(parts[-2])
    prev = int(parts[-4])
    return f, num, prev
dates = []
files = []
lengths = []
prev_lengths = []
skip = 0
for t in txt.split('commit')[1:]:
    dates.append(t.split('\n')[2][8:])
    try: 
        line1 = t.split('\n')[6]
        line2 = t.split('\n')[8]
        if line2:
            f, num, prev = split_line(line2)
        else:
            f, num, prev = split_line(line1)
    except: 
        f, num, prev = split_line(line1)
    files.append(f)
    lengths.append(num)
    prev_lengths.append(prev)

df = pd.DataFrame()
df['lengths'] = lengths
df['prev_lengths'] = prev_lengths
df['change'] = df['lengths'] - df['prev_lengths']
df['dates'] = pd.to_datetime(dates, errors='coerce', format="%m%d%Y")
df['files'] = files

plt.figure(figsize = [16,9])
i = 0
for name, item in df.groupby('files'):
    if np.size(item['lengths']) > 1:
        plt.plot(item['dates'], item['lengths']/1e6, label = name, color=color_sequence[i])
        i += 1

df_change = df[['dates', 'change']].sort_values(by='dates').reset_index(drop=True)
df_change['total_length'] = df['change'].cumsum()
df_change
plt.plot(df_change['dates'], df_change['total_length']/1e6, label='total', color=color_sequence[i+2])
plt.ylabel("Megabyte [MB]")
plt.xlabel("Time [Year-month]")
plt.title("Git commits over time")
plt.grid()
plt.legend()
plt.show()


# In[ ]:
