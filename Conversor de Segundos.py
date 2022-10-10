segundos_str = input("Por favor, digite o número em segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
segs_restantes_1 = total_segs % 86400

horas = segs_restantes_1 // 3600
segs_restantes_2 = segs_restantes_1 % 3600

minutos = segs_restantes_2 // 60
segs_restantes_3 = segs_restantes_2 % 60

segundos = segs_restantes_3

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
