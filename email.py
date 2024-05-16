import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def tarefa_consulta():
    try:
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()

        # Executar consulta no banco de dados
        cursor.execute('SELECT * FROM tabela_desejada')
        resultados = cursor.fetchall()

        mensagem_notificacao = "Seus pedidos a serem realizados"
        for resultado in resultados:

            mensagem_notificacao += f"Resultado: {resultado}\n"

        if mensagem_notificacao:
            tarefa_email(mensagem_notificacao) # type: ignore

        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao executar a tarefa de consulta: {e}")

# Configurações do email
email_de = 'matheuslopec@outlook.com'
senha = 'matheusLOP@45'
email_para = 'matheuslopec@gmail.com'
assunto = 'fornecedor'
corpo_email = 'andrezão é o batman'

# Função para enviar o email
def tarefa_email():
    msg = MIMEMultipart()
    msg['From'] = email_de
    msg['To'] = email_para
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo_email, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587)  # Porta 587 para TLS
    server.starttls()
    server.login(email_de, senha)
    server.sendmail(email_de, email_para, msg.as_string())
    server.quit()

    try:
        print("Email envial com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


def tarefa_verificar():
    try:
        print("Pedido processado com sucesso!")
    except Exception as e:
        print(f"Erro ao executar a tarefa: {e}")

scheduler = BlockingScheduler()
scheduler.add_job(tarefa_consulta, 'cron', day_of_week='wed', hour=22, minute=26)
scheduler.add_job(tarefa_email, 'cron', day_of_week='wed', hour=22, minute=27)
scheduler.add_job(tarefa_verificar, 'cron', day_of_week='wed', hour=22, minute=28)

scheduler.start()