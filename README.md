# YouTube Data Automation

Automação usando **YouTube Data API v3** com Python. Este projeto coleta **IDs de vídeos, visualizações e estatísticas detalhadas** de playlists e canais.

## Funcionalidades

- Geração de credenciais seguras via **OAuth 2.0** no Google Cloud.
- Coleta automática de **IDs de vídeos**, **views** e **estatísticas completas**.
- Suporte a **requisições em lote** para eficiência.
- Estrutura de código limpa com **list comprehensions**, **.join()** e boas práticas de Python.
- Autenticação **local** para testes seguros.
- Fácil integração com **dashboards, relatórios e sistemas de análise de conteúdo**.

## Pré-requisitos

- Python 3.9+
- Conta Google e acesso ao [Google Cloud Console](https://console.cloud.google.com/)
- YouTube Data API v3 habilitada
- Arquivo `secrets.json` com credenciais OAuth 2.0 (adicione ao `.gitignore` para não vazar no GitHub)

## Instalação

1. Clone o repositório:

git clone <https://github.com/seu-usuario/youtube-data-automation.gi>
cd youtube-data-automation

1. Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate # Linux/Mac
env\Scripts\activate # Windows

1. Instale as dependências:

pip install -r requirements.txt

1. Adicione seu arquivo secrets.json na raiz do projeto (não comite no Git, já está no .gitignore).

2. Execute o script:
   python main.py

## O script irá

-Abrir uma janela de autenticação local do Google.
-Coletar todos os vídeos da playlist especificada.
-Listar IDs de vídeos, views e outras estatísticas.
-Exibir os resultados no terminal ou exportar para CSV (opcional).
-Boas práticas implementadas
-Autenticação segura usando OAuth 2.0.
-Requisições em lote para otimizar chamadas à API.
-List comprehension e .join() para processamento rápido de listas.
-Estrutura de código modular e fácil de estender.
-.gitignore configurado para não expor credenciais.

## Ideias de expansão

-Exportar dados para CSV ou Google Sheets.
-Criar dashboards interativos com Plotly ou Dash.
-Automatizar alertas de crescimento de views ou comentários.
-Integrar com serviços de BI como Power BI ou Tableau.
