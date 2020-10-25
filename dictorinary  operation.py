#dictionary is a nothing but the key function.
d1={}
print(type(d1))
d2={"avanti":"2nd year","ved":"9th","rucha":"5th","parth":"8th"}
print(d2)
d2 ["pooja"]="8th"
print(d2)
del d2["pooja"]
print(d2)
d3=d2.copy()
del d3["avanti"]
print(d3)
d2.update({"rutuja":"1st year"})
print(d3)
print (d2.keys())
print(d2.items())
