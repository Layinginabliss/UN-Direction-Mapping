import csv
class Point:
    A = set();B = set();g = 0.0
    def __init__(self,A,B,g):self.A = set(A);self.B = set(B);self.g = g
class Output:
    a = 0;b = 0.0
    def __init__(self,a,b):self.a = a;self.b = b
def J(A,B):C = len(A & B);return C / (len(A) + len(B) - C)

tf = open('Indexed_mnist_train.csv')
z = set({'0','1','2','3','4','5','6','7','8','9'});P = [Point(set(),z,1)]

testfile = csv.reader(tf)
correct = 0
incorrect = 0
now = -1

for line in testfile:
    now += 1
    value = line[0]
    line.pop(0)
    O = []
    max = (0,0)
    error = 0
    found = False
    
    for y in P:
        for x in y.B:
            found_2 = False
            for o in O:
                if x == o.a:o.b += y.g * J(set(line),y.A) / len(y.B); found_2 = True;break
            if not found_2 : O.append(Output(x,y.g * J(set(line),y.A) / len(y.B)))
            
    for o in O:
        if o.b > max[1] : max = (o.a,o.b)
        
    if value == max[0] : correct += 1
    else: incorrect += 1
    
    for r in O:        
        if r.a == value and max[0] == r.a: found = True;break
        
    if not found:
        for r in O:
            if r.a == value and not r.a == max[0]:
                error = max[1] - r.b
                P.append(Point(set(line),set(value),1))
                P.append(Point(set(line),z - set(value),-1));break
    
    print(f'P {len(P)} : accuracy { "{:.5f}".format(correct / (correct + incorrect) * 100 ) } % : c \033[92m {correct} \033[0m : ic \033[91m {incorrect} \033[0m : value = {value}: max { max[0] } : \033[91m error { float("{:.4f}".format(error)) } \033[0m : React { [ (int(r.a),float("{:.4f}".format(r.b))) for r in O] }')