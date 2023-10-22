year=int(input("enter the year"))
if(year%400==0)and(year%100==0):
  print(year,"This is leep year")
elif(year%400==0)and(year%100!=0):
  print(year,"This is leep year")
else:
  print(year,"This is not a leep yera")
