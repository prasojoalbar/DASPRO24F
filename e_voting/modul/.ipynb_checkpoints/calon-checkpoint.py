listCalon =[]

def tambah_calon():
    idCalon = input("Masukkan id Calon :")
    if any(i["id"] == idCalon for i in listCalon):
        print("id sudah terdaftar")
        return
    namaCalon = input("Masukkan nama Calon:")
    visiCalon = input("Masukkan visi Calon:")
    listPemilih.append({"id" : idCalon, "nama" : namaCalon, "visi" : visiCalon, "jumlah_suara" : 0})
    print("calon sudah terdaftar")
    print(listPemilih)
    
    
    
