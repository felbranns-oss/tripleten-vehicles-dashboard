# Análise Exploratória de Anúncios de Veículos (EUA)

Aplicação web interativa para análise exploratória de anúncios de vendas de veículos nos Estados Unidos, desenvolvida como projeto da Sprint 5 do curso de Analista de Dados da TripleTen.

## O que o aplicativo faz

O aplicativo, construído com **Streamlit** e **Plotly Express**, permite explorar de forma interativa o conjunto de dados `vehicles_us.csv` (anúncios de venda de carros nos EUA). A partir da interface, é possível:

- Visualizar um **histograma** da quilometragem (`odometer`) dos veículos anunciados
- Gerar um **gráfico de dispersão** relacionando quilometragem (`odometer`) e preço (`price`)
- Consultar, opcionalmente, a **distribuição de preços por tipo de veículo**

Os gráficos são interativos: é possível dar zoom, passar o cursor para ver valores e filtrar faixas de interesse.

A análise exploratória prévia que fundamenta o aplicativo está no notebook `notebooks/EDA.ipynb`.

## Como executar localmente

Pré-requisitos: Python 3 e `pip`.

```bash
# 1. Clone o repositório e entre na pasta do projeto
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>

# 2. Crie e ative um ambiente virtual
python3 -m venv vehicles_env
source vehicles_env/bin/activate        # no Windows: vehicles_env\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o aplicativo Streamlit
streamlit run app.py
```

O aplicativo será aberto no navegador (em geral, em `http://localhost:8501`). Use os botões da página para gerar o histograma e o gráfico de dispersão.

## Aplicação no ar (Render)

Após o deploy no Render, o aplicativo ficará disponível em:

```
https://tripleten-vehicles-dashboard-uq38.onrender.com
```

O aplicativo está publicado no Render e pode ser acessado pelo endereço acima.

## Estrutura do projeto

```
.
├── app.py                 # Aplicativo web Streamlit
├── vehicles_us.csv        # Conjunto de dados de anúncios de veículos
├── requirements.txt       # Dependências do projeto
├── README.md              # Este arquivo
├── .gitignore
├── .streamlit/
│   └── config.toml        # Configuração do Streamlit (porta 10000 no Render)
└── notebooks/
    └── EDA.ipynb          # Análise exploratória dos dados
```
