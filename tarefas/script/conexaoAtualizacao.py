from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

# Definir o modelo das tabelas
Base = declarative_base()

class Atividade(Base):
    __tablename__ = 'atividade'

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    projeto = Column(Integer, ForeignKey('projeto.codigo'))  # Correção aqui
    data_inicio = Column(Date)
    data_fim = Column(Date)
    projeto_relacionado = relationship("Projeto", back_populates="atividades")  # Relacionamento

class Departamento(Base):
    __tablename__ = 'departamento'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String(100))
    sigla = Column(String(10), unique=True)
    descricao = Column(String(250))
    gerente = Column(Integer, ForeignKey('funcionario.codigo'))  # Correção aqui
    projetos = relationship('Projeto', back_populates='departamento')

class Funcionario(Base):
    __tablename__ = 'funcionario'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String(150))
    sexo = Column(String(1))
    dt_nasc = Column(Date)
    salario = Column(Integer)
    supervisor = Column(Integer, ForeignKey('funcionario.codigo'))  # Correção aqui
    depto = Column(Integer, ForeignKey('departamento.codigo'))
    projetos_responsavel = relationship('Projeto', back_populates='responsavel_projeto')

class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True)
    descricao = Column(String(250))
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))  # Correção aqui
    depto = Column(Integer, ForeignKey('departamento.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    atividades = relationship("Atividade", back_populates="projeto_relacionado")  # Relacionamento
    departamento = relationship('Departamento', back_populates='projetos')
    responsavel_projeto = relationship('Funcionario', back_populates='projetos_responsavel')

# Conectar ao banco de dados PostgreSQL
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Solicitar o ID do projeto ao usuário
    id_projeto = input("Digite o ID do projeto que deseja atualizar: ")

    # Converter o ID do projeto para inteiro
    id_projeto = int(id_projeto)

    # Solicitar o nome do novo responsável ao usuário
    novo_responsavel = input("Digite o nome do novo responsável: ")

    # Consultar o projeto pelo ID
    projeto = session.query(Projeto).filter_by(codigo=id_projeto).first()

    # Verificar se o projeto foi encontrado
    if projeto:
        # Atualizar o responsável pelo projeto
        projeto.responsavel = novo_responsavel
        session.commit()
        print("Projeto atualizado com sucesso!")
    else:
        print("Projeto não encontrado.")

except ValueError:
    print("O ID do projeto deve ser um número inteiro.")
except Exception as e:
    session.rollback()
    print("Ocorreu um erro durante a atualização:", e)

finally:
    # Fechar a sessão ao final
    session.close()