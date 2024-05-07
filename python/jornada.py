import pyautogui
import time
pyautogui.PAUSE = 1

## Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

## Entrar no site do sistemas
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

## Fazer login
pyautogui.click(x=526, y=592)
pyautogui.write("phnikidefaria3@gmail.com")

pyautogui.press("tab") ## passou para o campo de senha
pyautogui.write("Ph114015") ## senha

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#importar a base de dados com o pandas
import pandas as pd


tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"]) # quando vc quiser pegar uma informção da tabela
    #clicar no campo do código do produto
    pyautogui.click(x=576, y=419)
    # preencher o codigo
    pyautogui.write(codigo)
    # passar para o proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # obs
    obs= str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write
    # passar para o proximo campo
    pyautogui.press("tab")
    # apertar o botão
    pyautogui.press("enter")
    # scroll para subir para o início da tela
    pyautogui.scroll(5000)





















# import time
# time.sleep(5)
# print(pyautogui.position()) para saber a posição do mouse para poder clicar no lugar certo

# pyautogui.click = clicar com o mouse
# pyautogui.write = escrever um texto
# pyautogui. press = pressionar a tecla do teclado
# pyautogui.hotkey = aperta um conjunto de teclas (ctrl c, ctrl v)
  


