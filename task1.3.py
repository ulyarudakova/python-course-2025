text = "Привет)"
count1 = 0
count2 = 0

for i in text:
    if i == ")":
        count1 += 1
    elif i == "(":
        count2 += 1

if count1 > count2:
   print("Любит!")
elif count1 == count2:
    print("Ну хз...")
else:
    print("Не любит!")