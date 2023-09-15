from datetime import date
import PySimpleGUI as sg

dia_semana = date.today().weekday()
semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

# if dia_semana <= 5:
#     print(f"Tenha uma boa {semana[dia_semana]}-feira")
# else:
#     print(f"Tenha um bom {semana[dia_semana]}")


#Mensagem na interface
layout = [ [sg.Text(f"Tenha uma boa {semana[dia_semana]}-feira")],
           [sg.Button("Obrigado(a)", button_type = 7)]]

#cria a janela
window = sg.Window('Hello', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print('You entered', values [0])
    
window.close()

