while True:
  x=int(input("Type your math score: "))
  y=int(input("Type your LA score: "))
  z=int(input("Type your spanish score: "))

  xyz=x+y+z
  avarage=xyz/3
  print("Your avarage score is",avarage)

  if (avarage<=5):
    print("You're failing")

  if (avarage>5):
    print("You're passing")

  if (avarage>=9):
    print("Congratulations, you have a great score, take this as a reward: https://www.google.com.mx/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiVkpGKnM31AhUvmmoFHTvEB3kQyCl6BAgFEAM&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&usg=AOvVaw0aHtehaphMhOCAkCydRLZU")