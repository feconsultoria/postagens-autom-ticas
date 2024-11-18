name: Automação de Postagens

on:
  schedule:
    - cron: "0 9 * * *"  # Executa todos os dias às 9:00 AM UTC
  workflow_dispatch:  # Permite disparar manualmente o fluxo de trabalho

jobs:
  postagens_automáticas:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v2

    - name: Configurar Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'  # Você pode alterar a versão do Python conforme necessário

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install pytrends requests

    - name: Rodar script de postagens
      run: |
        python postagens_automáticas.py  # Se o seu script Python estiver nomeado assim
