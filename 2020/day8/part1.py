def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    all_x = create_possible_inputs(x)

    for i, x in enumerate(all_x):
        visited = set()
        position = 0
        acc = 0
        acc = execute(position, visited, acc, x)
        if acc:
            print(i, acc)

def create_possible_inputs(x):
    x_out = [x]
    for index, i in enumerate(x):
        instruction = i[:3]
        if instruction == 'nop':
            test = x.copy()
            test[index] = 'jmp' + test[index][3:]
            x_out.append(test)
        elif instruction == 'acc':
            pass
        elif instruction == 'jmp':
            test = x.copy()
            test[index] = 'nop' + test[index][3:]
            x_out.append(test)
        else:
            print('Error')
    return x_out

def execute(position, visited, acc, x):
    if position in visited:
        return False
    elif position == len(x):
        return acc
    else:
        visited.add(position)

    instruction = x[position][:3]
    if instruction == 'nop':
        position += 1
    elif instruction == 'acc':
        acc += int(x[position][4:])
        position += 1
    elif instruction == 'jmp':
        position += int(x[position][4:])
    else:
        print("ERROR")
    return execute(position, visited, acc, x)



if __name__ == '__main__':
    main()
