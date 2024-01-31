from datetime import date

cod_pais = input("entrar codigo pais:")
if cod_pais == "P":
    pais = "Portugal"
elif cod_pais == "E":
    pais = "Espanha"
elif cod_pais == "F":
    pais = "Franca"
else:
    pais = "Pais desconhecido"

pu = float(input("entrar preco bilhete:"))
passageiros = int(input("entrar n passageiros:"))
#metodo_1_entrada
data_marcada = (str(input("marque dia da viagem(DD-MM-AAAA):")).split("-"))
data_efectiva = (str(input("marque data efectiva(DD-MM-AAAA):")).split("-"))
#entrada statica da data
#d10 = date(2000,1,10)
#d20 = date(2000,1,14)
#d10 = date(input("marque dia da viagem:"))
#d20 = date(input("marque data efectiva:"))

#metodo_1conversao
d1 = date(int(data_marcada[2]),int(data_marcada[1]),int(data_marcada[0]))
d2 = date(int(data_efectiva[2]),int(data_efectiva[1]),int(data_efectiva[0]))

dias = (d20-d10).days
dias_2 = (d2-d1).days

#metodo_2_entrada+conversao
#data_marcada = (date.isoformat(input("marque dia da viagem(DD-MM-AAAA):")).split("-"))
#data_efectiva = (date.isoformat(input("marque data efectiva(DD-MM-AAAA):")).split("-"))
#data_sistema = date.today()

print("atraso :{}".format(dias))
print("atraso :{}".format(dias_2))

valor = pu*passageiros

if passageiros > 5 and passageiros == 10:
    valtot = valor - (valor*0.05)
elif passageiros>10 and passageiros==20:
    valtot = valor - (valor * 0.10)
else:
    valtot = valor - (valor * 0.50)

#atraso = data_efectiva - data_marcada
atraso = dias
atraso_xdias = dias-2
val_atraso_2dias = (valtot * 0.05) * 2

xdias = 0
cont_val_atraso_xdias = val_atraso_xdias = 0
val_acrecimo = 10

while xdias < atraso_xdias:
    val_atraso_xdias = ((valtot * val_acrecimo) / 100)
    cont_val_atraso_xdias += val_atraso_xdias
    xdias+=1
    if xdias == atraso_xdias - 1:
        break
    else:
        val_acrecimo += 5

valtot_fin = valtot + val_atraso_2dias

#if valtot_fin > 100000 and cod_pais =="P":
   #valtot_a_pagar = valtot_fin - (valtot_fin*0.50)
#else:
valtot_a_pagar = valtot_fin + cont_val_atraso_xdias

print("Pais :{}".format(pais))
print("Passageiros :{}".format(passageiros))
print("PU :{}".format(pu))
#print("Data marcada :{}".format(data_marcada))
#print("Data efectiva :{}".format(data_efectiva))
print("Valor :{}".format(valor))
print("Valor total :{}".format(valtot))
print("dias atraso :{}".format(atraso))
print("atraso_x_dias :{}".format(atraso_xdias))
print("valor atraso_2_dias :{}".format(val_atraso_2dias))
print("valor atraso_x_dias :{}".format(val_atraso_xdias))
print("valor contador atraso_x_dias :{}".format(cont_val_atraso_xdias))
print("valor final :{}".format(valtot_fin))
print("valor final a pagar :{}".format(valtot_a_pagar))