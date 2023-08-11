import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do remetente
email_de = 'listjuansantana@gmail.com'
senha = '7860644a'

# Configurações do destinatário
email_para = 'listjuansantanao@example.com'

# Configurações do servidor SMTP do Gmail
smtp_servidor = 'smtp.gmail.com'
smtp_porta = 587  # Para TLS

# Criação do objeto de mensagem
mensagem = MIMEMultipart()
mensagem['From'] = email_de
mensagem['To'] = email_para
mensagem['Subject'] = 'Testando Jenkins'

# Corpo do email
corpo = 'Este é um exemplo de e-mail enviado usando Python e Jenkins.'
mensagem.attach(MIMEText(corpo, 'plain'))

# Conexão com o servidor SMTP
server = smtplib.SMTP(smtp_servidor, smtp_porta)
server.starttls()

# Login com as credenciais do remetente
server.login(email_de, senha)

# Envio do email
texto_do_email = mensagem.as_string()
server.sendmail(email_de, email_para, texto_do_email)

# Encerramento da conexão com o servidor
server.quit()

print('Email enviado com sucesso!')
