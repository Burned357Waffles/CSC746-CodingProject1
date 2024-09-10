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


def compute_latency(data, nAccesses):
    if nAccesses == 0:
        return data

    for i, time in enumerate(data):
        data[i] = time / nAccesses

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

plt.title("Comparison of Average Memory Latency")

code1_latency = compute_latency(code1_time, 0)
code2_latency = compute_latency(code2_time, 1)
code3_latency = compute_latency(code3_time, 1)

plt.plot(code1_latency, "r-o")
plt.plot(code2_latency, "b-x")
plt.plot(code3_latency, "g-^")

# chatGPT helped with formatting ticks
# set ticks
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, labels=[f'$2^{{{x}}}$' for x in problem_sizes])

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Average Latency in Seconds")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
