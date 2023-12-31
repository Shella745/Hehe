class Pilih:
    def pilihan(self):
        print("\n=============")
        print("PILIH POSISI")
        print("=============")
        print("1. Admin")
        print("2. Direktur SDM")
        print("3. Direktur")
        print("4. Keluar")
        pilih_posisi = input("Masukkan pilihan (1-4): ")
        return pilih_posisi
    
class User:
    def _init_(self, username, password, posisi):
        self.username = username
        self.password = password
        self.posisi = posisi

    def login(self):
        print("************************")
        print(f"Login sebagai {self.posisi}")
        print("************************")
        input_username = input(f"Masukkan username {self.posisi}: ")
        input_password = input(f"Masukkan password {self.posisi}: ")
        return input_username == self.username and input_password == self.password

class Admin(User):
    def __init__(self):
        super()._init_("admin123", "123", "Admin")
        self.dataDirektur = []
        self.dataDirekturSDM = []

    def tambahDataDirektur(self, nama, jabatan):
        direkturBaru = {'nama': nama, 'jabatan': jabatan}
        self.dataDirektur.append(direkturBaru)
        print(f"Data direktur {nama} ditambahkan dengan jabatan {jabatan}")

    def tambahDataDirekturSDM(self, nama, jabatan):
        direkturSDMBaru = {'nama': nama, 'jabatan': jabatan}
        self.dataDirekturSDM.append(direkturSDMBaru)
        print(f"Data direktur SDM {nama} ditambahkan dengan jabatan {jabatan}")

    def pilihEdit(self):
        print("\n=== EDIT DATA ===\n")
        print("Pilih data yang ingin diedit:")
        print("1. Direktur")
        print("2. Direktur SDM")
        print("3. Tidak edit data")

        pilihan = input("Masukkan pilihan (1-3): ")
        if pilihan == "1":
            self.editData(self.dataDirektur, "Direktur")
        elif pilihan == "2":
            self.editData(self.dataDirekturSDM, "Direktur SDM")
        elif pilihan == "3":
            pass 

    def editData(self, data, jenis):
        print(f"=== Edit Data {jenis} ===")
        nama = input(f"Masukkan nama {jenis} yang ingin diubah: ")

        for direktur in data:
            if direktur['nama'] == nama:
                direktur['nama'] = input(f"Masukkan nama {jenis} baru: ")
                direktur['jabatan'] = input(f"Masukkan jabatan {jenis} baru: ")

                print(f"Data {jenis} {nama} berhasil diubah.")
                break
        else:
            print(f"Tidak menemukan {jenis} dengan nama {nama}")

    def tampilData(self):
        print("\n=== Data Direktur ===")
        for direktur in self.dataDirektur:
            print(f"Nama: {direktur['nama']}, Jabatan: {direktur['jabatan']}")

        print("\n=== Data Direktur SDM ===")
        for direktur_sdm in self.dataDirekturSDM:
            print(f"Nama: {direktur_sdm['nama']}, Jabatan: {direktur_sdm['jabatan']}")


class DirekturSDM(User):
    def __init__(self):
        super()._init_("sdm234", "234", "Direktur SDM")
        self.dataPegawai = []
        self.dataGajiPokok = []

    def tambahDataPegawai(self):
        print("====================")
        print("Tambah Data Pegawai")
        print("====================")
        jumlah = int(input("Masukkan jumlah pegawai yang akan ditambahkan: "))

        for i in range(jumlah):
            nip = input("Masukkan NIP pegawai: ")
            nama = input("Masukkan nama pegawai: ")
            jabatan = input("Masukkan jabatan pegawai: ")
            gaji = 0
            standar_gaji = float(input("Masukkan standar gaji pokok pegawai: "))
            gaji_perjam = float(input("Masukkan gaji perjam:"))
            divisi = input("Masukkan divisi: ")

            data_pegawai = {
                "nip": nip,
                "nama": nama,
                "jabatan": jabatan,
                "gaji" : gaji,
                "standar_gaji": standar_gaji,
                "gaji_perjam": gaji_perjam,
                "divisi": divisi
            }

            self.dataPegawai.append(data_pegawai)
            print(f"Data pegawai {nama} ditambahkan.\n")

    def pilihEdit(self):
        print("Apakah anda ingin mengedit data?")
        while True:
            answer = input("(Y/N): ").upper()
            if answer == "Y":
                self.editDataPegawai()
                break
            elif answer == "N":
                break
            else:
                print("Masukkan Y atau N.")

    def editDataPegawai(self):
        print("===================")
        print("Edit Data Pegawai")
        print("===================")
        nip_to_edit = input("Masukkan NIP pegawai yang ingin diubah: ")

        for pegawai in self.dataPegawai:
            if pegawai['nip'] == nip_to_edit:
                pegawai['nama'] = input("Masukkan nama pegawai baru: ")
                pegawai['jabatan'] = input("Masukkan jabatan pegawai baru: ")
                pegawai['standar_gaji'] = float(input("Masukkan standar gaji pokok pegawai baru: "))
                pegawai['gaji_perjam'] = float(input("Masukkan gaji perjam baru:"))
                pegawai['divisi'] = input("Masukkan divisi: ")

                print(f"Data pegawai dengan NIP {nip_to_edit} berhasil diubah.")
                break
        else:
            print(f"Tidak menemukan pegawai dengan NIP {nip_to_edit}")

    def tampilData(self):
        print("\n=============")
        print("Tampil Data")
        print("=============")
        for pegawai in self.dataPegawai:
            print(f"NIP: {pegawai['nip']}, Nama: {pegawai['nama']}, Jabatan: {pegawai['jabatan']}, Standar Gaji Pokok: {pegawai['standar_gaji']}, Gaji Perjam: {pegawai['gaji_perjam']}, Divisi: {pegawai['divisi']}")

    def tampilPegawaiBulan(self):
        days = 0
        bln = input("Masukkan bulan yang ingin dilihat gajinya : ")
        if bln in ['Januari','Maret', 'Mei', 'Juli', 'Agustus', 'Oktober', 'Desember']:
            days = 27
        elif bln in ['Februari','April', 'Juni', 'September', 'November']:
            days = 26
        for pegawai in self.dataPegawai:
            pegawai['gaji'] = float(pegawai['standar_gaji'] + (pegawai['gaji_perjam'] * days * 5))

        print("====================================================")
        print(f"Tampil Pegawai Dengan Gaji Pada Bulan {bln}")
        print("====================================================")
        sorted_data = sorted(self.dataPegawai, key=lambda x: x['nip'])
        for pegawai in sorted_data:
            print(f"NIP: {pegawai['nip']}, Nama: {pegawai['nama']}, Jabatan: {pegawai['jabatan']}, Total Gaji: {pegawai['gaji']}, Divisi: {pegawai['divisi']}")

    def tampilListDivisi(self):
        print("\n====================")
        print("Tampil List Divisi")
        print("====================")
        divisi_tampil1 = set()

        for num, pegawai in enumerate(self.dataPegawai, start=1):
            divisi= pegawai['divisi']
            if divisi not in divisi_tampil1:
                divisi_tampil1.add(divisi)
                print(f"{num}. Divisi : {pegawai['divisi']}")

    def tampilDivisiStandarGaji(self):
        print("\n===========================================")
        print("Tampil List Divisi Beserta Standar Gajinya")
        print("===========================================")
        divisi_tampil2 = set()

        for num, pegawai in enumerate(self.dataPegawai, start=1):
            divisi = pegawai['divisi']
            if divisi not in divisi_tampil2:
                print(f"{num}. Divisi : {pegawai['divisi']}, Standar Gaji: {pegawai['standar_gaji']}")
                divisi_tampil2.add(divisi)

    def tampilPegawaiDivisiTertentu(self):
        print("\n===================================")
        print("Tampil Pegawai di Divisi Tertentu")
        print("===================================")
        divisi = input("Masukkan divisi untuk menampilkan pegawai: ")
        for pegawai in self.dataPegawai:
            if pegawai['divisi'] == divisi:
                print(f"NIP: {pegawai['nip']}, Nama: {pegawai['nama']}, Divisi: {pegawai['divisi']}")

    def tampilPejabatdiKantor(self):
        print("\n================================")
        print("Tampil Daftar Pejabat di Kantor")
        print("================================")
        pejabat_list = set([pegawai['jabatan'] for pegawai in self.dataPegawai])
        for pegawai in self.dataPegawai:
            if pegawai['jabatan'] in pejabat_list:
                print(f"NIP: {pegawai['nip']}, Nama: {pegawai['nama']}, Jabatan: {pegawai['jabatan']}")

    def totalGaji(self):
        print("\n===========================================")
        print("Total Gaji yang Harus Dibayar Setiap Bulan")
        print("===========================================")
        self.tampilPegawaiBulan()
        total_gaji = sum(pegawai['gaji'] for pegawai in self.dataPegawai)
        print(f"Total Gaji yang Harus di Bayar Bulan Ini: {total_gaji}")

class Direktur(DirekturSDM, User):
    def __init__(self, username, password, dktr_sdm):
        User._init_(self, username, password, "Direktur")
        self.dktrsdm = dktr_sdm

    def login(self):
        return super().login()

    def tampilListPegawai(self):
        self.dktr_sdm.tampilData()

    def tampilListDivisi(self):
        self.dktr_sdm.tampilListDivisi()

    def tampilDivisidanStandarGaji(self):
        self.dktr_sdm.tampilDivisiStandarGaji()

    def tampilListPegawaiDivisiTertentu(self):
        self.dktr_sdm.tampilPegawaiDivisiTertentu()

    def tampilListPejabat(self):
        self.dktr_sdm.tampilPejabatdiKantor()

    def tampilTotalGaji(self):
        self.dktr_sdm.totalGaji()
 
dktr_sdm = DirekturSDM()
direktur_obj = Direktur("dktr345", "345", dktr_sdm)

while True:
    pilih_obj = Pilih()
    pilih_posisi = pilih_obj.pilihan()

    if pilih_posisi == "1":
        posisi = "Admin"
    elif pilih_posisi == "2":
        posisi = "Direktur SDM"
    elif pilih_posisi == "3":
        posisi = "Direktur"
    elif pilih_posisi == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")

    aplikasi = None
    if posisi == "Admin":
        aplikasi = Admin()
    elif posisi == "Direktur SDM":
        aplikasi = dktr_sdm
    elif posisi == "Direktur":
        aplikasi = direktur_obj

    if aplikasi.login():
        if posisi == "Admin":
            nama_direktur = input("Masukkan nama Direktur: ")
            jabatan_direktur = input("Masukkan jabatan Direktur: ")
            aplikasi.tambahDataDirektur(nama_direktur, jabatan_direktur)
            nama_direktur_sdm = input("Masukkan nama Direktur SDM: ")
            jabatan_direktur_sdm = input("Masukkan jabatan Direktur SDM: ")
            aplikasi.tambahDataDirekturSDM(nama_direktur_sdm, jabatan_direktur_sdm)
            aplikasi.pilihEdit()
            aplikasi.tampilData()
            
        elif posisi == "Direktur SDM":
            aplikasi.tambahDataPegawai()
            aplikasi.pilihEdit()
            aplikasi.tampilData()
            aplikasi.tampilPegawaiBulan()
            aplikasi.tampilListDivisi()
            aplikasi.tampilDivisiStandarGaji()
            aplikasi.tampilPegawaiDivisiTertentu()
            aplikasi.tampilPejabatdiKantor()
            aplikasi.totalGaji()

         
        elif posisi == "Direktur":
            aplikasi.tampilListPegawai()
            aplikasi.tampilListDivisi()
            aplikasi.tampilDivisidanStandarGaji()
            aplikasi.tampilListPegawaiDivisiTertentu()
            aplikasi.tampilListPejabat()
            aplikasi.tampilTotalGaji()
                
            print("Program Selesai")
            break

    else:
        print("Username atau password salah. Silakan coba lagi.")

