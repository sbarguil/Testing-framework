import easygui

easygui.msgbox('Selecione o arquivo de origem', 'Origem')
origfile = easygui.fileopenbox()
arq = open(origfile, 'r')

arqdest = open(origfile + '.changed', 'w')

substituiparam = 0
achouparam = 0

log = 1  # 1=on 0=off


def findparam(x):
    global achouparam
    global substituiparam

    if (x.find("get:") != -1):
        achouparam = 1
        if log: print(x)
    if (achouparam == 1 and x.find('tags:') > 0):
        substituiparam = 1
        if log: print(x)

    if (linha.find("post:") != -1):
        achouparam = 2
        if log: print(x)
    if (achouparam == 2 and linha.find('tags:') > 0):
        substituiparam = 2
        if log: print(x)

    if (linha.find("delete:") != -1):
        achouparam = 3
        if log: print(x)
    if (achouparam == 3 and linha.find('tags:') > 0):
        substituiparam = 3
        if log: print(x)

    if (linha.find("put:") != -1):
        achouparam = 4
        if log: print(x)
    if (achouparam == 4 and linha.find('tags:') > 0):
        substituiparam = 4
        if log: print(x)


for linha in arq:

    if (substituiparam == 1):
        if log: print("Deletado: " + linha)
        linha = '      - "RETRIEVAL Operations"\n'
        if log: print("Alterado: " + linha)
        substituiparam = 0
        achouparam = 0

    if (substituiparam == 2):
        if log: print("Deletado: " + linha)
        linha = '      - "CREATION Operations"\n'
        if log: print("Alterado: " + linha)
        substituiparam = 0
        achouparam = 0

    if (substituiparam == 3):
        if log: print("Deletado: " + linha)
        linha = '      - "DELETION Operations"\n'
        if log: print("Alterado: " + linha)
        substituiparam = 0
        achouparam = 0

    if (substituiparam == 4):
        if log: print("Deletado: " + linha)
        linha = '      - "MODIFICATION Operations"\n'
        if log: print("Alterado: " + linha)
        substituiparam = 0
        achouparam = 0

    findparam(linha)
    arqdest.write(linha)

arq.close()
arqdest.close()
