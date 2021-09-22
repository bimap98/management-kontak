# Program Management Kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("============================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"No Telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon: ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }

    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("No telepon yang akan dihapus : ")

    index = -1
    
    for i in range(0, len(daftar_kontak)):
        if telepon == daftar_kontak[i]["telepon"]:
            index = i
            break

    if index == -1:
        print("Data tidak ditemukan")
    
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus kontak")

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("============================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"No Telepon : {kontak['telepon']}")