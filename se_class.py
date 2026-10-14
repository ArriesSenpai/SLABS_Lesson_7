#Author Lemart

first_group = ["Lemart", "Nsuku","Owethu","Sibonile","Nhanhla","Kwandokuhle"]
print(first_group)
first_group.append("Jabulile")
print(first_group)

first_group[3] = "Quintin"
print(first_group)

first_group.insert(0, "Pearl")
print(first_group)

first_group.remove("Owethu")
print(first_group)

second_group = ["Tsehpo", "Carol", "Nthabiseng", "Ndivhuwo", "Bontle", "Lehlogonolo", "Lemuel"]
combined_group = first_group + second_group
print(combined_group)
