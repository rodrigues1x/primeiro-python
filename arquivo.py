nascimento =1997
nome ='lorenzo'
anoAtual =2023
nascimentojovem =2007

def calculoIdade(nascimento,anoAtual):
    idade = anoAtual-nascimento
    idadejovem = anoAtual-nascimentojovem
    return idade
idade=calculoIdade (nascimento,anoAtual)
idadejovem=calculoIdade (nascimentojovem,anoAtual)
print('lorenzo tem '+ str (idade))
print('lorenzo tem ' + str(idadejovem))
