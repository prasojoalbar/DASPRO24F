listPemilih= []

def tambah_Pemilih():
    idPemilih = input("Masukan Id Pemilih:")
    if any(i["id"] == idPemilih for i in listPemilih):
        print("id sudah kedaftar")
        return
    namaPemilih = input("Masukan nama Pemilih:")
    jurusanPemilih =input("Masukan Jurusan Pemilih:")
    listPemilih.append({"id" : idPemilih, "nama" : namaPemilih, "jurusan" : jurusanPemilih, "sudah_memilih" : False})
    print(" Pemilih Sudah di Daftarkan")
    print(listPemilih)
   
    
    
                     
