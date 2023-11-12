#!/home/tefan/.conda/envs/lftc_env/bin
import argparse
import re
import tabulate
from hash_table import HashTable
from automat import AutomatFinit

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
sepChar = "@"
reserved_words = ["int", "float", "struct", "pereche", "for", "if", "#include<iostream>", "main", "std::cin",
                  "std::cout", "\'\\n\'"]
operators = ["+", "-", "/", "%", "*", "==", "!=", "<=", ">=", "=", "&&", "||", ">", "<"]
separators = ["{", "}", ";", "(", ")", ",", "<<", ">>"]
parser.add_argument("src", help="Source mlp script")
args = vars(parser.parse_args())
print(args)

af_ID = AutomatFinit.fromFile('AF_specs/af_ID.spec')
af_CONST = AutomatFinit.fromFile('AF_specs/af_const.spec')
af_RATIONAL = AutomatFinit.fromFile('AF_specs/af_rat.spec')

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
                new_line = new_line.replace(word, f"{sepChar}" * len(word), 1)
                pos = new_line.find(word)

        for word in separators:
            pos = new_line.find(word)
            while pos >= 0:
                line_structure.append((pos, word, 0))
                atoms.add(word)

                new_line = new_line.replace(word, f"{sepChar}" * len(word), 1)
                pos = new_line.find(word)

        for word in operators:
            pos = new_line.find(word)
            while pos >= 0:
                line_structure.append((pos, word, 0))
                atoms.add(word)

                new_line = new_line.replace(word, f"{sepChar}" * len(word), 1)
                pos = new_line.find(word)

        line_structure.sort(key=lambda x: x[0])
        start = 0
        posInLine = 0
        detectedBefore = False
        while posInLine < len(new_line) - 1:
            if not detectedBefore:
                detected_id = af_ID.checkPrefix(new_line[posInLine:])
                detected_const = af_CONST.checkPrefix(new_line[posInLine:])
                detected_rat = af_RATIONAL.checkPrefix(new_line[posInLine:])
                if len(detected_id) > 0:
                    if len(detected_id) > 8:
                        print(f'TOO LENGTHY ID NAME on line {i}')
                    line_structure.append((posInLine, detected_id, 1))
                    posInLine += len(detected_id) -1
                    detectedBefore = True
                else:
                    if len(detected_rat) > len(detected_const):
                        line_structure.append((posInLine, detected_rat, 2))
                        posInLine += len(detected_rat) -1
                        detectedBefore = True

                    elif len(detected_const) > 0:
                        line_structure.append((posInLine, detected_const, 2))
                        posInLine += len(detected_const) -1
                        detectedBefore = True

            else:
                if new_line[posInLine] not in f" {sepChar}":
                    print(f'INVALID VARIABLE NAME/CONST on line {i},{posInLine}')
                    detectedBefore = False

                else:
                    detectedBefore = False

            posInLine += 1

        line_structure.sort(key=lambda x: x[0])
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
