
[Link para o script em c++](https://github.com/Luisf66/Projeto-e-Administra-o-de-Banco-de-Dados/tree/main/tarefas/script)

# Resumo sobre ODBC
ODBC (Open Database Connectivity) é uma API (Interface de Programação de Aplicações) padrão para acessar bancos de dados relacionais a partir de diversas linguagens de programação, incluindo C++. O ODBC permite que aplicativos se comuniquem com bancos de dados usando uma interface comum, independentemente do sistema de gerenciamento de banco de dados (SGBD) subjacente.

Em C++, para utilizar ODBC, geralmente você segue os seguintes passos:

- Inclua os cabeçalhos necessários para ODBC em seu código.
- Configure uma conexão com o banco de dados utilizando funções específicas do ODBC, como SQLConnect.
- Prepare e execute consultas SQL usando funções como SQLPrepare e SQLExecute.
- Recupere os resultados das consultas usando funções como SQLFetch e SQLGetData.
- Libere recursos alocados usando funções como SQLFreeStmt e SQLFreeHandle.
- Gerencie erros e exceções durante todo o processo de interação com o banco de dados usando funções de tratamento de erros do ODBC.

O ODBC fornece uma camada de abstração que permite que os aplicativos sejam independentes do banco de dados subjacente, facilitando a portabilidade do código entre diferentes SGBDs. Isso é possível porque os drivers ODBC fornecem uma interface consistente para o acesso aos dados, independentemente do SGBD específico utilizado.

Na atividade foi utilizado o pqxx que se trata de uma poderosa biblioteca C++ para acessar bancos de dados PostgreSQL. Ele fornece uma interface simples e eficiente para interagir com bancos de dados PostgreSQL diretamente de programas C++.

# Resumo sobre ORM


