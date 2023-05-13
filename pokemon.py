import pandas as pd

# Get pokemon from CSV file based on name
def get_pokemon( name ):
    df = pd.read_csv("Pokemon.CSV")
    chosen_pokemon = df[df["Name"] == name]
    
    # Om den inte hittar pokemon, printa "Pokemon not found"
    if chosen_pokemon.empty:
        print("Pokemon not found")
        return None
        
    return {
        "name": chosen_pokemon["Name"].values[0],
        "hp": chosen_pokemon["HP"].values[0],
        "attack": chosen_pokemon["Attack"].values[0],
        "defense": chosen_pokemon["Defense"].values[0],
        "speed": chosen_pokemon["Speed"].values[0],
    }


# Testing the function
if __name__ == "__main__":
    pokemon = get_pokemon("Pikachu")
    print(f"Pokemon: Pikachu\nHP: {pokemon['name']}\nAttack: {pokemon['attack']}\nDefense: {pokemon['defense']}\nSpeed: {pokemon['speed']}")
    
