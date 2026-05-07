


def item_finder(item):
    list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]

    if item in list:
        print("Item found")
    else:
        print("Item not found")

''''
def main():
    planets=["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]

    print("number of planets: ", len(planets))

    #print the first planet
    print("first  planets: ",planets[0])

    #print the last planet
    print("last planet: ",planets[-1])
    print("last planet: ",planets[len(planets) -1 ])


    print("max:",max(planets))
    print("min:",min(planets))

    neighbor=["mercury","venus"] *4
    print(neighbor)
'''



def main():
   item_finder("Mercury")



main()
