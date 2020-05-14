import os
import easygui

log = 1  # 1=on 0=off

easygui.msgbox('Selecione o arquivo de origem', 'Origem')
arq_orig = easygui.fileopenbox()

arq_dest = arq_orig + "_no_error"
apagar = ""

# Arquivo erros
easygui.msgbox('Selecione o arquivo de erros', 'Error file')
error = easygui.fileopenbox()
error_file = open(error, 'r')

for linha in error_file:
    if log: print(linha)
    if linha.find("to line") > 0:
        if log: print("achou")
        if log: print(linha.split(" ")[3])
        apagar = apagar + linha.split(" ")[3].rstrip('\n') + "d;"

comando = "sed \"" + apagar + "\" " + arq_orig + " > " + arq_dest
if log: print(comando)

os.system(comando)
