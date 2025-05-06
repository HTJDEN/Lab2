def calculate_bmi(height, weight):

    print("height " , height)
    print("weight " + str(weight))
    bmi = weight/(height**2)
    print("your bmi is", bmi)
    return bmi

def classify_bmi(bmi):
    if(bmi < 18.5):
        # print("you are underweight")
        return 1
    elif (bmi >= 18.5 and bmi <=25):
        # print("you are acceptable weight")
        return 0
    else:
        # print("you are overweight")
    return -1

def app():
    output = calculate_bmi (1.7 , 60)
    classify_bmi(output)
    return 

if __name__ == "__main__":
    app()










