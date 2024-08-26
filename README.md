# tcc_pos_ia_pucmg
Repositório do meu TCC do Curso de Pós-Graduação em Inteligência Artificial - PUCMG

---

# Conversão de Linguagem Natural em Operações de Análise de Dados com apoio de Modelos de Inteligência Artificial Generativa

Este repositório contém o código do meu Trabalho de Conclusão de Curso (TCC) da Pós-Graduação em Inteligência Artificial pela PUC-MG.

## Descrição do Projeto

O projeto **Conversão de Linguagem Natural em Operações de Análise de Dados com apoio de Modelos de Inteligência Artificial Generativa** visa facilitar a análise de dados tabulares armazenados em arquivos CSV. A aplicação possibilita que usuários realizem consultas em linguagem natural sobre os dados e obtenham respostas ou insights com base em modelos avançados de inteligência artificial generativa, como o GPT.

## Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/):** Framework para criação de aplicações web interativas e de fácil uso.
- **[Pandas](https://pandas.pydata.org/):** Biblioteca para manipulação e análise de dados.
- **[PandasAI](https://github.com/gventuri/pandas-ai):** Integração entre Pandas e modelos de linguagem natural.
- **[OpenAI API](https://platform.openai.com/):** Interface para acesso a modelos de linguagem avançados como GPT-3.5 e GPT-4.
- **[Python-dotenv](https://pypi.org/project/python-dotenv/):** Gerenciamento de variáveis de ambiente para segurança de dados sensíveis.

## Funcionalidades

- Upload de arquivos CSV.
- Exibição dos dados carregados de forma interativa.
- Interface intuitiva para realizar perguntas em linguagem natural sobre os dados.
- Respostas geradas automaticamente com base na análise do conteúdo do CSV.

## Como Executar a Aplicação

1. Clone o repositório:
   ```bash
   git clone https://github.com/fredcobain/tcc_pos_ia_pucmg.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd tcc_pos_ia_pucmg
   ```
3. Crie um ambiente virtual (recomendado o uso do Anaconda Python, criando um ambiente na versão Python versão 3.10):
   ```bash
   conda create --name PYTHON3_10 python=3.10
   conda activate PYTHON3_10
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API OpenAI:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```
6. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

## Como Usar

1. Faça o upload de um arquivo CSV.
2. Explore os dados na interface interativa.
3. Insira uma pergunta em linguagem natural no campo de texto.
4. Clique no botão "Chat with CSV" para obter a resposta gerada pelo modelo de linguagem.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Streamlit.
- `requirements.txt`: Lista de dependências do projeto.
- `.env.example`: Exemplo do arquivo `.env` com a configuração da chave da API.

---

## Documentos para Download

Nesta seção, você encontrará todos os documentos relevantes para o projeto, incluindo o relatório final, o canvas de análise do software, o caderno de testes, e o dataset utilizado.

### 1. Relatório Final
- **Arquivo PDF:** [Relatório Técnico - Versão Final](https://github.com/fredcobain/tcc_pos_ia_pucmg/blob/main/Relatorio%20T%C3%A9cnico%20-%20Vers%C3%A3o%20Final.pdf)

### 2. Software Analytics Canvas
- **Arquivo PDF:** [Software Analytics Canvas - Versão Final](https://github.com/fredcobain/tcc_pos_ia_pucmg/blob/main/Software-Analtics-Canvas-Final.pdf)

### 3. Caderno de Testes
- **Arquivo Excel:** [Caderno de Testes](https://github.com/fredcobain/tcc_pos_ia_pucmg/blob/main/Caderno%20de%20Testes.xlsx)

### 4. Dataset Utilizado no Trabalho
- **Kaggle:** [IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)

---


