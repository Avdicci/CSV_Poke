import PySimpleGUI as sg
from pokemon import get_pokemon
sg.theme('DarkBrown4')

layout_1 = [ 
    [sg.Text('What pokemon do you want?')],      
    [sg.InputText(key='pokemon_name')],
    [sg.Button('Search in Pokedex', key='search_in_pokedex')]
]

layout_2 = [[sg.Text('Names: xxx', key='name')],
    [sg.Text('Attack: xxx', key="attack")],
    [sg.Text('HP: xxx', key="hp")],
    [sg.Text('DEF: xxx', key="defense")],
    [sg.Text('Speed: xxx', key="speed")],
    [sg.Cancel()]]

# Create the window
window_1 = sg.Window('Home', layout_1)
window_2 = sg.Window('Pokedex', layout_2, finalize=True)
window_2.hide()

while True:
    event, values = window_1.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'search_in_pokedex':
        window_1.hide()
        
        # Takes input from the user
        input_text = values['pokemon_name']    
        
        # Get the pokemon data    
        pokemon = get_pokemon(input_text)
        
        # If the pokemon is not found, show a popup and unhide window 1
        if pokemon == None:
            sg.popup('Pokemon not found')
            window_1.un_hide()
            continue
        
        # Update the text in the window
        window_2['name'].update(f'Name: {pokemon["name"]}')
        window_2['attack'].update(f'Attack: {pokemon["attack"]}')
        window_2['hp'].update(f'HP: {pokemon["hp"]}')
        window_2['defense'].update(f'Defense: {pokemon["defense"]}')
        window_2['speed'].update(f'Speed: {pokemon["speed"]}')
    
        
        # Unhide window 2 which now contains the data
        window_2.un_hide()
    
    # window 2 events
    event, values = window_2.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window_2.hide()
        window_1.un_hide()
    
        
window_1.close()
window_2.close()

