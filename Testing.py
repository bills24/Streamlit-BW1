import pandas as pd

df = pd.read_csv("Cafes Data", converters={"Cafe Type": eval})
print(df)
"""for i in df["Cafe Type"]:
    print(i)
    print(type(i))
    for j in i:
        print(j)"""
location = []
for i in df["Cafe Type"]:
    for j in i:
        if j not in location:
            location.append(j)

print(location)
