
#Nível 1: Fácil (Fundamentos)
#Contagem Regressiva: Imprima os números de 10 a 1 usando um for.

for i in range(10,0,-1):
    print(i)
#--------------------------------------------------------------------------
#Tabuada Dinâmica: Peça um número ao usuário e exiba a tabuada dele (1 a 10) usando for.

numeroUsuario = int(input("Informe um número: "))
for i in range(1,11):
    print("-----------------------------")
    print(f'{i} * {numeroUsuario} = {numeroUsuario*i}')

#--------------------------------------------------------------------------
#Soma Infinita: Use um while para somar números que o usuário digitar. Pare apenas quando ele digitar 0 e mostre o total.

numero =1;
soma = 0
while numero != 0:
        numero = int(input("Digite um numero:"))
        soma += numero
print(f"A soma dos numeros: {soma}")


#Nível 2: Intermediário (Lógica e Filtros)
#Apenas os Pares: Percorra um intervalo de 1 a 50 e imprima apenas os números pares.
for i in range(1, 51):
    if i %2 ==0:
        print(i)

#Validação de Dados: Crie um loop while que peça uma senha. Enquanto a senha for diferente de "1234", continue pedindo "Acesso negado, tente novamente".

senhaCorreta = "1234"
senha = "0"
while senhaCorreta != senha:
    senha = (input("Digite uma senha: "))
    if senha == senhaCorreta:
        print('Senha correta!')
        break
    else:
        print("Senha incorreta! Tente novamente.")



#Fatorial: Calcule o fatorial de um número digitado pelo usuário (Ex: $5! = 5 \times 4 \times 3 \times 2 \times 1$).

# 1. Guardamos o número do usuário
numero = int(input("Digite um número: "))

# 2. Criamos uma variável SEPARADA para o resultado, começando em 1
resultado = 1

# 3. O loop usa o 'numero' como limite, mas multiplica o 'resultado'
for i in range(1, numero + 1):
    resultado *= i
    # Se quiser ver o passo a passo, o print fica aqui dentro
    print(f"Multiplicando por {i}: {resultado}")

# 4. Resultado final fora do loop
print(f"O fatorial final de {numero} é {resultado}")



