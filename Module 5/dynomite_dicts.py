

if __name__ == "__main__" :

    pokedex = { }
    list1 = ['Grass', 'Poisen']
    list2 = ['Fire', 'Flying']
    list3 = ['Water']
    pokedex["Venosaur"] = list1
    pokedex["Charizard"] = list2
    pokedex["Blastoise"] = list3
    print(pokedex)

    pokedex.pop("Blastoise")
    print(pokedex)
