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
    # Solicitar os valores para inserção da atividade ao usuário
    descricao = input("Insira a descrição da atividade: ")
    projeto_codigo = input("Insira o código do projeto da atividade: ")
    data_inicio = input("Insira a data de início da atividade (formato: AAAA-MM-DD): ")
    data_fim = input("Insira a data de término da atividade (formato: AAAA-MM-DD): ")

    # Converter as datas para o tipo datetime
    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

    # Criar uma nova instância de Atividade com os valores fornecidos
    nova_atividade = Atividade(descricao=descricao, projeto=projeto_codigo, data_inicio=data_inicio, data_fim=data_fim)

    # Adicionar a nova atividade à sessão e fazer o commit para salvar no banco de dados
    session.add(nova_atividade)
    session.commit()

    print("Atividade inserida com sucesso! Código da atividade:", nova_atividade.codigo)

except ValueError:
    print("Erro: Certifique-se de inserir datas no formato correto (AAAA-MM-DD)!")
except Exception as e:
    session.rollback()
    print("Ocorreu um erro durante a inserção da atividade:", e)

finally:
    # Fechar a sessão ao final
    session.close()