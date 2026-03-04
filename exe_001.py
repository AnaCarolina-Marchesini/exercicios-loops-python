'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

# loop para repetição
while True:
    # pedir a nota / Usamos float, pois no enunciado não é especificado se serão números inteiros ou não.
    nota = float(input('Digite uma nota (0-10): '))

    # condição para verificar se a nota atinge os criterios do enunciado.
    if 0 <= nota <= 10:
        # se atingir o print aparece.
        print('Você está dentro dos parâmetros pedidos!')
        # e o programa é encerrado.
        break
    # senão, o programa volta ao começo e repete a pergunta até que o criterio seja atingido.
    else:
        continue