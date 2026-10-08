import sys
# Assignment: 
# 1. do support for mul and div as well
# 2. support power 2 pow 3 = 2 x 2 x 2 = 8
# 3. div operator, op2 should not be 0

try:
    process = sys.argv[1]
    process = process.lower()

    if process not in ("add", "sub"):
        raise Exception(f"Invalid process: {process}")
except Exception as err:
    print("Opeation should be one of: add, sub")
    print(err)
    sys.exit(0)

try:
    op1 = float(sys.argv[2])
except:
    print("operand1 should be valid float number")
    sys.exit(0)

try:
    op2 = float(sys.argv[3])
except:
    op2 = 0.

result = 0.

if process == "add":
    result = op1 + op2
elif process == "sub":
    result = op1 - op2


print(f"Result of {op1} {process} {op2} is: {result}")
