import csv

class Point:
    A = set();B = set();g = 0.0
    def __init__(self,A,B,g):self.A = set(A);self.B = set(B);self.g = g
class Output:
    a = 0;b = 0.0
    def __init__(self,a,b):self.a = a;self.b = b
def J(A,B):C = len(A & B);return C / (len(A) + len(B) - C)

P = [Point(set(),set({'0','1','2','3','4','5','6','7','8','9'}),1)]

def map(file_name,P,test_only = False):
    tf = open(file_name)
    testfile = csv.reader(tf)
    correct = 0
    incorrect = 0
    now = -1
    error  = []

    for line in testfile:
        now += 1
        value = line[0]
        line.pop(0)
        O = []
        max = (0,0)
        found = False
        
        for y in P:
            for x in y.B:
                found_2 = False
                for o in O:
                    if x == o.a: 
                        o.b += y.g * J(set(line),y.A) / len(y.B)
                        found_2 = True
                        break
                if not found_2 :
                    O.append(Output(x,y.g * J(set(line),y.A) / len(y.B))) 
                
        for o in O:
            if o.b > max[1] : max = (o.a,o.b)
            
        if value == max[0] : correct += 1
        else: incorrect += 1
        
        for r in O:        
            if r.a == value and max[0] == r.a: found = True;break
            
        error.append(0)
            
        if not found and not test_only:
            for r in O:
                if r.a == value and not r.a == max[0]:
                    error[len(error)-1]  = max[1] - r.b
                    P.append(Point(set(line),set(value),1))
                    break
        
        error_type = '\033[91m'
        if error[len(error)-1] == 0:
            error_type = '\033[92m'
            
        React = f' : {error_type} React { [ (int(r.a),float("{:.4f}".format(r.b))) for r in O] } \033[0m '
       # React = ''
        
        print(f'T : {now} / 60000 : P {len(P)} :'
            f'Mean Accuracy { "{:.5f}".format(correct / (correct + incorrect) * 100 ) } % : '
            f'C \033[92m {correct} \033[0m : Ic \033[91m {incorrect} \033[0m :'
            f' Value {value} : {error_type} Max { max[0] } \033[0m : '
            f'\033[91m AR : {float("{:.4f}".format(sum(x for x in error)/len(error)))} \033[0m : '
            f'{error_type} Error { float("{:.4f}".format(error[len(error)-1])) } \033[0m'
            + React)
    
    # T - Data Corrently at
    # P - Total records
    # C - Correct ones thus far
    # Ic - Incorrect ones thus far
    # Value - Right value 
    # Max - Record votted higest value
    # AR - Avarage Error
    # Error - Rhe distant between true value and incorrect value
    # React - Full election

# This acived 89.95 %  with total 6887 records
map('Data/Indexed_mnist_train.csv',P)
map('Data/Indexed_mnist_test.csv',P,True)
