# YouTube Data Automation

 Automação usando **YouTube Data API v3** com Python. Este projeto coleta **IDs de vídeos, visualizações e estatísticas detalhadas** de playlists e canais.

## Funcionalidades

- Geração de credenciais seguras via OAuth 2.0
- Coleta automática de IDs de vídeos e estatísticas
- Suporte a requisições em lote
- Código limpo e eficiente
- Autenticação local para testes
- Integração com dashboards e relatórios

## Pré-requisitos

- Python 3.9+
- Conta Google e acesso ao Google Cloud Console
- Arquivo secrets.json

OBS: Arquivo com credenciais OAuth 2.0 (adicionar ao `.gitignore` para não vazar no GitHub).

## Instalação

**1) Clone o repositório**

```bash
git clone https://github.com/seu-usuario/youtube-data-automation.git
cd youtube-data-automation
```

**2) Crie e ative um ambiente virtual**

```bash
python -m venv venv

- Ativar ambiente virtual

source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3) Instale as dependências**

```bash
pip install -r requirements.txt
```

**4) Adicione `secrets.json`**

Coloque seu `secrets.json` na raiz do projeto (não comite).

**5) Execute o script**

```bash
python main.py
```

## O script irá:

- Abrir uma janela de autenticação local do Google: Inicia o fluxo OAuth para obter permissão do usuário.
- Coletar todos os vídeos da playlist especificada: Percorre a playlist e coleta os IDs dos vídeos.
- Listar IDs de vídeos, views e outras estatísticas: Agrega e exibe métricas relevantes de cada vídeo.

## Boas práticas implementadas:

- Autenticação segura usando OAuth 2.0
- Requisições em lote para otimizar chamadas à API
- Uso de list comprehensions e `.join()` para processamento eficiente
- Estrutura modular e fácil de estender
- `.gitignore` configurado para não expor credenciais

## Ideias de expansão

- Exportar dados para CSV ou Google Sheets
- Criar dashboards interativos com Plotly ou Dash
- Automatizar alertas de crescimento
- Integração com serviços de BI (Power BI, Tableau)
