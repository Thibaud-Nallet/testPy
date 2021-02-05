from src.user import User

name = input("Saississez votre nom : ")
firstname = input("Saississez votre prénom : ")
year_birth = int(input("Saississez votre année de naissance : "))

#p = User("nallet", "thibaud", 1991)
p = User(name, firstname, year_birth)
print(p)