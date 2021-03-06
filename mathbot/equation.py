import re, math

def two_var_equation(text):
    const = [["","",""],["","",""]]
    formula = text.split("\n")
    if formula[0][0] == "x":
        const[0][0] += '1'
    if formula[1][0] == "x":
        const[1][0] += '1'

    for m in range(2):
        j=0
        for i in range(len(formula[m])):
            if formula[m][i] == 'x' or formula[m][i] == 'y':
                j+=1
            elif formula[m][i] == '=':
                pass
            elif formula[m][i] == "+":
                if formula[m][i+1] == "y":
                    const[m][j] += '1'
                else:
                    pass
            else:
                const[m][j] += formula[m][i] 

    print(const)
    delta = int(const[0][0]) * int(const[1][1]) - int(const[0][1]) * int(const[1][0])
    delta_x = int(const[0][2]) * int(const[1][1]) - int(const[0][1]) * int(const[1][2])
    delta_y = int(const[0][0]) * int(const[1][2]) - int(const[0][2]) * int(const[1][0])

    x = delta_x/delta
    y = delta_y/delta

    return 'x='+str(x)+'\n'+'y='+str(y)


def inverse_matrix(text):
    a = text.split("\n")
    matrix= [] 
    for i in range(2):
        matrix.append([x for x in a[i].split(' ')])
    delta = 1/(int(matrix[0][0]) * int(matrix[1][1]) - int(matrix[0][1]) * int(matrix[1][0]))

    
    return '[' + str(delta*int(matrix[1][1])) + ', ' + str(delta*int(matrix[0][1])*-1) + '\n' + ' ' + str(delta*int(matrix[1][0])*-1) + ', ' + str(delta*int(matrix[0][0])) + ' ]'

def HorizontalThrow(text):
    velocity, height = text.split('/')
    time = math.sqrt(int(height)*2/10)
    distance = int(velocity)*time 
    return "時間: " + str(time) + ' sec\n距離: ' + str(distance) + ' m'