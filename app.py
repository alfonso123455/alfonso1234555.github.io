import streamlit as st
import random 
import requests

st.set_page_config (
    page_title="Pokemons",
    layout="centered"
)

def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f" https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()
        else: 
            return None
    except:
        return None
    

def get_random_pokemon():
    random_id = random.randint(1, 1000)
    return get_pokemon_data (str(random_id))

st.title (" Pokemon list")
st.markdown("Basic information from pokemons")

col1, col2 = st.columns([5,1])

with col1:
    pokemon_name = st.text_input("Write a name of a Pokemon:", "")
    
    with col2: 
        button = st.button (" Here for Pokemon!")
        
        pokemon_data = None
    if pokemon_name:
        pokemon_data = get_pokemon_data(pokemon_name)
    elif button:
        pokemon_data = get_random_pokemon()
        
    if pokemon_data:
        
        img_col, info_col = st.columns([1, 1])
    
    with img_col:
        
        st.image(
            pokemon_data["sprites"]["other"]["official-artwork"]["front_default"],
            caption=f"#{pokemon_data['id']} {pokemon_data['name'].title}",
            use_container_width=True
        )
        
with info_col:
    
    st.header("Information of the pokemon!")
    st.write(f"Height:  {pokemon_data['height']}")
    st.write(f"Weight: {pokemon_data['weight']}")
    
    st.subheader("Type")
    types = [type["type"]["name"] for type in pokemon_data["types"]]
    for type in types:
        st.write(f"{type.title()}")        
        


    
    