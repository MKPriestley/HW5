

if __name__ == "__main__" :

    pokemon = ('picachu', 'charmander', 'bulbasaur')

    print(pokemon[1])

    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]
    #print(starter1)
    #print(starter2)
    #print(starter3)

    my_name = "Miranda"
    my_tuple = tuple(my_name)
    print(my_tuple)

    print('i' in my_tuple)
   
    for i in range (2, 11) :
        print(i)

    integers = ('2', '3', '4', '5', '6', '7', '8', '9', '10')
    i = 0
    while i < len(integers) :
        print(integers[i])
        i += 1

string = 'This is a simple string'
for letter in string :
    print(letter)
    
repeat = ('this', 'is', 'a', 'simple', 'string')
for word in repeat :
    for i in range(3) :
        print(word)
