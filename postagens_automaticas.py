name: Automação de Postagens

on:
  schedule:
    - cron: "*/5 * * * *"  # Executa a cada 5 minutos
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
        pip install selenium pytrends

    - name: Instalar dependências do Chrome e ChromeDriver
      run: |
        sudo apt-get update -y
        sudo apt-get install -y wget curl unzip
        sudo apt-get install -y chromium-chromedriver
        sudo apt-get install -y xvfb
        sudo apt-get install -y libappindicator3-1 libindicator7

    - name: Rodar script de postagens
      run: |
        export DISPLAY=:99.0  # Configura a variável DISPLAY para Xvfb
        python postagens_automáticas.py  # O script Python
