#!/home/tefan/.conda/envs/lftc_env/bin
import argparse
import re
import tabulate
from hash_table import HashTable
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

reserved_words=["int", "float", "struct", "pereche" , "for", "if","#include<iostream>", "main", "std::cin", "std::cout", "\'\\n\'"]
operators = ["+", "-", "/", "%", "*", "==", "!=", "<=", ">=", "=", "&&", "||", ">", "<" ]
separators = ["{", "}", ";" , "(", ")", ",", "<<", ">>"]
parser.add_argument("src", help="Source mlp script")
args = vars(parser.parse_args())
print(args)

atoms = set()
program_structure = []
with open(args['src'], "r") as program:

    for i, line in enumerate(program):
        line_structure = []
        new_line = line
        for word in reserved_words:
            pos = line.find(word)
            while pos >= 0:
                line_structure.append((pos, word, 0))
                atoms.add(word)
                new_line = new_line.replace(word, " "*len(word), 1)
                pos = new_line.find(word)

        for word in separators:
            pos = new_line.find(word)
            while pos >= 0:
                line_structure.append((pos, word, 0))
                atoms.add(word)

                new_line = new_line.replace(word, " "*len(word), 1)
                pos = new_line.find(word)

        for word in operators:
            pos = new_line.find(word)
            while pos >= 0:
                line_structure.append((pos, word, 0))
                atoms.add(word)

                new_line = new_line.replace(word, " "*len(word), 1)
                pos = new_line.find(word)

        line_structure.sort(key=lambda x:x[0])
        new_line = new_line.split()

        start = 0
        p = 0
        for last_atom in new_line:

            for word in line_structure[p:]:
                pos = line.rfind(last_atom, start, word[0])
                start = word[0] + len(word[1])
                p += 1
                if pos >= 0:
                    m = re.fullmatch('[a-zA-Z][a-zA-Z0-9_.]*', str(last_atom))
                    n = re.fullmatch('([1-9][0-9]*(\.[0-9]*)?)|(0(\.[0-9]*)?)', str(last_atom))
                    if m is None and n is None:
                        print(f'INVALID VARIABLE NAME/CONST on line {i} : {str(last_atom)}')
                        exit(1)
                    at = last_atom
                    if m is not None:
                        point = last_atom.find(".")
                        at = last_atom[point+1:]

                    line_structure.append((pos, at, 1 if m is not None else 2))
                    atoms.add(at)

                    if m is not None and len(last_atom) > 8:
                        print(f"MAX 8 CHARACTER IDS ON LINE {i}")
                        exit(1)
                    break;

        line_structure.sort(key=lambda x:x[0])
        program_structure.append(line_structure)

line_size = 50
print("_" * line_size, end="")
print("ANALIZATOR LEXICAL MLP")
print(atoms)
atoms = ["ID", "CONST"]
FIP = []
TS_ID = HashTable()
TS_CONST = HashTable()
for line in program_structure:
    for atom in line:
        if atom[2] == 0:
            if atom[1] not in atoms:
                atoms.append(atom[1])
            FIP.append((atoms.index(atom[1]), None))
        else:
            if atom[2] == 1:
                if TS_ID.find(atom[1]) is None:
                    TS_ID.insert(atom[1], "info")
                FIP.append((0, TS_ID.getIndex(atom[1])))
            else:
                if TS_CONST.find(atom[1]) is None:
                    TS_CONST.insert(atom[1], "info")
                FIP.append((0, TS_CONST.getIndex(atom[1])))

print("_"*line_size, end="")
print(tabulate.tabulate([(a,b) for a,b in enumerate(atoms)], ["Cod", "Atom lexical"]))
print("_"*line_size, end="")
print("FIP")
print(tabulate.tabulate(FIP, ["Cod atom", "Pozitie in TS"]))
print("_"*line_size, end="")
print("TS_ID")
print(tabulate.tabulate(TS_ID.getAll(), ["Pozitie", "Atom lexical", "alte info"]))
print("_"*line_size, end="")
print("TS_CONST")
print(tabulate.tabulate(TS_CONST.getAll(), ["Pozitie", "Atom lexical", "alte info"]))




