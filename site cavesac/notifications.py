import smtplib
import os
from email.message import EmailMessage

def send_notification(name, email_vol, phone):
    sender = os.getenv('EMAIL_SENDER')
    password = os.getenv('EMAIL_PASSWORD')
    admin_email = os.getenv('ADMIN_EMAIL')

    if not all([sender, password, admin_email]):
        return False, "Credenciais de e-mail não configuradas no .env"

    # Usando EmailMessage (classe moderna recomendada no Python 3)
    msg = EmailMessage()
    msg.set_content(f"Novo voluntário cadastrado:\n\nNome: {name}\nE-mail: {email_vol}\nTelefone: {phone}")
    
    msg['Subject'] = 'Novo Cadastro de Voluntário - ONG'
    msg['From'] = sender
    msg['To'] = admin_email

    try:
        # Configuração para Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        return True, "E-mail enviado com sucesso."
    except Exception as e:
        return False, f"Falha no envio: {str(e)}"