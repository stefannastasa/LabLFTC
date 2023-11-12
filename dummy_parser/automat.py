class AutomatFinit:
    @staticmethod
    def computeLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def computeConsole(line):
        return [value.strip() for value in line.strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            Q = AutomatFinit.computeLine(file.readline())
            E = AutomatFinit.computeLine(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = AutomatFinit.computeLine(file.readline())

            S = AutomatFinit.computeTranzitii(AutomatFinit.computeLine(''.join([line for line in file])))

            return AutomatFinit(Q, E, S, q0, F)

    @staticmethod
    def fromConsole():
        S = AutomatFinit.computeConsole(input('S = '))
        E = AutomatFinit.computeConsole(input('E = '))
        s0 = input('s0 = ')
        F = AutomatFinit.computeConsole(input('F = '))

        Sf = AutomatFinit.computeTranzitii(AutomatFinit.computeConsole(input('Sf = ')))

        return AutomatFinit(S, E, Sf, s0, F)

    @staticmethod
    def computeTranzitii(parts):
        result = []
        transitions = []
        index = 0

        while index < len(parts):
            transitions.append(parts[index] + ',' + parts[index + 1])
            index += 2

        for transition in transitions:
            lhs, rhs = transition.split('->')
            state2 = rhs.strip()
            state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

            result.append(((state1, route), state2))

        return result

    def __init__(self, S, E, Sf, s0, F):
        self.S = S
        self.E = E
        self.Sf = Sf
        self.s0 = s0
        self.F = F

    def isState(self, value):
        return value in self.S

    def getTransitionsFor(self, state):
        if state == 's0':
            state = self.s0
        if not self.isState(state):
            raise Exception('Can only get transitions for states')

        return [trans for trans in self.Sf if trans[0][0] == state]

    def showTransitionsFor(self, state):
        transitions = self.getTransitionsFor(state)

        print('{ ' + ' '.join([' -> '.join([str(part) for part in trans]) for trans in transitions]) + ' }')

    def checkSeq(self, seq):
        next = self.s0
        for charact in seq:
            transitions = self.getTransitionsFor(next)
            ok = False
            for trans in transitions:
                if charact in trans[0][1]:
                    next = trans[1]
                    ok = True
            if not ok:
                return False

        if next in self.F:
            return True
        else:
            return False

    def checkPrefix(self, seq):
        checkStr = ""
        answer = ""
        for charact in seq:
            checkStr += charact
            if self.checkSeq(checkStr):
                answer = checkStr

        return answer

    def __str__(self):
        return 'S = { ' + ', '.join(self.S) + ' }\n' \
            + 'E = { ' + ', '.join(self.E) + ' }\n' \
            + 'F = { ' + ', '.join(self.F) + ' }\n' \
            + 'Sf = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.Sf]) + ' }\n' \
            + 's0 = ' + str(self.s0) + '\n'
