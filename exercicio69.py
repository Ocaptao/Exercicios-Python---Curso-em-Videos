# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nãoo continuar
# No final, mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos

contador_idade = 0
contador_h = 0
contador_m20 = 0
sexos = ["f","m"]
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).lower().strip()
    while sexo != "f" and sexo != "m":
        sexo = str(input("Digite seu sexo [M/F]: ")).lower().strip()
    if idade > 18:
        contador_idade += 1
    if sexo == "m":
        contador_h += 1
    if sexo == "f" and idade < 20:
        contador_m20 += 1
    op = str(input("Deseja Cadastrar mais Pessoas [S/N]: ")).lower().strip()
    while op != "s" and op != "n":
        op = str(input("Deseja Cadastrar mais Pessoas [S/N]: ")).lower().strip()
    if op == "n":
        break
print("=-="*10)
print(f"Foram cadastrados {contador_idade} pessoas maiores de 18 anos")
print(f"Foram cadastrados {contador_h} homens")
print(f"E {contador_m20} são mulheres menores de 20 anos")



    
