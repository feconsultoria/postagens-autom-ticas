# Automação de Postagens

Este repositório contém um fluxo de trabalho automatizado para postagens em blogs, utilizando o GitHub Actions para rodar um script Python que coleta tendências do Google e publica conteúdo no Blogger.

## Como funciona

O fluxo de trabalho é executado a cada 5 minutos, conforme configurado no GitHub Actions. Ele coleta as últimas tendências do Google e gera postagens automaticamente no seu blog.

## Requisitos

- Python 3.8 ou superior
- Conta no [GitHub](https://github.com) para configurar a automação
- Conta no [Blogger](https://www.blogger.com) e configuração da API para a publicação das postagens

## Como usar

Clone este repositório:

```bash
git clone https://github.com/feconsultoria/postagens-autom-ticas.git
