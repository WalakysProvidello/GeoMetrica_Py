import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para calcular a área
def calcular_area():
    formas = combo_formas.get()
    valor1 = float(entry_valor1.get())
    valor2 = float(entry_valor2.get()) if entry_valor2.get() else None

    if formas == 'quadrado':
        area = valor1 ** 2
    elif formas == 'retangulo':
        area = valor1 * valor2
    elif formas == 'circulo':
        area = 3.14159 * valor1 ** 2
    elif formas == 'triangulo':
        area = (valor1 * valor2) / 2
    else:
        messagebox.showerror('Erro', 'Selecione uma forma geométrica')
        return

    resultado_label.config(text=f'Resultado: A área do {formas} é {area}')

# Configuração da janela principal
root = tk.Tk()
root.title('Calculadora de Área')

# Criar widgets
label_formas = ttk.Label(root, text='Selecione a forma:')
combo_formas = ttk.Combobox(root, values=['quadrado', 'retangulo', 'circulo', 'triangulo'])
label_valor1 = ttk.Label(root, text='Digite o valor 1:')
entry_valor1 = ttk.Entry(root)
label_valor2 = ttk.Label(root, text='Digite o valor 2 (opcional):')
entry_valor2 = ttk.Entry(root)
calcular_button = ttk.Button(root, text='Calcular', command=calcular_area)
resultado_label = ttk.Label(root, text='Resultado:')

# Layout dos widgets
label_formas.grid(row=0, column=0, padx=10, pady=5, sticky='w')
combo_formas.grid(row=0, column=1, padx=10, pady=5)
label_valor1.grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_valor1.grid(row=1, column=1, padx=10, pady=5)
label_valor2.grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_valor2.grid(row=2, column=1, padx=10, pady=5)
calcular_button.grid(row=3, column=0, columnspan=2, pady=10)
resultado_label.grid(row=4, column=0, columnspan=2, pady=5)

# Executar o loop da aplicação
root.mainloop()
