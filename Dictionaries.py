def ninjas(dictionary):
    for key,val in dictionary.items():
        print(f"I am {key} and I am a {val} belt ")


ninja_belts={}

while True:
    name=input("Enter the ninja name ")
    belt=input("Enter the ninja belt color ")
    ninja_belts[name] = belt

    another=input("Enter another ninja?? ")

    if another == "y":
        continue
    else:
        break

ninjas(ninja_belts)