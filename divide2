print("#include <stdio.h>")
print("#include <stdint.h>")
print("#include <stdlib.h>")

print("int main(int argc, char* argv[])")
print("{")
print("    uint8_t number = atoi(argv[1]); // No problems here")

for i in range(2**8):
    print("    if (number == "+str(i)+")")
    if i % 2 == 0:
        print("        printf(\"even\\n\");")
    else:
        print("        printf(\"odd\\n\");")

print("}")
