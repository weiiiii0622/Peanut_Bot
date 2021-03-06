import re

def two_var_equation(text):
    const = [[],[]]
    formula = text.split("\n")
    const1 = re.split('[x y + - =]',formula[0])
    const2 = re.split('[x y + - =]',formula[1])
    for i in const1:
        if i != '':
            const[0].append(float(i))
    for i in const2:
        if i != '':
            const[1].append(float(i))
    print(const)
    delta = const[0][0]*const[1][1]-const[0][1]*const[1][0]
    delta_x = const[0][2]*const[1][1]-const[0][1]*const[1][2]
    delta_y = const[0][0]*const[1][2]-const[0][2]*const[1][0]

    x = delta_x/delta
    y = delta_y/delta

    return 'x='+str(x)+'\n'+'y='+str(y)