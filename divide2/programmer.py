f = open("divide2.c","w")


f.write("#include <stdio.h>\n")
f.write("#include <stdint.h>\n")
f.write("#include <stdlib.h>\n\n")

f.write("int main(int argc, char* argv[])")
f.write("{\n")
f.write("    uint8_t number = atoi(argv[1]); // No problems here\n\n")

for i in range(2**16):
    f.write("    if (number == "+str(i)+")\n")
    if i % 2 == 0:
        f.write("        printf(\"even\\n\");\n")
    else:
        f.write("        printf(\"odd\\n\");\n")

f.write("}")

f.close