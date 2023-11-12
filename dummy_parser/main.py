from automat import AutomatFinit




if __name__ == '__main__':
    af = AutomatFinit.fromFile('af_cpp.txt')
    print(af)
    # print(af.checkSeq('abaa'))
    # print(af.checkPrefix('abaaa'))
    # print(af.checkSeq('abaaa'))
    # print(af.checkPrefix('ab'))
    print(af.checkSeq("123"))
    print(af.checkSeq("0123"))
    print(af.checkPrefix("12abc"))
    print(af.checkPrefix("12313132ab"))
