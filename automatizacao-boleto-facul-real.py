import pyautogui
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código estiver rodando!")
pyautogui.PAUSE = 0.5

# Abrir o Google Chrome
pyautogui.click(76,743)

# Abrir o aluno online
time.sleep(1)
pyautogui.write("https://aluno.iesb.br/aluno/#login")
pyautogui.press("enter")

# Fazer login no aluno online
time.sleep(2)
pyautogui.press("Tab")
username = "******"
pyautogui.write(username)
password = "******"
pyautogui.press("Tab")
pyautogui.write(password)
pyautogui.press("enter")

# Entrar na aba Boletos
time.sleep(3)
pyautogui.click(31,114)
time.sleep(1)
pyautogui.click(40,695)

# Fazer o download do boleto
time.sleep(3)
pyautogui.click(960,330)

# Fechar o download do boleto
time.sleep(3.5)
pyautogui.click(1342,693)

# Entrar no email
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")

# Enviar o boleto por email
time.sleep(4)
pyautogui.click(98,217)
time.sleep(2)
pyautogui.write("usuario1@gmail.com")
pyautogui.press("tab")
pyautogui.write("usuario2@gmail.com")
pyautogui.press("tab") # seleciona o email
pyautogui.press("tab") # pula pro campo do assunto
time.sleep(0.5)
pyperclip.copy("ATENÇÃO! Boleto da Faculdade")
pyautogui.hotkey('ctrl','v') # escrever o assunto
pyautogui.press("tab") # pular pro corpo do email


texto = """
Usuario1 e Usuario2,
    Segue o boleto referente ao mês atual.
    
     *****LEMBRETE:*****
     Pagar até dia 07 deste mês.
    
    Atenciosamente,
    Robô do Ian
    """
time.sleep(0.5)
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')

# Anexar o arquivo (boleto)
time.sleep(2)
pyautogui.click(853,682) # Clicar em anexar arquivo
time.sleep(2)
pyautogui.click(606,51) # Clicar na barra para escrever
time.sleep(2)
pyautogui.write("downloads")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(273,210) # Clicar no primeiro boleto
pyautogui.click(795,505) # Abrir arquivo
time.sleep(2)
pyautogui.hotkey('ctrl','enter')

pyautogui.alert("O código acabou de rodar. Pode usar o seu computador novamente!")
