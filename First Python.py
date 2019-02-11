"""

thisdict =    {
    "brand": "Ford",
        "model": "Mustang",
            "year": 1964
}
print(thisdict)

family =    {
    1: "Kevin",
        2: "Mom",
            3: "Delano",
                4: "Kameren"
}

print(family)

for x in family.items():
    print(x)

if 2 in family:
    print("Mom is home")
    print("Welcome back")


else:
    print("Where is she?")

x = str("")

while "Mom" not in family.items():
    print("Who's leaving?")
    x = input()
    family.pop([x])         #WHY CANT I DELETE THIS KEY-VALUE PAIR

print("Mom Left")

"""
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
     for line in response:
         line = line.decode('utf-8')  # Decoding the binary data to text.
         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
             print(line)

