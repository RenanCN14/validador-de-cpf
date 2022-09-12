def formata_cpf(cpf):
    formatado = []
    for i in cpf:
        if "1234567890".__contains__(i):
            formatado.append(i)
    num = ""
    for i in formatado:
        num += i
    return(num)

def valida_1_digito(cpf):
    cont = 10
    acu = 0
    CPF = []
    if len(cpf) == 11:
        for i in cpf:
            CPF.append(i)
            if len(CPF) <= 9:
                acu += int(i) * cont
                cont -= 1
        result = acu * 10 % 11
        if result == 10:
            result = 0

        if CPF[9] == str(result):
            return True
        else:
            return False
    else:
        return False

def valida_2_digito(cpf):
    cont = 11
    acu = 0
    CPF = []
    if len(cpf) == 11:
        for i in cpf:
            CPF.append(i)
            if len(CPF) <= 10:
                acu += int(i) * cont
                cont -= 1
        result = acu * 10 % 11
        if result == 10:
            result = 0

        if CPF[10] == str(result):
            return True
        else:
            return False
    else:
        return False

def verdadeiro_falso(cpf):
    if valida_1_digito(cpf) and valida_2_digito(cpf):
        print("CPF valido")
    else:
        print("CPF falso")


while True:
    while True:
        cpf = input("Digite um CPF :")
        if cpf == "":
            pass
        else:
            break
    cpf = formata_cpf(cpf)
    verdadeiro_falso(cpf)
    resp = input("Testar novo CPF? (s/n)")
    while True:
        if resp.lower() == 's':
            break
        elif resp.lower() == "n":
            exit()
        else:
            resp = input("Não entendi, digite s ou n: ")
