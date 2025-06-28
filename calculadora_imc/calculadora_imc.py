#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Índice de Massa Corporal (IMC)
Autor: Johann Moraes Maleski
Descrição: Programa que calcula e classifica o IMC de uma pessoa
"""

def main():
    print("=" * 50)
    print("    CALCULADORA DE ÍNDICE DE MASSA CORPORAL")
    print("=" * 50)
    print()
    
    # 1º e 2º Passo: Definir as variáveis peso e altura
    try:
        peso = float(input("Digite seu peso em quilogramas (kg): "))
        altura = float(input("Digite sua altura em metros (m): "))
        
        # Validação dos dados de entrada
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos!")
            return
        
        if altura > 3.0:  # Altura muito alta, provavelmente em centímetros
            print("Atenção: Altura parece estar em centímetros. Convertendo para metros...")
            altura = altura / 100
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")
        return
    
    # 3º Passo: Calcular o IMC
    # O IMC é calculado dividindo o peso pela altura ao quadrado
    imc = peso / (altura ** 2)
    
    # 4º Passo: Exibir o IMC com duas casas decimais
    print()
    print(f"Seu peso: {peso} kg")
    print(f"Sua altura: {altura:.2f} m")
    print(f"Seu IMC é: {imc:.2f}")
    print()
    
    # 5º Passo: Classificar o IMC usando estrutura condicional if-else
    print("Classificação do IMC:")
    print("-" * 30)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        cor = "🔵"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
        cor = "🟢"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
        cor = "🟡"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
        cor = "🟠"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
        cor = "🔴"
    else:
        classificacao = "Obesidade grau III (mórbida)"
        cor = "🔴"
    
    print(f"{cor} {classificacao}")
    print()
    
    # Exibir tabela de referência
    print("Tabela de Classificação do IMC:")
    print("-" * 40)
    print("🔵 Abaixo de 18,5     - Abaixo do peso")
    print("🟢 18,5 a 24,9       - Peso normal")
    print("🟡 25,0 a 29,9       - Sobrepeso")
    print("🟠 30,0 a 34,9       - Obesidade grau I")
    print("🔴 35,0 a 39,9       - Obesidade grau II")
    print("🔴 40,0 ou mais      - Obesidade grau III")
    print()
    
    # Dicas de saúde
    print("Dicas de Saúde:")
    print("-" * 20)
    if imc < 18.5:
        print("• Consulte um nutricionista para ganhar peso de forma saudável")
        print("• Pratique exercícios para ganhar massa muscular")
    elif 18.5 <= imc < 25:
        print("• Parabéns! Seu peso está dentro da faixa ideal")
        print("• Mantenha uma alimentação equilibrada e pratique exercícios")
    elif 25 <= imc < 30:
        print("• Considere uma dieta balanceada e exercícios regulares")
        print("• Consulte um profissional de saúde para orientações")
    else:
        print("• É recomendado buscar orientação médica")
        print("• Considere um plano de emagrecimento com profissionais")
    
    print()
    print("=" * 50)

def executar_novamente():
    """Função para permitir múltiplos cálculos"""
    while True:
        main()
        
        continuar = input("Deseja calcular outro IMC? (s/n): ").lower().strip()
        if continuar not in ['s', 'sim', 'y', 'yes']:
            break
        print("\n" + "=" * 50 + "\n")
    
    print("Obrigado por usar a Calculadora de IMC!")
    print("Cuide bem da sua saúde! 💪")

if __name__ == "__main__":
    # 6º Passo: Testar o código
    executar_novamente()

