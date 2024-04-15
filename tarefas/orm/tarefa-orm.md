
[Link para o script em c++](https://github.com/Luisf66/Projeto-e-Administra-o-de-Banco-de-Dados/tree/main/tarefas/script)

# Resumo sobre ODBC
ODBC (Open Database Connectivity) é uma API (Interface de Programação de Aplicações) padrão para acessar bancos de dados relacionais a partir de diversas linguagens de programação, incluindo C++. O ODBC permite que aplicativos se comuniquem com bancos de dados usando uma interface comum, independentemente do sistema de gerenciamento de banco de dados (SGBD) subjacente.

Em C++, para utilizar ODBC, geralmente você segue os seguintes passos:

Inclua os cabeçalhos necessários para ODBC em seu código.
Configure uma conexão com o banco de dados utilizando funções específicas do ODBC, como SQLConnect.
Prepare e execute consultas SQL usando funções como SQLPrepare e SQLExecute.
Recupere os resultados das consultas usando funções como SQLFetch e SQLGetData.
Libere recursos alocados usando funções como SQLFreeStmt e SQLFreeHandle.
Gerencie erros e exceções durante todo o processo de interação com o banco de dados usando funções de tratamento de erros do ODBC.
O ODBC fornece uma camada de abstração que permite que os aplicativos sejam independentes do banco de dados subjacente, facilitando a portabilidade do código entre diferentes SGBDs. Isso é possível porque os drivers ODBC fornecem uma interface consistente para o acesso aos dados, independentemente do SGBD específico utilizado.

# Resumo sobre ORM
ORM (Object-Relational Mapping) em C++ é uma técnica que mapeia objetos em um sistema orientado a objetos para tabelas em um banco de dados relacional, simplificando assim a interação entre a aplicação e o banco de dados. Em essência, ele permite que você trabalhe com objetos em seu código, enquanto as operações de leitura e escrita são traduzidas automaticamente para operações de banco de dados.

Alguns pontos importantes sobre ORM em C++:

- Abstração de Banco de Dados: ORM fornece uma camada de abstração sobre o banco de dados, permitindo que os desenvolvedores trabalhem com objetos e classes em vez de lidar diretamente com consultas SQL.

- Mapeamento Objeto-Relacional: ORM mapeia as estruturas de dados do seu código (objetos, classes, etc.) para as tabelas do banco de dados e vice-versa. Isso é feito por meio de configurações ou anotações que descrevem como as entidades do seu sistema se relacionam com as tabelas do banco de dados.

- Operações CRUD Simplificadas: Com ORM, operações básicas de CRUD (Create, Read, Update, Delete) são simplificadas. Por exemplo, em vez de escrever consultas SQL manualmente, você pode chamar métodos em objetos para salvar ou recuperar dados do banco de dados.

- Gerenciamento de Relacionamentos: ORM facilita o gerenciamento de relacionamentos entre objetos e tabelas no banco de dados. Ele permite definir associações entre entidades no código, como relacionamentos um-para-um, um-para-muitos e muitos-para-muitos, e traduz essas associações para relacionamentos de chave estrangeira no banco de dados.

- Performance: Um bom ORM pode otimizar consultas e operações de banco de dados para melhorar o desempenho da aplicação. No entanto, é importante entender como o ORM está traduzindo suas operações de código para consultas SQL e como isso afeta o desempenho geral da aplicação.

Alguns exemplos de frameworks ORM populares em C++ incluem o ODB (Object Database) e o SOCI (Simple Oracle Call Interface). Esses frameworks oferecem diversas funcionalidades para facilitar o desenvolvimento de aplicações que utilizam ORM em C++, ajudando os desenvolvedores a lidar de forma eficiente com o acesso a dados em suas aplicações.

Outro exemplo que foi utilizado é o pqxx que se trata de uma poderosa biblioteca C++ para acessar bancos de dados PostgreSQL. Ele fornece uma interface simples e eficiente para interagir com bancos de dados PostgreSQL diretamente de programas C++.