#input details
name=input("Enter your name: ")
age=int(input("Enter your age: "))
gender=input("Enter your gender: ")
height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))

#BMI calculation
BMI=round((weight/(height**2))*703,2)

BMIc=""
#BMI category
if(BMI<16):
    BMIc="Severely Underweight"
elif(BMI>=16 and BMI<18.5):
    BMIc="Underweight"
elif(BMI>=18.5 and BMI<25):
    BMIc="Healthy"
elif(BMI>=25 and BMI<30):
    BMIc="Overweight"
else:
    BMIc="Obese"
    
    
#daily calorie consumption cal/100g
food={"Milk":100,"Egg":155,"Rice":130,"Lentils":113,"Vegetable":85,"Meat":143}
calorie={}
totalCal=0;
for i in food.keys():
    val=float(input(f'Enter the Quantity in grams for food {i}: '))
    val=((food.get(i)/100)*val)
    totalCal=round(totalCal+val,2)
    calorie.update({i:val})

#printing if child is undernurished or nurished by checking minimum calorie required
if(age>=0 and age<2):
    if(totalCal<800):
        print(f"Child is Undernourished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 800 ")
    else:
        print(f"Child is nurished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 800")
elif(age>=2 and age<4):
    if(totalCal<1400):
        print(f"Child is Undernourished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 1400")
    else:
        print(f"Child is nurished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 1400")

elif(age>=4 and age<8):
    if(totalCal<1800):
        print(f"Child is Undernourished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 1800")
    else:
        print(f"Child is nurished as your daily calorie intake is {totalCal} and minimum calorie intake for your age group is 1800")
        
else:
    print("You are not a child as your age is more than 8 years")