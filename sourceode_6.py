A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' } 
C = {}

var_a = A.difference(B)
var_b = B.difference(A)
var_c = A.difference(C)
var_d = B.difference(C)

print("a. A  difference B", var_a,
    "\nb. B  difference A", var_b,
    "\nc. A  difference C", var_c,
    "\nd. B  difference C", var_d)