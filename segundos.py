segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // (24 * 60 * 60)  # Divide por segundos em um dia
segundos %= 24 * 60 * 60          # Calcula o resto dos segundos após a conversão em dias
horas = segundos // (60 * 60)     # Divide por segundos em uma hora
segundos %= 60 * 60               # Calcula o resto dos segundos após a conversão em horas
minutos = segundos // 60          # Divide por minutos em uma hora
segundos %= 60                    # Calcula o resto dos segundos após a conversão em minutos

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))