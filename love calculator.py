print("welcome to love calculator")
boy_name = str(input("enter your name\n "))
girl_name = str(input("enter his/her name\n "))
low_boy_name = boy_name.lower()
low_girl_name = girl_name.lower()
count_boy_name = low_boy_name.count('t') + low_boy_name.count('r') + low_boy_name.count('u') + low_boy_name.count('e') 
count_boy_name1 = low_boy_name.count('l') + low_boy_name.count('o') + low_boy_name.count('v') + low_boy_name.count('e')
count_girl_name = low_girl_name.count('t') + low_girl_name.count('r') + low_girl_name.count('u') + low_girl_name.count('e') 
count_girl_name1 = low_girl_name.count('l') + low_girl_name.count('o') + low_girl_name.count('v') + low_girl_name.count('e')
sum_count = count_boy_name + count_girl_name
sum_count1 = count_boy_name1 + count_girl_name1

#we want to concatenate

a = sum_count
b = sum_count1

love_score = int(str(a) + str(b))
print(f"your love score is: {love_score} " )

if love_score < 10 or love_score > 90:
    print(f"you score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"you score is {love_score}, You both will do good as partners")
else:
    print(f"you score is {love_score}, You both will do good as partners")

