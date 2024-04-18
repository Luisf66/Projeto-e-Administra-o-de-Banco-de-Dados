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
    projetos_responsavel = relationship('Projeto', back_populates='responsavel_projeto')  # Correção aqui

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
    # Realizar a consulta
    projetos_atividades = session.query(Projeto, Atividade).join(Atividade).all()

    # Exibir o resultado da consulta
    for projeto, atividade in projetos_atividades:
        print(f"Projeto: {projeto.nome}, Descrição: {projeto.descricao}")
        print(f"Atividade: {atividade.descricao}, Data de Início: {atividade.data_inicio}, Data de Término: {atividade.data_fim}")
        print()

except Exception as e:
    print("Ocorreu um erro durante a consulta:", e)

finally:
    # Fechar a sessão ao final
    session.close()
