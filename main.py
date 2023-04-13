print("Hello World")

name = input("Enter your name: ")
time = float(input("Enter the current time: "))

if(time<=12):
  print("Very Good morning ",name)
elif(time<=16):
  print("Very Good afternoon ",name)
elif(time<=20):
  print("Very Good evening ",name)
else:
  print("Very Good night ",name)