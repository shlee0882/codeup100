a = input()

def f(x):
    return {
        'A': 'best!!!',
        'B': 'good!!',
        'C': 'run!',
        'D': 'slowly~'
    }.get(x, 'what?')

b = f(a)

print(b)
