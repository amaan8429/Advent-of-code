from data import lines

def first_digit(s):
    for ch in s:
        if ch.isdigit():
            return ch
    return ''

def last_digit(s):
    for ch in s[::-1]:
        if ch.isdigit():
            return ch
    return ''

def main():
    sum = 0
    for line in lines.split('\n'):
        a = first_digit(line)
        b = last_digit(line)
        n = int(a + b)
        sum+=n
    print(sum)



main()






