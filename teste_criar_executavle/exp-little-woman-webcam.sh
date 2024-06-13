#este arquivo está configurado para rodar na máquina linux que está no gamelab IMD/UFRN

#ativando o ambiente virtual venv
ls
cd ~
#pwd - comando para ver o diretório atual
cd /home/juliana/Documents/EYEtracking-gitrepo/eye_data
source .venv/bin/activate

#rodando o experimento
psychopy -x ../../web-teste_lastrun.py

#desativando o ambiente virtual
deactivate