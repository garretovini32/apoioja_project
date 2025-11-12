# 🐊 ApoioJá — Plataforma de Apoio e Denúncias Comunitárias

O **ApoioJá** é uma aplicação web desenvolvida em **Flask (Python)** que permite registrar e acompanhar denúncias comunitárias de forma simples e acessível.  
O projeto foi criado com o objetivo de promover acolhimento e ação rápida frente a situações de vulnerabilidade, representado pela mascote **Pereira, o jacaré acolhedor 🐊💙**.

---

## 🚀 Funcionalidades Principais

- 📝 **Cadastro de denúncias** (categoria, localização e descrição)
- 📅 **Registro com data e hora automáticas**
- 💾 **Banco de dados SQLite integrado**
- 🎨 **Interface web intuitiva e acolhedora**
- 🖼️ **Banner personalizado com o jacaré Pereira**
- 🧩 **Arquitetura modular** (Blueprints e organização por pastas)
- 🧠 **Pronto para deploy no Render.com**

---

## 🧱 Estrutura do Projeto

´´´
apoioja_project/
│
├── app/
│ ├── static/ # Arquivos estáticos (CSS, imagens, JS)
│ │ └── apoioja_banner.png
│ ├── templates/ # Páginas HTML (index, denúncia, etc)
│ ├── models.py # Modelos do banco de dados
│ ├── routes.py # Rotas e endpoints da aplicação
│ ├── init.py # Criação e configuração do app Flask
│
├── tests/ # Testes automáticos (exemplo em test_api.py)
├── venv/ # Ambiente virtual (ignorado no Git)
├── run.py # Ponto de entrada para rodar o app
├── app.db # Banco SQLite (ignorado no Git)
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
´´´


---

## ⚙️ Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/garretovini32/apoioja_project.git
   cd apoioja_project

python -m venv venv
venv\Scripts\activate


pip install -r requirements.txt


python run.py


http://127.0.0.1:5000/


📦 Tecnologias Utilizadas

Python 3.12+

Flask

SQLite

HTML / CSS / Jinja2

Render.com (deploy futuro)

🧑‍💻 Autores

| Integrante          | RA    | Função                                       |
| ------------------- | ----- | -------------------------------------------- |
| Victor Cardoso      | 86433 | Backend / Estrutura Flask                    |
| Vinicius Leite      | 76199 | Frontend / Integração de templates           |
| Vinicius Garreto    | 98284 | Gerenciamento do repositório e deploy        |
| Rodrigo Bittencourt | 70182 | Modelagem de dados                           |
| Kleber Santana      | 70182 | Design e conteúdo visual                     |
