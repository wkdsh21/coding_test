li = ["*", "-", "+", "//"]
a = 5
b = 1
c = 6
for i in li:
    if eval(f"{a}{i}{b}=={c}"):
        print(f"{a}{i}{b} = {c}")
    if eval(f"c==b{i}a"):
        print(f"{a}{i}{b} = {c}")
