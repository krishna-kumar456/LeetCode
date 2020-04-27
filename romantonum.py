s = "MCMXCIV"

sym_map = {
"I":1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000
}

result = 0
prev = ""

for i,v in enumerate(s):
    if prev == "I" and (v == 'X' or v == 'V'):
        result -= sym_map[prev]
        result += sym_map[v] - sym_map["I"]
    elif prev == "X" and (v == 'L' or v == 'C'):
        result -= sym_map[prev]
        result += sym_map[v] - sym_map["X"]

    elif prev == "C" and (v == 'D' or v == 'M'):
        result -= sym_map[prev]
        result += sym_map[v] - sym_map["C"]

    else:
        result +=sym_map[v]

    prev = v


print(result)