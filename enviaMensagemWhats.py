import pywhatkit
import pyautogui
import time

def enviar_mensagem_whatsapp(numeros, mensagem):
    for numero in numeros:
        pywhatkit.sendwhatmsg_instantly(f"+{numero}", mensagem, wait_time=20)  # Envia a mensagem imediatamente com um tempo de espera de 20 segundos entre cada mensagem
        time.sleep(10)  # Aguarda 10 segundos após abrir o WhatsApp Web
        pyautogui.press('enter')  # Simula a tecla Enter para enviar a mensagem

# Lista de números de telefone e mensagem padrão

numeros = ['5519111111111', '5511922223344']  # Substitua pelos números de telefone
mensagem = '''  Sua mensagem aqui
                Sua mensagem aqui
                Sua mensagem aqui'''  # Mensagem que deseja enviar

enviar_mensagem_whatsapp(numeros, mensagem)
