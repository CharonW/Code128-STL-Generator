
CODE128_PATTERNS = {
    0:  [2,1,2,2,2,2],
    1:  [2,2,2,1,2,2],
    2:  [2,2,2,2,2,1],
    3:  [1,2,1,2,2,3],
    4:  [1,2,1,3,2,2],
    5:  [1,3,1,2,2,2],
    6:  [1,2,2,2,1,3],
    7:  [1,2,2,3,1,2],
    8:  [1,3,2,2,1,2],
    9:  [2,2,1,2,1,3],
    10: [2,2,1,3,1,2],
    11: [2,3,1,2,1,2],
    12: [1,1,2,2,3,2],
    13: [1,2,2,1,3,2],
    14: [1,2,2,2,3,1],
    15: [1,1,3,2,2,2],
    16: [1,2,3,1,2,2],
    17: [1,2,3,2,2,1],
    18: [2,2,3,2,1,1],
    19: [2,2,1,1,3,2],
    20: [2,2,1,2,3,1],
    21: [2,1,3,2,1,2],
    22: [2,2,3,1,1,2],
    23: [3,1,2,1,3,1],
    24: [3,1,1,2,2,2],
    25: [3,2,1,1,2,2],
    26: [3,2,1,2,2,1],
    27: [3,1,2,2,1,2],
    28: [3,2,2,1,1,2],
    29: [3,2,2,2,1,1],
    30: [2,1,2,1,2,3],
    31: [2,1,2,3,2,1],
    32: [2,3,2,1,2,1],
    33: [1,1,1,3,2,3],
    34: [1,3,1,1,2,3],
    35: [1,3,1,3,2,1],
    36: [1,1,2,3,1,3],
    37: [1,3,2,1,1,3],
    38: [1,3,2,3,1,1],
    39: [2,1,1,3,1,3],
    40: [2,3,1,1,1,3],
    41: [2,3,1,3,1,1],
    42: [1,1,2,1,3,3],
    43: [1,1,2,3,3,1],
    44: [1,3,2,1,3,1],
    45: [1,1,3,1,2,3],
    46: [1,1,3,3,2,1],
    47: [1,3,3,1,2,1],
    48: [3,1,3,1,2,1],
    49: [2,1,2,3,3,1],
    50: [2,3,2,1,3,1],
    51: [2,1,3,1,2,3],
    52: [2,1,3,3,2,1],
    53: [2,3,3,1,2,1],
    54: [3,1,2,1,3,1],
    55: [3,1,1,1,2,3],
    56: [3,1,1,3,2,1],
    57: [3,3,1,1,2,1],
    58: [3,1,2,3,1,1],
    59: [3,3,2,1,1,1],
    60: [3,1,4,1,1,1],
    61: [2,2,1,4,1,1],
    62: [4,3,1,1,1,1],
    63: [1,1,1,2,2,4],
    64: [1,1,1,4,2,2],
    65: [1,2,1,1,2,4],
    66: [1,2,1,4,2,1],
    67: [1,4,1,1,2,2],
    68: [1,4,1,2,2,1],
    69: [1,1,2,2,1,4],
    70: [1,1,2,4,1,2],
    71: [1,2,2,1,1,4],
    72: [1,2,2,4,1,1],
    73: [1,4,2,1,1,2],
    74: [1,4,2,2,1,1],
    75: [2,4,1,2,1,1],
    76: [2,2,1,1,1,4],
    77: [4,1,3,1,1,1],
    78: [2,4,1,1,1,2],
    79: [1,3,4,1,1,1],
    80: [1,1,1,2,4,2],
    81: [1,2,1,1,4,2],
    82: [1,2,1,2,4,1],
    83: [1,1,4,2,1,2],
    84: [1,2,4,1,1,2],
    85: [1,2,4,2,1,1],
    86: [4,1,1,2,1,2],
    87: [4,2,1,1,1,2],
    88: [4,2,1,2,1,1],
    89: [2,1,2,1,4,1],
    90: [2,1,4,1,2,1],
    91: [4,1,2,1,2,1],
    92: [1,1,1,1,4,3],
    93: [1,1,1,3,4,1],
    94: [1,3,1,1,4,1],
    95: [1,1,4,1,1,3],
    96: [1,1,4,3,1,1],
    97: [4,1,1,1,1,3],
    98: [4,1,1,3,1,1],
    99: [1,1,3,1,4,1],
    100:[1,1,4,1,3,1],
    101:[3,1,1,1,4,1],
    102:[4,1,1,1,3,1],
    103:[2,1,1,4,1,2],
    104:[2,1,1,2,1,4],   
    105:[2,1,1,4,1,2], 
    106:[2,3,3,1,1,1,2]  
}

def encode_code128_modules(s: str) -> list[int]:
    if len(s) == 0:
        raise ValueError("Empty string not allowed")
    if len(s) > 12:
        raise ValueError("String length must not exceed 12 characters")
   
    START_B = 104
    STOP = 106
  
    symbols = [START_B]

    for ch in s:
        v = ord(ch) - 32
        if not (0 <= v <= 94):
            raise ValueError(f"Unsupported character: {ch}")
        symbols.append(v)

    checksum = symbols[0]
    for i, sym in enumerate(symbols[1:], start=1):
        checksum += sym * i
    checksum %= 103
    symbols.append(checksum)

    symbols.append(STOP)

    modules = []
    for sym in symbols:
        modules.extend(CODE128_PATTERNS[sym])

    return modules
while True:
    s = input("String input (limit 10):")
    if len(s) > 10:
        print("Illigle retry:")
    else:
        break
modules = encode_code128_modules(s)
print(modules)

import subprocess

OPENSCAD_EXE = r"C:\Program Files\OpenSCAD\openscad.exe"

UNIT = 0.6         
BAR_LENGTH = 25.0   
BAR_DEPTH  = 0.5    

SCAD_FILE = "barcode.scad"
STL_FILE  = "barcode.stl"

with open(SCAD_FILE, "w", encoding="utf-8") as f:
    f.write(f"UNIT = {UNIT};\n")
    f.write(f"BAR_LENGTH = {BAR_LENGTH};\n")
    f.write(f"BAR_DEPTH = {BAR_DEPTH};\n\n")

    f.write(f"modules = {modules};\n\n")

    f.write("// OpenSCAD ）\n")
    f.write("function prefix_sum(arr, i) =\n")
    f.write("    (i <= 0) ? 0 : arr[i-1] + prefix_sum(arr, i-1);\n\n")

    f.write("for (i = [0 : len(modules)-1]) {\n")
    f.write("    w = modules[i] * UNIT;\n")
    f.write("    x = prefix_sum(modules, i) * UNIT;\n\n")
    f.write("    if (i % 2 == 0) {\n")
    f.write("        translate([x, 0, 0])\n")
    f.write("            cube([w, BAR_LENGTH, BAR_DEPTH], center=false);\n")
    f.write("    }\n")
    f.write("}\n")

print("✓ OpenSCAD File generated:", SCAD_FILE)

cmd = [
    OPENSCAD_EXE,
    "-o", STL_FILE,
    SCAD_FILE
]

subprocess.run(cmd, check=True)

print("✓ STL File generated:", STL_FILE)
