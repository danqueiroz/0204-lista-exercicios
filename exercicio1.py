import datetime

def calculando_dias (dia,mes, ano):
    data_input = datetime.date(year=ano,month=mes,day=dia)
    if data_input is None:
            error = "ops"
            return error
    dias_de_vida = datetime.date.today() - data_input
    return dias_de_vida

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

print("Você tem", calculando_dias(dia, mes, ano), " de vida")