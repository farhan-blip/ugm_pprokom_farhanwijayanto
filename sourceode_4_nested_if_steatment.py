#Nama File: nested_if_steatment.py
jenis_kelamin= "Pria"
umur= 20
if(jenis_kelamin=="Pria"):
    if(umur>=25):
        print("Pria boleh Menikah")
    else:
        print("Pria Tidak Boleh Menikah")
elif(jenis_kelamin=="Wanita"):
    if(umur>=20):
        print("Wanita boleh Menikah")
    else:
        print("Wanita tidak Boleh Menikah")
else:
    print("Jenis Kelamin tidak terdaftar")