

if __name__ == "__main__" :

    food = ['rice', 'beans']
    print(food)

    food.append('broccoli')
    print(food)

    food_extend = ['bread', 'pizza']
    food.extend(food_extend)
    print(food)
    
    print(food[0:2])

    print(food[len(food) - 1])

    breakfast_list= 'eggs,fruit,orange juice'
    breakfast = breakfast_list.split (',')
    print(breakfast)

    print(len(breakfast))

    float_point = 0.0
    fp_list = []
    while float_point != "stop" :
        float_point = input("Please enter a floating point number, or enter stop: ")
        if float_point != "stop" :
            fp_list.append(float(float_point))
    print(min(fp_list))
    print(max(fp_list))
    print(sum(fp_list) / len(fp_list))







    

