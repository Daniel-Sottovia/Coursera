segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // (3600*24)
segundos_rest = segundos % (3600*24)
horas = segundos_rest // 3600
segundos_horas = segundos_rest % 3600
minutos = segundos_horas // 60
segundos_segundos = segundos_horas % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_segundos} segundos.")