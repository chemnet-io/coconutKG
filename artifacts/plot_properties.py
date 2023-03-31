import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    '--input',
                    help='path to csv file',
                    type=str)
parser.add_argument('-o',
                    '--output',
                    help='path to output file',
                    type=str)
parser.add_argument('-x',
                    '--xaxis',
                    help='name of x column',
                    type=str)
parser.add_argument('-y',
                    '--yaxis',
                    help='name of y column',
                    type=str)

args = parser.parse_args()


sns.set_theme(style="white")

df = pd.read_csv(args.input, sep=r'\s*,\s*', engine='python')

g = sns.lineplot(data=df, x=args.xaxis, y=args.yaxis)
g.get_figure().set_size_inches(8, 16)


plt.savefig(args.output, bbox_inches='tight')
