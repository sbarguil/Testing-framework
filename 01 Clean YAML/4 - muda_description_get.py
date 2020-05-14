import easygui

easygui.msgbox('Selecione o arquivo de origem', 'Origem')
origfile = easygui.fileopenbox()
arq = open(origfile, 'r')

param = "get"
arqdest = open(origfile + '.changed_' + param, 'w')


substituiparam = 0
achouparam = 0

log = 1  # 1=on 0=off

comando = 0
cmd = ""

param_ok = 0
cont = 0
linha = ""


def operacao(x):
    global cmd
    global comando
    if (x.find('/data/') > 0):
        comando = 1
        cmd = x
        if log: print(cmd)


def parametro(x):
    global param_ok
    if (x.find(param) > 0 and comando == 1):
        param_ok = 1
        if log: print(x)


def summary(x):
    global cont
    global param_ok
    global comando
    global linha
    cont = cont + 1
    if (x.find('summary') > 0 and cont > 2 and param_ok > 0):
        if log: print(x)
        descricao = easygui.textbox(" Digite a descricao " + param + " " + cmd+"\n"+linha)
        cont = 0
        param_ok = 0
        comando = 0
        linha = '      summary: "' + descricao + '"\n'


for linha in arq:
    operacao(linha)
    parametro(linha)
    summary(linha)
    arqdest.write(linha)

arq.close()
arqdest.close()