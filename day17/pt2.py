from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]


program = []
registers = [0, 0, 0]
ip = 0
output = []

for line in content:
    if "Register A:" in line:
        registers[0] = int(line[12:])
    elif "Register A:" in line:
        registers[1] = int(line[12:])
    elif "Register A:" in line:
        registers[2] = int(line[12:])
    elif "Program:" in line:
        program = [int(x) for x in line[9:].split(',')]


def get_combo(combo):
    global registers
    if combo in [0, 1, 2, 3]:
        return combo
    elif combo in [4, 5, 6]:
        return registers[combo-4]
    else:
        print("7 is not a valid combo operand)")
        return None


def opcode(op, operand):
    global registers
    if op == 0:  # A // 2^combo
        registers[0] = registers[0] // (2**get_combo(operand))
    elif op == 1:  # B XOR lit
        registers[1] = registers[1] ^ operand
    elif op == 2:  # combo % 8
        registers[1] = get_combo(operand) % 8
    elif op == 3:  # Jump A Not Zero
        if registers[0] != 0:
            global ip
            ip = operand
    elif op == 4:  # B XOR C
        registers[1] = registers[1] ^ registers[2]
    elif op == 5:  # OUT
        global output
        output.append(get_combo(operand) % 8)
    elif op == 6:  # B XOR lit
        registers[1] = registers[0] // (2**get_combo(operand))
    elif op == 7:  # B XOR lit
        registers[2] = registers[0] // (2**get_combo(operand))


def run_program(A):
    global program
    global ip
    ip = 0
    global output
    global registers
    registers[0] = A
    while ip < len(program):
        p = ip
        ip += 2
        opcode(program[p], program[p+1])
    return output

def get_best_quine_input(program, cursor, sofar):
  for candidate in range(8):
    if run_program(sofar * 8 + candidate) == program[cursor:]:
      if cursor == 0:
        return sofar * 8 + candidate
      ret = get_best_quine_input(program, cursor - 1, sofar * 8 + candidate)
      if ret is not None:
        return ret
  return None

print(get_best_quine_input(program, len(program) - 1, 0))