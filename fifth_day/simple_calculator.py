import sys

try:
    process = sys.argv[1]
    op1 = float(sys.argv[2])
    op2 = float(sys.argv[3])

except:
    print("Opeation, operand1 and operand2 are required agruements")
    sys.exit(0)

result = 0.

if process == "add":
    result = op1 + op2
elif process == "sub":
    result = op1 - op2

print(f"Result is: {result}")
