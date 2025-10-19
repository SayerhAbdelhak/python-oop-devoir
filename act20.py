### act20 gestion des adresse IP
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]
print(f"list originale : {adresses_ip}")
    
#1/2/3 
print(f"la premiere {adresses_ip[0]}, la derniere {adresses_ip[-1]}, la troisieme {adresses_ip[2]}")

#4
adresses_ip.append("172.31.0.1")


#5
adresses_ip.remove("200.100.50.1")
print(f"qst 5: {adresses_ip}")

#6
print(f"le nombre d'add restant est {len(adresses_ip)}")

#7
if "192.168.0.1" in adresses_ip:
    print("192.168.0.1 est dans la liste")
else:
    print("192.168.0.1 n'est pas dans la liste")

classses_ip={
    "192.168.0.1":"classe A",
    "10.0.0.1":"classe B",
    "172.16.0.1":"classe C",
    "200.100.50.1":"adresse ip publique",
    "169.254.0.1":"adresse ip de lien local (apipa)"
}
#8
print(f"qst 8: {classses_ip["10.0.0.1"]}")

#9
adresses_ip.sort
print(f"la liste apre sort:{adresses_ip}")

#10
for el in classses_ip:
    if classses_ip[el] == "classe C":
        print(f"l element {el} est dans la classe C.")
    else:
        print(f"l element {el} n'est pas dans la classe C.")

#11
counter = 0
for el in classses_ip:
    if classses_ip[el] == "adresse ip publique":
        counter += 1

print(f"le nombre d'elements avec adresse ip public est {counter}")