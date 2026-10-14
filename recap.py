#Author: Lemart

all_letters = ["a", "b","c", "d", "e", "f", "g", "h"]
print(all_letters)

all_letters.append("i")
print(all_letters)

all_letters[3] = "q"
print(all_letters)

all_letters.insert(6,"x")
print(all_letters)

all_letters.remove("e")
print(all_letters)

vegetables = ["carrots", "cabbage", "spinach", "tomato", "potato"]
all_combined = all_letters + vegetables
print(all_combined)

i = 0
while i < len(all_letters):
    print(all_letters[i])
    i += 1

sa_provinces = ["guateng", "mpumalanga", "limpopo", "Finland", "tokyo", "zimbabwe", "china"]
print(sa_provinces)
print(min(sa_provinces))
print(max(sa_provinces))
print(len(sa_provinces))
print(sa_provinces.index("tokyo"))
print(sa_provinces.count("china"))
print(sa_provinces.count("congo"))

