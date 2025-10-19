file = open("Table_de_multiplication.txt", "w+")

for i in range(1,11):
    file.write(f"La table de multiplication de {i:02}\n")
    for j in range(1,11):
        file.write(f"{i:02} x {j:02} = {i*j}\n")