import random

print("Theme Options:")
print("Music, People, Literature, Science, Math, School, Food, Countries, Yo Mama")

Music =["Pop and rap","Orchestra","Viola","Band"]
People=["Political","Famous","Historical"]
Literature=["Historical","Popular"]
Science=["Chemistry","Anatomy","Physics","Seasons","Plants","Animals","Planets",]
Math=["Shapes","Numbers","Algebra","Equations","Calculus"]
School=["High School","Private School","Public School","Middle School","Elementary School"]
Food=["Desserts","Dinner","Lunch","Breakfast","Junk Food"]
Countries=["CANADA","United States","Urban Countries"]

Political=["Pun1", "Pun2", "Pun3"]


print("Enter a theme: ")
theme = input()
if theme=="Music":
  print ("subthemes:")
  for subtheme in Music:
    print (subtheme)
elif theme=="People":
  print ("subtheme")
  for subtheme in People:
    print (subtheme)
elif theme=="Literature":
  print ("subtheme")
  for subtheme in Literature:
    print (subtheme)
elif theme=="Science":
  print ("subtheme")
  for subtheme in Science:
    print (subtheme)
elif theme=="Math":
  print ("subtheme")
  for subtheme in Math:
    print (subtheme)
elif theme=="School":
  print ("subtheme")
  for subtheme in School:
    print (subtheme)
elif theme=="Food":
  print ("subtheme")
  for subtheme in Food:
    print (subtheme)
elif theme=="Countries":
  print ("subtheme")
  for subtheme in Countries:
    print (subtheme)

print("Enter a subtheme: ")
subtheme = input()

random.seed(10)
num = random.randint(0,2)

if subtheme=="Political":
  print (Political[num])
