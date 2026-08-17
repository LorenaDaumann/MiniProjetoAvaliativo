#ver slides que falam sobre a criaao do pandas



#TRABALAHNDO DATAS
from datetime import date, time, datetime, timedelta

#data - dia,mes,ano
data = date(2026,7,22)
data_pc = datetime.now()
print(data)
print(data_pc)

#time - horas, minutos, segundos
inicio_filme = datetime(2026, 7, 23, 21, 50)


#datetime - junção data e hora

#timedelta - diferença entre datas e horas
duracoes = timedelta(1)#sew passo apenas um numero, ele entende que é dia
dia_2semana_atras = data - timedelta(days=1, weeks=2)
print(dia_2semana_atras)

data_exemplo = datetime(2026, 1, 1, 12, 0, 0)
result = data_exemplo.strftime("%d/%m/%Y")
