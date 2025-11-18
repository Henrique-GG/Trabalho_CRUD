1. CRUD de Cursos com Python (CustomTkinter + MySQL)

2. Descrição do Projeto

Aplicação de desktop (GUI) desenvolvida em Python para a disciplina de Banco de Dados. O objetivo é demonstrar as quatro operações fundamentais de persistência de dados (CRUD) conectadas a um banco de dados MySQL.

A aplicação permite ao usuário gerenciar um cadastro simples de cursos.

3. Screenshot da Aplicação

<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/38fd1684-46ff-464e-a36f-4ad2913bd30a" />


4. Funcionalidades (CRUD)

A aplicação implementa o ciclo CRUD completo:

[C]reate (Adicionar): Insere um novo nome de curso no banco de dados.

[R]ead (Ler): Carrega e exibe todos os cursos cadastrados em uma tabela (Treeview).

[U]pdate (Atualizar): Permite selecionar um curso na tabela, alterar seu nome e salvar a modificação.

[D]elete (Excluir): Permite selecionar um curso na tabela e removê-lo permanentemente do banco.

5. Tecnologias Utilizadas

Python 3.x: Linguagem principal da aplicação.

CustomTkinter: Biblioteca para criação da interface gráfica (GUI) moderna.

MySQL Connector/Python: Biblioteca oficial para conectar o Python ao banco de dados MySQL.

MySQL Server: Sistema de Gerenciamento de Banco de Dados.

6. Pré-requisitos

Antes de começar, você precisará ter os seguintes softwares instalados:

Python 3.10+

Um servidor MySQL (Ex: XAMPP, WAMP ou [suspicious link removed])

Um cliente de banco de dados (Ex: MySQL Workbench ou DBeaver)

7. Instalação e Configuração

Siga os passos abaixo para executar o projeto:

1. Clonar o Repositório

git clone https://github.com/Henrique-GG/Trabalho_CRUD
cd seu-repositorio


2. Configurar o Banco de Dados

Abra seu cliente MySQL (ex: MySQL Workbench).

Execute o script SQL fornecido no arquivo script.sql para criar o banco e a tabela.

-- Conteúdo de script.sql
CREATE DATABASE crud_gui;
USE crud_gui;

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);


3. Criar um Ambiente Virtual (Recomendado)

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


4. Instalar as Dependências

O arquivo requirements.txt contém todas as bibliotecas necessárias.

pip install -r requirements.txt


5. Configurar a Conexão

Ponto mais importante: Você precisa atualizar o arquivo app.py com suas credenciais do MySQL.

Abra o app.py e edite a função conectar():

# ...
# =============================
# CONEXÃO COM O BANCO
# =============================
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # <-- MUDE AQUI (seu usuário)
        password="Henrique1109",  # <-- MUDE AQUI (sua senha)
        database="crud_gui"
    )
# ...


8. Como Executar a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, basta executar o script app.py:

python app.py


A janela da aplicação deverá abrir, e os dados do banco (se houver) serão carregados.

9. Estrutura dos Arquivos

.
├── app.py               # Arquivo principal: lógica do CRUD e interface gráfica
├── cor.json             # Tema de cores customizado para o CustomTkinter
├── requirements.txt     # Lista de dependências Python (pip)
├── script.sql           # Script de criação do banco de dados e tabela
└── README.md            # Este arquivo


10. Autor

Desenvolvido por [Henrique Guimarães Gonçalves, Lucas Goulart de Queiroz, Miguel Marques]
