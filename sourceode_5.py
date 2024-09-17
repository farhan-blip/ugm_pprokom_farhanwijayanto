A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' } 
C = {}

var_a = A.symmetric_difference(B)
var_b = B.symmetric_difference(A)
var_c = A.symmetric_difference(C)
var_d = B.symmetric_difference(C)

print("a. A  symmetric difference B", var_a,
    "\nb. B  symmetric difference A", var_b,
    "\nc. A  symmetric difference C", var_c,
    "\nd. B  symmetric difference C", var_d)