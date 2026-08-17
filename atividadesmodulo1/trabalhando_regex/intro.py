import re

texto = "Otto, otto, OTTO come mocotó"

padrao = re.compile("otto")
padrao= r"Ot." #ponto significa qualquer coisa
padrao = r"[Oo]tto" #representyam uma letra
matches = re.findall(padrao, texto, flags=re.IGNORECASE)

print(len(matches))
print(matches)