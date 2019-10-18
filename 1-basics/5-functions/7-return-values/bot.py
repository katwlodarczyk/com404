def sum_weights(bops_weight, beeps_weight):
    total_weight= bops_weight + beeps_weight
    return total_weight

def calc_avg_weight(bops_weight, beeps_weight):
    sum_weights(bops_weight, beeps_weight)
    avg_weights = sum_weights(bops_weight, beeps_weight) / 2  
    return avg_weights

def run():
    print("Please enter weight of Bop")
    bops_weight= int(input())
    print("Please enter weight of Beep")
    beeps_weight = int(input())
    print("Shoul I calculate sum or average")
    word = str(input())
    if (word == "sum"):
        answer = sum_weights(bops_weight, beeps_weight)
        print(answer)
    else: 
        answer = calc_avg_weight(bops_weight, beeps_weight)
        print(answer)
run()