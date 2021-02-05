from src.user import User
from datetime import date

#name = input("Saississez votre nom : ")
#firstname = input("Saississez votre prénom : ")
#year_birth = input("Saississez votre année de naissance : ")

print(type(date.today()))

p = User("nallet", "thibaud", 1991)
#p = User(name, firstname, year_birth)
print(p)