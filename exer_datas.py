from datetime import date


#data_nas= date.isoformat(input("entroduizir data de nascimento:"))
#pr int("nesceu aos :{}".format(data_nas))

data_nas = input("marque a data de nascimento:DD-MM-AAAA : ").split("-")
data_hoje = date.today()

data_nas2= date(int(data_nas[2]), int(data_nas[1]), int(data_nas[0]))
#data_nas_mes = data_nas2.month
idade_dias = (data_hoje - data_nas2).days

print("tem {} dias de idade".format(idade_dias))
#print("tem {} meses de idade".format(idade_meses))
#print("tem {} anos de idade".format(idade_anos))