# YouTube Data Automation

Automação usando **YouTube Data API v3** com Python. Este projeto coleta **IDs de vídeos, visualizações e estatísticas detalhadas** de playlists e canais.

## Funcionalidades

---

**Geração de credenciais seguras via OAuth 2.0**

Configuração de OAuth 2.0 pelo Google Cloud para obter credenciais seguras.

---

**Coleta automática de IDs de vídeos e estatísticas**

Raspagem e agregação automática de IDs, views e outras métricas dos vídeos.

---

**Suporte a requisições em lote**

Uso de chamadas em lote para reduzir latência e limites de requisições.

---

**Código limpo e eficiente**

Estrutura com list comprehensions, `.join()` e boas práticas de Python para legibilidade e performance.

---

**Autenticação local para testes**

Fluxo de autenticação local seguro para desenvolvimento e testes.

---

**Integração com dashboards e relatórios**

Fácil integração com ferramentas de visualização e análise (CSV, Google Sheets, BI).

## Pré-requisitos

---

**Python 3.9+**

Instale Python 3.9 ou superior.

---

**Conta Google e acesso ao Google Cloud Console**

Habilite o YouTube Data API v3 no seu projeto do Google Cloud.

---

**Arquivo secrets.json**

Arquivo com credenciais OAuth 2.0 (adicionar ao `.gitignore` para não vazar no GitHub).

## Instalação

---

**1) Clone o repositório**

```bash
git clone https://github.com/seu-usuario/youtube-data-automation.git
cd youtube-data-automation
```

---

**2) Crie e ative um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# on Windows: venv\Scripts\activate
```

---

**3) Instale as dependências**

```bash
pip install -r requirements.txt
```

---

**4) Adicione `secrets.json`**

Coloque seu `secrets.json` na raiz do projeto (não comite).

---

**5) Execute o script**

```bash
python main.py
```

## O script irá

---

**Abrir uma janela de autenticação local do Google**

Inicia o fluxo OAuth para obter permissão do usuário.

---

**Coletar todos os vídeos da playlist especificada**

Percorre a playlist e coleta os IDs dos vídeos.

---

**Listar IDs de vídeos, views e outras estatísticas**

Agrega e exibe métricas relevantes de cada vídeo.

---

**Exportar resultados (opcional)**

Opções para exibir no terminal ou exportar para CSV/Google Sheets.

---

**Boas práticas implementadas**

- Autenticação segura usando OAuth 2.0
- Requisições em lote para otimizar chamadas à API
- Uso de list comprehensions e `.join()` para processamento eficiente
- Estrutura modular e fácil de estender
- `.gitignore` configurado para não expor credenciais

## Ideias de expansão

---

**Exportar dados para CSV ou Google Sheets**

Adicionar opções nativas de exportação para integração com planilhas.

---

**Criar dashboards interativos com Plotly ou Dash**

Visualizações interativas e relatórios em tempo real.

---

**Automatizar alertas de crescimento**

Alertas por e-mail/Slack quando vídeos apresentarem crescimento significativo.

---

**Integração com serviços de BI (Power BI, Tableau)**

Conectar saídas a ferramentas de BI para relatórios corporativos.

