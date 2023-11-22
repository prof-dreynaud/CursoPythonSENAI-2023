import tkinter as tk

def saudacao():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    saudacao_label.config(text=f"Seja muito bem-vindo(a), {nome} {sobrenome}!")

janela = tk.Tk()
janela.title("PROGRAMA SAUDAÇÃO!!")

label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

label_sobrenome = tk.Label(janela, text="Digite seu sobrenome: ")
label_sobrenome.pack()

entry_sobrenome = tk.Entry(janela)
entry_sobrenome.pack()

botao_saudacao = tk.Button(janela, text="Saudação", command=saudacao)
botao_saudacao.pack()

saudacao_label = tk.Label(janela, text="")
saudacao_label.pack()

janela.mainloop()