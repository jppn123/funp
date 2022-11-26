def cd(dia,mes):
    meses = ["","janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    m = meses[mes]
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31 or dia < 0:
            print(f"não existe a data {dia} de {m}")
            exit(1)
        elif mes == 1:
            dano = dia
        elif mes == 3:
            dano = dia + 59
        elif mes == 5:
            dano = dia + 120
        elif mes == 7:
            dano = dia + 181
        elif mes == 8:
            dano = dia + 212
        elif mes == 10:
            dano = dia + 273
        elif mes == 12:
            dano = dia + 334
    elif mes == 2:
        if dia > 28 or dia < 0:
            print(f"não existe a data {dia} de {m}")
            exit(2)
        else:
            dano = 31 + dia
            
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30 or dia < 0:
            print(f"não existe a data {dia} de {m}")
            exit(1)
        elif mes == 4:
            dano = dia + 90
        elif mes == 6:
            dano = dia + 151
        elif mes == 9:
            dano = dia + 243
        elif mes == 11:
            dano = dia + 304

  
    return print(f'dia {dia} de {m} é o {dano}º dia do ano')
