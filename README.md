# Calculadora de Índice de Massa Corporal (IMC)

## Descrição
Este projeto implementa uma calculadora de IMC (Índice de Massa Corporal) em Python, desenvolvida como parte do portfólio de Linguagem de Programação do 2º Semestre.

**Autor:** Johann Moraes Maleski  
**Polo:** Anhanguera Ingleses, Florianópolis/SC

## Funcionalidades

- ✅ Cálculo do IMC baseado em peso e altura
- ✅ Classificação automática do IMC
- ✅ Validação de dados de entrada
- ✅ Conversão automática de altura (cm para metros)
- ✅ Exibição de tabela de referência
- ✅ Dicas de saúde personalizadas
- ✅ Interface amigável com emojis
- ✅ Opção para múltiplos cálculos
- ✅ Interface web com Flask

## Como usar

### Requisitos
- Python 3.x instalado no sistema

### Execução via linha de comando (terminal)

1. Acesse a pasta do projeto:
   ```bash
   cd "Caminho/para/Calculador IMC"
   ```
2. Execute o script no terminal:
   ```bash
   python calculadora_imc.py
   ```

### Execução da interface web

1. Abra o terminal na pasta do projeto.
2. Crie e ative o ambiente virtual (caso ainda não exista):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```
3. Instale as dependências:
   ```powershell
   pip install flask
   ```
4. Execute o aplicativo web:
   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```
5. Abra o navegador e acesse:
   - http://127.0.0.1:5000

### Exemplo de uso (linha de comando)

```
==================================================
    CALCULADORA DE ÍNDICE DE MASSA CORPORAL
==================================================

Digite seu peso em quilogramas (kg): 80
Digite sua altura em metros (m): 1.75

Seu peso: 80.0 kg
Sua altura: 1.75 m
Seu IMC é: 26.12

Classificação do IMC:
------------------------------
🟡 Sobrepeso
```

## Classificação do IMC

| Faixa de IMC      | Classificação              |
|-------------------|---------------------------|
| Abaixo de 18,5    | Abaixo do peso            |
| 18,5 a 24,9       | Peso normal               |
| 25,0 a 29,9       | Sobrepeso                 |
| 30,0 a 34,9       | Obesidade grau I          |
| 35,0 a 39,9       | Obesidade grau II         |
| 40,0 ou mais      | Obesidade grau III        |

## Estrutura do Código

O código segue os 6 passos descritos no portfólio:

1. **1º Passo:** Acesso ao ambiente de desenvolvimento
2. **2º Passo:** Definição das variáveis peso e altura
3. **3º Passo:** Cálculo do IMC (peso / altura²)
4. **4º Passo:** Exibição do IMC com duas casas decimais
5. **5º Passo:** Classificação usando estrutura if-else
6. **6º Passo:** Teste do código com valores válidos

## Validações Implementadas

- ✅ Verificação de valores numéricos válidos
- ✅ Validação de valores positivos
- ✅ Conversão automática de altura em centímetros
- ✅ Tratamento de erros de entrada

## Melhorias Adicionais

Além dos requisitos básicos, foram implementadas:

- Interface mais amigável com formatação
- Tabela de referência visual
- Dicas de saúde personalizadas
- Opção para múltiplos cálculos
- Validações robustas de entrada
- Documentação completa
- Interface web com Flask para uso no navegador

## Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Linguagem de Programação.

