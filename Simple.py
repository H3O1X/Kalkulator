#program kalkulator

#function

def jumlah(x,y):
	return x+y

def kurang(x,y):
	return x-y
	
def kali(x,y):
	return x*y
	
def bagi(x,y):
	return x/y
	
print("pilih operasi hitung:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilih=input("Pilih:")

satu = int(input("Masukkan angka pertama : "))
dua = int(input("Masukkan angka kedua : "))

if pilih==1 :
	print(jumlah(satu,dua))
	
elif pilih==2 :
	print(kurang(satu,dua))
	
elif pilih==3 :
	print(kali(satu,dua))
	
elif pilih==4 :
	print(bagi(satu,dua))
	
else:
	print("Masukkan anda salah!")
