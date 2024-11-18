name: Automate Postings

on:
  schedule:
    - cron: '0 0 * * *' # Executa o script todos os dias à meia-noite (UTC)
  workflow_dispatch: # Permite rodar manualmente

jobs:
  postagens:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt  # Instale as dependências necessárias

      - name: Run postagens automáticas script
        run: |
          python postagens_automaticas.py  # Substitua pelo nome correto do seu script
