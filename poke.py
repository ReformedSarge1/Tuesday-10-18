from pokeapi import *
from flask import *
import json

app = Flask(__name__)
data = dict()



@app.route('/')
def home():
    return render_template('main.html')

@app.route('/pokedex',methods =['POST','GET'])
def pokedex():
    if request.method == 'POST': 
        sno = int(request.form['sno'])
    else :
        sno = 1
    results = pokes
    if(sno <1):
        return "Enter a valid Value"
    if(sno > 13):
        return "Under Progress"
    
    data = {
    "id" : str(results[sno]['id']),
    "name" : str(results[sno]['name']),
    "type1" : str(results[sno]['type1']),
    "type2" : str(results[sno]['type2']),
    "ability1" : str(results[sno]['ability1']),
    "ability2" : str(results[sno]['ability2']),
    "Hiddenability" : str(results[sno]['Hiddenability']),
    "HP" : str(results[sno]['HP']),
    "Attack" : str(results[sno]['Attack']),
    "Defense" : str(results[sno]['Defense']),
    "SpecialAttack" : str(results[sno]['SpecialAttack']),
    "SpecialDefense" : str(results[sno]['SpecialDefense']),
    "Speed" : str(results[sno]['Speed']),
    "TotalStats" : str(results[sno]['TotalStats']),
    "EvolutionMethod" : str(results[sno]['EvolutionMethod']),
    "EvolutionName" : str(results[sno]['EvolutionName'])
    }
    return render_template('poke.html', data = data)



if __name__ == '__main__': 
    app.run(debug = True) 

pokes = {
1 : {
    "id" : "#001",
    "name" : "Bulbasaur",
    "type1" : "Grass",
    "type2" : "Poison",
    "ability1" : "Overgrow",
    "ability2" : "Overgrow",
    "Hiddenability" : "Chlorophyll",
    "HP" : 45,
    "Attack" : 49,
    "Defense" : 49,
    "SpecialAttack" : 65,
    "SpecialDefense" : 65,
    "Speed" : 45,
    "TotalStats" : 318,
    "EvolutionMethod" : "Level up till 16",
    "EvolutionName" : "Ivysaur"
},
2 : {
    "id" : "#002",
    "name" : "Ivysaur",
    "type1" : "Grass",
    "type2" : "Poison",
    "ability1" : "Overgrow",
    "ability2" : "Overgrow",
    "Hiddenability" : "Chlorophyll",
    "HP" : 60,
    "Attack" : 62,
    "Defense" : 63,
    "SpecialAttack" : 80,
    "SpecialDefense" : 80,
    "Speed" : 60,
    "TotalStats" : 405,
    "EvolutionMethod" : "Level up till 32",
    "EvolutionName" : "Venusaur"
},
3 : {
    "id" : "#003",
    "name" : "Venusaur",
    "type1" : "Grass",
    "type2" : "Poison",
    "ability1" : "Overgrow",
    "ability2" : "Overgrow",
    "Hiddenability" : "Chlorophyll",
    "HP" : 80,
    "Attack" : 82,
    "Defense" : 83,
    "SpecialAttack" : 100,
    "SpecialDefense" : 100,
    "Speed" : 80,
    "TotalStats" : 525,
    "EvolutionMethod" : "Venusaurite",
    "EvolutionName" : "Mega-Venusaur"
},

5 : {
    "id" : "#004",
    "name" : "Charmander",
    "type1" : "Fire",
    "type2" : "Fire",
    "ability1" : "Blaze",
    "ability2" : "Blaze",
    "Hiddenability" : "SolarPower",
    "HP" : 39,
    "Attack" : 52,
    "Defense" : 43,
    "SpecialAttack" : 60,
    "SpecialDefense" : 50,
    "Speed" : 65,
    "TotalStats" : 309,
    "EvolutionMethod" : "Level up till 16",
    "EvolutionName" : "Charmeleon"
}
}