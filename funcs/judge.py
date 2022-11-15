import os
import resGen.hatena
import resGen.bougen
import resGen.yasasi

def judge(argSen):
    if('♡' in argSen or '💛' in argSen or '❥' in argSen):
        return resGen.yasasi.yasasi(argSen)

    if('?' in argSen or '？' in argSen):
        return resGen.hatena.hatena(argSen)
    return resGen.bougen.bougen(argSen)
