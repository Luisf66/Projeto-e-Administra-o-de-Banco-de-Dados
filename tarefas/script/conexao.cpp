#include <iostream>
#include <pqxx/pqxx>

int main() {
    try {
        // Estabelecer conexão com o banco de dados
        pqxx::connection conn("dbname=postgres user=postgres password=postgres hostaddr=127.0.0.1 port=5432");

        if (conn.is_open()) {
            std::cout << "Conexão bem-sucedida!" << std::endl;
        } else {
            std::cout << "Erro ao conectar." << std::endl;
            return 1;
        }

        // Executar consulta SQL
        pqxx::work txn(conn);
        pqxx::result result = txn.exec("SELECT * FROM projeto");

        // Exibir resultados
        for (const auto &row : result) {
            for (const auto &field : row) {
                std::cout << field.c_str() << " ";
            }
            std::cout << std::endl;
        }

        // Commit e fechamento da transação
        txn.commit();

        // Fechar conexão
        conn.disconnect();
        std::cout << "Conexão encerrada." << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Erro ao conectar ao PostgreSQL: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
