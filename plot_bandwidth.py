"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "data_MFLOPS.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

def compute_bandwidth_usage(data, nBytes, capacity):
    
    for i, time in enumerate(data):
        data[i] = (nBytes / time) / capacity

    return data



fname = "data_runtime.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

plt.title("Comparison of Percent of Memory Bandwidth Used")

# Theoretical Peak Bandwidth: 204.8 GB/s per CPU
capacity = 204.8

code1_bandwidth = compute_bandwidth_usage(code1_time, 0, capacity)
code2_bandwidth = compute_bandwidth_usage(code2_time, 8, capacity)
code3_bandwidth = compute_bandwidth_usage(code3_time, 8, capacity)

plt.plot(code1_bandwidth, "r-o")
plt.plot(code2_bandwidth, "b-x")
plt.plot(code3_bandwidth, "g-^")

# chatGPT helped with formatting ticks
# set ticks
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, labels=[f'$2^{{{x}}}$' for x in problem_sizes])

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("% Memory Bandwidth Used")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
