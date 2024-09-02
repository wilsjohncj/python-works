from json import load

f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\JSONworks\\filims.json","r")

filims = load(f)

for fl in filims:

    print(fl.get("title"))

