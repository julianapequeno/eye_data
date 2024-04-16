#ideia: unir os trabalhos de shiroyang (extrator para CSV) e hsogo (calibragem)
#Usar os dados coletados para fazer alguma coisa.
#analisar onde a pessoa olha de acordo com o vídeo?

#clustering para verificar onde a pessoa mais olhou na tela?

import pandas as pd

dataset = pd.read_csv('../202404161409.csv')

dataset.head(5)