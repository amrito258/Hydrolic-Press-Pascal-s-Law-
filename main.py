import math

print('F1, F2, A1, A2, r1, r2, d1, d2')
a = input('What do you want to calculate? => ')

if 'F1' in a:
    F2 = float(input('Enter the value of F2(N): '))
    print('1. A1, A2\n2. r1, r2\n3. d1, d2 ')
    known_quan = input('Which number of values you have?: ')

    if '1' in known_quan:
        A1 = float(input('Enter the value of A1(m²): '))
        A2 = float(input('Enter the value of A2(m²): '))
        F1 = (F2 * A1) / A2
        print(f'The value of F1 is {F1}N')

    elif '2' in known_quan:
        r1 = float(input('Enter the value of r1(m): '))
        r2 = float(input('Enter the value of r2(m): '))
        F1 = (F2 * (r1 * r1)) / (r2 * r2)
        print(f'The value of F1 is {F1}N')

    elif '3' in known_quan:
        d1 = float(input('Enter the value of d1(m): '))
        d2 = float(input('Enter the value of d2(m): '))
        F1 = (F2 * (d1 * d1)) / (d2 * d2)
        print(f'The value of F1 is {F1}N')

    else:
        print('You entered wrong!')

elif 'F2' in a:
    F1 = float(input('Enter the value of F1(N): '))
    print('1. A1, A2\n2. r1, r2\n3. d1, d2')
    known_quan = input('Which number of values you have?: ')

    if '1' in known_quan:
        A1 = float(input('Enter the value of A1(m²): '))
        A2 = float(input('Enter the value of A2(m²): '))
        F2 = (F1 * A2) / A1
        print(f'The value of F2 is {F2}N')

    elif '2' in known_quan:
        r1 = float(input('Enter the value of r1(m): '))
        r2 = float(input('Enter the value of r2(m): '))
        F2 = (F1 * (r2 * r2)) / (r1 * r1)
        print(f'The value of F1 is {F2}N')

    elif '3' in known_quan:
        d1 = float(input('Enter the value of d1(m): '))
        d2 = float(input('Enter the value of d2(m): '))
        F2 = (F1 * (d2 * d2)) / (d1 * d1)
        print(f'The value of F1 is {F2}N')

elif 'A1' in a:
    A2 = float(input('Enter the value of A2(m²): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    A1 = (F1 * A2) / F2
    print(f'The value of A1 is {A1}m²')

elif 'A2' in a:
    A1 = float(input('Enter the value of A1(m²): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    A2 = (F2 * A1) / F1
    print(f'The value of A2 is {A2}m²')

elif 'r1' in a:
    r2 = float(input('Enter the value of r2(m): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    r1 = math.sqrt((F1 * (r2 * r2)) / F2)
    r1 = round(r1, 4)
    print(f'The value of r1 is {r1}m')

elif 'r2' in a:
    r1 = float(input('Enter the value of r1(m): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    r2 = math.sqrt((F2 * (r1 * r1)) / F1)
    r2 = round(r2, 4)
    print(f'The value of r2 is {r2}m')

elif 'd1' in a:
    d2 = float(input('Enter the value of d2(m): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    d1 = math.sqrt((F1 * (d2 * d2)) / F2)
    d1 = round(d1, 4)
    print(f'The valuje of d1 is {d1}m')

elif 'd2' in a:
    d1 = float(input('Enter the value of d1(m): '))
    F1 = float(input('Enter the value of F1(N): '))
    F2 = float(input('Enter the value of F2(N): '))
    d2 = math.sqrt((F2 * (d1 * d1)) / F1)
    d2 = round(d2, 4)
    print(f'The valuje of d2 is {d2}m')

else:
    print('You entered wrong!')
