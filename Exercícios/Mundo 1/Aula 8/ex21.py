import os
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

caminho_completo = os.path.join(pasta_do_script, "ex21.mp3")

os.startfile(caminho_completo)
