#!/use/bin/env python
from os import system

system('clear')
print('\n\033[1;32m SERVIDOR INICIADO EM  -  localhost:8080\033[1;39m\n\n')
system('python -m http.server 8080')
print('\n\n\033[1;30mSERVIDOR ENCERRADO...\n\n\033[m')

