x = 0
for index in range(5,10,2):
   x += 10
   print("the value of x is {0}".format(x))
   


students_name =["jessy", "jake", "mark", "john", "lilly"]


for name in students_name:
    if name == "mark":
       print("found him "  +  name)
       break
    print("currently testing "  +  name)


for name in students_name:
   if name == "john":
      continue
      print("found him "  +  name)
   print("currently testing "  +  name)


   x = 0
   while x < 10:
      print("the value is {0}".format(x))
      x += 1


   num = 4
   while True:
      if num == 4:
         break
      print("hello")   



