def donuts(count):
    
    if count < 10:
        return "number of donuts :"+str(count)
    else :
        return "number of donuts is many"

def both_ends(s):
    begining= s[0:2]
    end= s[-2:]
    if len(s) < 2:
        return " "
    else: 
        return begining + end

def fix_start(s):
    star= s[0]
    step_one= s[1:]
    new_string= step_one.replace(star, "*")
    return star+new_string


def mix_up(a, b):
    mix_a= b[:2] + a[2:]
    mix_b= a[:2] + b[2:]

    return mix_a +" " +mix_b

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print ('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print ('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print ('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print ('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
