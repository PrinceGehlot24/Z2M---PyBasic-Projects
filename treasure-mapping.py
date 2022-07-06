print("Welcome to the Treasure-Mapping")

row1 = ["■", "■", "■"]
row2 = ["■", "■", "■"]
row3 = ["■", "■", "■"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put your treasure?\n")
x = int(position[0])
y = int(position[1])  

new = map[y - 1]
new[x - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
