import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI

# Carrega as variáveis de ambiente a partir de um arquivo .env
load_dotenv()

# Obtém a chave da API do OpenAI a partir das variáveis de ambiente
openai_api_key = os.getenv("OPENAI_API_KEY")


# Função principal para fazer a análise dos dados com base em linguagem natural
def chat_csv(df, prompt):
    # Inicializa o modelo GPT-4 do OpenAI com a chave de API fornecida
    llm = OpenAI(api_token=openai_api_key, model="gpt-4")
    
    # Instancia o PandasAI, que permite usar LLMs para interagir com DataFrames
    pandas_ai = PandasAI(llm)
    
    # Executa a análise com base no prompt fornecido pelo usuário
    resultado = pandas_ai.run(df, prompt=prompt)
    
    # Exibe o resultado no console (útil para debug)
    print(resultado)
    
    # Retorna o resultado para ser exibido na interface
    return resultado

# Configura o layout da página como "wide", para usar a largura total da tela
st.set_page_config(layout='wide')

# Define o título da aplicação
st.title("Conversão de Linguagem Natural em Análise de Dados com LLMs")

# Cria um campo para o upload de arquivos CSV
input_csv = st.file_uploader("Faça o Upload do seu Dataset em formato CSV", type=['csv'])

# Verifica se um arquivo foi carregado
if input_csv is not None:

    # Cria duas colunas lado a lado para organizar a interface
    col1, col2 = st.columns([1, 1])

    # Coluna 1: Exibe o CSV carregado
    with col1:
        st.info("CSV Carregado com Sucesso")
        
        # Lê o arquivo CSV usando Pandas
        data = pd.read_csv(input_csv)
        
        # Exibe o DataFrame carregado em formato de tabela interativa
        st.dataframe(data, use_container_width=True)

    # Coluna 2: Área de interação com o usuário
    with col2:
        st.info("Interaja com o Dataset")
        
        # Campo para o usuário digitar uma pergunta em linguagem natural
        input_text = st.text_area("Digite sua pergunta")

        # Verifica se o usuário inseriu uma pergunta
        if input_text is not None:
            # Botão para enviar a pergunta e iniciar o processamento
            if st.button("Enviar"):
                st.info("Sua pergunta: " + input_text)
                
                # Chama a função para processar a pergunta e analisar o CSV
                result = chat_csv(data, input_text)
                
                # Exibe o resultado final para o usuário
                st.success(result)
