#Author: Lemart

letters = ["a", "b", "c", "d", "e", "f"]
letters.append("z")
print(letters)

unchangeable_letters = tuple(letters)
letters.append("x")
print(letters)

aplhabets = ("b","x","w","q")
aplhabets.append("c")
print(aplhabets)
