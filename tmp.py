from Classes.viewer import reader
import sys
import os






try:
    file = "C:/Users/Mykola/Documents/GitHub/Multilayer-simulation/testdata.json"
    try:
        materials=["FeCr1"]
    except:
        print("no materila argument provided! Why are you even using it then?")
        os.exit(1)
except:
    print("No filename is provided")
    os.exit(1)
   
if __name__ == "__main__":
    data=reader(file)
    data.GetMHonT(filter=materials)
    data.GetMTonH(filter=materials)
