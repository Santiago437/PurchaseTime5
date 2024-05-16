import sqlite3


def create_connection():
  """ Cria uma conexão com o banco de dados. """
  conn = sqlite3.connect('cadastro.db')
  return conn

def create_table(conn):
  """ Cria a tabela 'usuarios' no banco de dados. """
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                      id INTEGER PRIMARY KEY,
                      nome text,
                      senha text
                  )''')
  conn.commit()

def create_table1(conn):
  """ Cria a tabela 'usuarios' no banco de dados. """
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    produto TEXT,
                    fornecedor TEXT,
                    frequencia INTEGER,
                    quantidade INTEGER,
                    preco REAL,
                    data_inicio DATE,
                    data_fim DATE,
                    usuario_id INTEGER,
                    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                  )''')
  conn.commit()

conn = create_connection()
create_table1(conn)
create_table(conn)
conn.close()
