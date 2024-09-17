A = {100, 7, 8} 
B = {200, 4, 5}
C = {300, 2, 3} 
D = {100, 200, 300}

var_a = A & D
var_b = B & D
var_c = C & D
var_d = A & B & C & D

print("a.A ∩ D:", var_a,
    "\nb.B ∩ D:", var_b,
    "\nc.C ∩ D:", var_c,
    "\nd.A ∩ B ∩ C ∩ D:", var_d)
