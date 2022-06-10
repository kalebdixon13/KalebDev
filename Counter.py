#Demonstrate the usage of counter objects 

from collections import Counter

def main(): 
    class1 = ["Bob", "Becky", "Jo", "Kaleb", "Tony", "Jonah", "Kaleb"]
    class2 = ["Grant", "Moises", "Alex", "Jaiden", "Hunter"]

    #Count how much are in the classes
    c1 = Counter(class1)
    c2 = Counter(class2)

    c1 = sum(c1.values() )

    print(c1, "are in class 1") 
    print(c2, "here are the counters")


main()