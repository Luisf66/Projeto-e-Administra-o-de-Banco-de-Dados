# Projeto e Administracão de Banco de Dados  

- Matrícula: 20220041189 
- Nome: Luis Felipe Dos Santos Tolentino 
- Email: luis.felipe.santos.701@ufrn.edu.br  
- [Link para tarefa-orm.md](https://github.com/Luisf66/Projeto-e-Administra-o-de-Banco-de-Dados/blob/main/tarefas/orm/tarefa-orm.md)

# Uso do código C++

Para utilizar o codigo disponibilizado no diretório script você primeiro deve realizar a instalação do pqxx com o comando 
<code> sudo apt-get install libpqxx-dev</code>

Feito isso você pode verificar a intalação com o comando
<code>dpkg -s libpqxx-dev</code>

Em seguida, inclua o diretório do pqxx no includepath caso esteja na IDE vscode e para compilar corretamente execute os comandos
<code>g++ -o conexao conexao.cpp -lpqxx -lpq</code>
<code>./conexao</code>

### Resolução das questões

O código base realiza a exibição de tudo que esteja na tabela projeto

<code>pqxx::result result = txn.exec("SELECT * FROM projeto");</code>

Para a resolução das questões esse trecho do algoritmo deve ser substituido por respectivamente

- Inserir uma atividade em algum projeto;

<code>pqxx::result result = txn.exec("
    INSERT INTO atividade (codigo,descricao,projeto,data_inicio,data_fim) 
    values ("Valores para inserção")
    ");</code>
- Atualizar o líder de algum projeto;

<code>pqxx::result result = txn.exec("
    UPDATE projeto
    SET responsavel = 'Novo líder'
    WHERE codigo = 'ID do projeto'
    ");</code>
- Listar todos os projetos e suas atividades;

<code>pqxx::result result = txn.exec("
    SELECT * 
FROM projeto pro INNER JOIN atividade ati
ON ati.projeto = pro.codigo
    ");</code>