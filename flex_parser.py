
import argparse
import re
import tabulate
from hash_table import HashTable
from automat import AutomatFinit
import subprocess
import os
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source mlp script")
args = vars(parser.parse_args())
print(args)
program = args['src']

subprocess.run(f"./flex/a.out {args['src']} > output.txt", shell=True)

atoms = ["ID", "CONST"]
FIP = []
TS_ID = HashTable()
TS_CONST = HashTable()
with open("output.txt", "r") as f:
    for line in f.readlines():
        if "Error on line" in line:
            print(line)
            continue    
        values=line.strip().split("|")
        if values[0] == "1":
            if values[1] not in atoms:
                atoms.append(values[1])
            FIP.append((atoms.index(values[1]), None))
        elif values[0] == "3":
            if TS_ID.find(values[1]) is None:
                TS_ID.insert(values[1], "info")
            FIP.append((0, TS_ID.getIndex(values[1])))
        else:
            if TS_CONST.find(values[1]) is None:
                TS_CONST.insert(values[1], "info")
            FIP.append((0, TS_CONST.getIndex(values[1])))

line_size=50
print("_" * line_size, end="")
print(tabulate.tabulate([(a, b) for a, b in enumerate(atoms)], ["Cod", "Atom lexical"]))
print("_" * line_size, end="")
print("FIP")
print(tabulate.tabulate(FIP, ["Cod atom", "Pozitie in TS"]))
print("_" * line_size, end="")
print("TS_ID")
print(tabulate.tabulate(TS_ID.getAll(), ["Pozitie", "Atom lexical", "alte info"]))
print("_" * line_size, end="")
print("TS_CONST")
print(tabulate.tabulate(TS_CONST.getAll(), ["Pozitie", "Atom lexical", "alte info"]))

