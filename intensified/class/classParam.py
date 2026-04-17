class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

a.lastname = "최"
print(a.lastname)
print(Family.lastname)