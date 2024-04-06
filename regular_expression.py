import re
pattern = r"colour"  #### row string
text = "My favourite colour is Red"
match = re.search(pattern, text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())


if re.search(pattern,"red is a colour, I love red colour"):

    print("Match")
else:
    print("Not Matched")

pattern2 = r"red"
if re.match(pattern2,"red is a colour, I love red colour"):

    print("Match")
else:
    print("Not Matched")


pattern3 = r"colour"
print(re.findall(pattern3,"red is a colour, I love red colour"))


