import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para calcular a área
def calcular_area():
    formas = formas.get()
    valores = float(valores.get())
    valores2 = float(valores2.get())

    if formas == 'quadrado':
        area = valores ** 2
    elif formas == 'retângulo':
        area = valores * valores2
    elif formas == 'círculo':
        area = 3.14159 * valores ** 2
    elif formas == 'triângulo':
        area = (valores * valores2) / 2
    else:
        messagebox.showerror('Erro', 'Selecione uma forma geométrica')
        return

    messagebox.showinfo('Resultado', f'A área do {formas} é {area}')


# Criando a janela principal
janela = tk.Tk()
janela.title('Área de Formas Geométricas')

# Criando os widgets
frame = ttk.Frame(janela, padding=(20, 10, 20, 10))
frame.pack(fill=tk.BOTH, expand=True)

formas = tk.StringVar()
valores = tk.StringVar()
valores2 = tk.StringVar()

label_formas = ttk.Label(frame, text='Forma geométrica:')
label_formas.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
combo_formas = ttk.Combobox(frame, textvariable=formas, values=('quadrado', 'retângulo', 'círculo', 'triângulo'))
combo_formas.grid(row=0, column=1, padx=(0, 10), pady=(0, 10))

label_valores = ttk.Label(frame, text='Valor:')
label_valores.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
entry_valores = ttk.Entry(frame, textvariable=valores)
entry_valores.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

label_valores2 = ttk.Label(frame, text='Valor 2:')
label_valores2.grid(row=2, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)
entry_valores2 = ttk.Entry(frame, textvariable=valores2)
entry_valores2.grid(row=2, column=1, padx=(0, 10), pady=(0, 10))

button_calcular = ttk.Button(frame, text='Calcular Área', command=calcular_area)
button_calcular.grid(row=3, column=0, columnspan=2, pady=(0, 10))

# Iniciando o loop principal
janela.mainloop()