SkillSanta_Dict={
    "name":"Pooja",
    "age":22,
    "salary":60000,
    "city":"new delhi"
    }

print("previous dictionary is:",SkillSanta_Dict)

SkillSanta_Dict["location"]=SkillSanta_Dict["city"]
del SkillSanta_Dict["city"]

print("change dictionary is:",SkillSanta_Dict)
