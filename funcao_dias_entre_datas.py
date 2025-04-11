from datetime import datetime       

def dias_entre_datas(data1, data2):
    formato = "%d/%m/%Y"
    d1 = datetime.strptime(data1, formato)
    d2 = datetime.strptime(data2, formato)
    diferenca = abs((d2 - d1).days)
    return diferenca

dias = dias_entre_datas("24/03/2025", "11/04/2025")
print(f"Passaram-se {dias} dias entre as datas")

