'''
    Autor: Iago Magalhães
    Data: 17/12/2024
    Descrição: Código para envio automático de Emails utilizando a lib Secure-SMTPLIB
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    '''
        :param destinatario: email do destinatario
        :param assunto: assunto do email a ser enviado
        :param mensagem: mensagem do email a ser enviado
    '''
    #Configurações do sevirdor de email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = ''
    senha = ''

    #Conteúdo da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    #Adiciona o corpo da mensagem
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        #Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() #Utiliza o TLS para segurança
        server.login(remetente, senha) #Login no servidor SMTP

        #Envia o email
        server.sendmail(remetente, destinatario, msg.as_string())
        print('E-mail eniado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar E-mail: {e}')
    finally:
        server.quit() #Encerra a conexão com o servidor SMTP


#Executando aplicação
enviar_email('', 'Assunto do email', 'Corpo do email')
