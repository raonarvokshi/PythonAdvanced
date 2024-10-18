emri = "Raonar"
mosha = 17
temperatura = 25.5

print(type(emri))
print(type(mosha))
print(type(temperatura))

mosha = mosha + 10
print(mosha)

emri_mbiemri = emri + " Vokshi"
print(emri_mbiemri)

my_data = ["Raonar", "Vokshi", 17, "Shkolla Digjitale"]
age = my_data[2]
print(age)
my_data.append("Prishtina")
print(my_data)
my_data.insert(4, "Klasa 12")
print(my_data)
my_data.remove("Vokshi")
del my_data[0]
print(my_data)