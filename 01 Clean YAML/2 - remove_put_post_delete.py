import os
import easygui

easygui.msgbox('Selecione o arquivo de origem', 'Origem')
arq_orig = easygui.fileopenbox()

arq_dest = arq_orig + "_onlyget"

comando = "sed \"/^  \/data/,/^definitions/{ /^definitions/b;/post:/,/\/data/{/\/data/b;d } ;/delete:/,/\/data/{/\/data/b;d }; }\" " + arq_orig + " > " + arq_orig + "_tmp"

print(comando)
os.system(comando)

comando = "sed \"/^  \/data/,/^definitions/{ /^definitions/b;/put:/,/\/data/{/\/data/b;d } ;}\" " + arq_orig + "_tmp" + " > " + arq_dest
print(comando)
os.system(comando)

os.remove(arq_orig + "_tmp")
