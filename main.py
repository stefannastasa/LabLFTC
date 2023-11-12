from automat import AutomatFinit




if __name__ == '__main__':
    af = AutomatFinit.fromFile('AF_specs/af_test.spec')
    print(af)
    # print(af.checkSeq('abaa'))
    # print(af.checkPrefix('abaaa'))
    # print(af.checkSeq('abaaa'))
    # print(af.checkPrefix('ab'))
    print(af.checkSeq("#include<iostream>intfloatintfloat"))
