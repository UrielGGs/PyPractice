from random import randint, choice


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = "%s %s %s = " % (nums[0], op, nums[1])
    tries = 0

    while tries < 3:
        try:
            answer = int(input(prompt))
        except:
            continue

        if answer == result:
            print('Very good!')
            break
        else:
            print('Wrong answer')
            tries +=1
    else:
        print('%s%s' % (prompt, result))


def main():
    while True:
        exam()
        try:
            yn = input("Continue(y/n)?").strip()[0]
        except ImportError:
            continue
        except (KeyboardInterrupt, EOFError):
            print()
            yn = 'n'

        if yn in 'Nn':
            break


if __name__ == '__main__':
    main()
