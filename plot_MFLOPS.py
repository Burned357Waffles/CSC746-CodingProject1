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


def compute_MFLOPs(data, ops):
    
    for i, n in enumerate(problem_sizes):
        nOps = (2**n) * ops
        data[i] = data[i] * nOps

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

plt.title("Comparison of MFLOPS/s")

code1_MFLOPS = compute_MFLOPs(code1_time, 1)
code2_MFLOPS = compute_MFLOPs(code2_time, 1)
code3_MFLOPS = compute_MFLOPs(code3_time, 1)

plt.plot(code1_MFLOPS, "r-o")
plt.plot(code2_MFLOPS, "b-x")
plt.plot(code3_MFLOPS, "g-^")

# chatGPT helped with formatting ticks
# set ticks
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, labels=[f'$2^{{{x}}}$' for x in problem_sizes])


#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS/s")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
