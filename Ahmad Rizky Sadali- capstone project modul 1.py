#Capstone Project Modul 1 (Create, Read, Update, Delete/CRUD)
#Ahmad Rizky Sadali
#JCDSOL-015-GROUP 2


# menciptakan objek buku dengan attribut2nya yg masih kosong, 
# yang nanti akan diisi oleh fungsi lain melalui user input

class Book:
    def __init__(self):
         self.books = {}
         self.book = {
            'judul': '',
            'penulis': '',
            'tahun': '',
            'jumlah': 0
            }
#-----------------------------------------------------------------\
#Fungsi Menu Utama
#dengan (self) setiap fungsi akan berjalan di dalam class. Perlu memasukkan self ke dalam setiap fungsi agar tidak error.
#while true, memastikan agar main menu tetap berjalan sampai ditutup dengan input
    def menu_book(self):
        while True:
            print("---MENU UTAMA---")
            print("1: Tambah Data Buku\n2: Perbaharui Data Buku\n3: Hapus Data Buku\n4: Tampilkan Data Buku\n5: Keluar dari Program\n")
            option = int(input("Masukkan angka menu pilihan: "))
            if option == 1:
              self.add_book()
            elif option == 2:
              self.edit_book()
            elif option == 3:
              self.delete_book()
            elif option == 4:
              self.read_books()
            elif option == 5:
              print("Keluar dari program...")
              exit() 
            else:
              print("Pilihan tidak tersedia")
              option = int(input("Harap masukkan angka yang tersedia: "))

#-----------------------------------------------------------------\
#Fungsi Read

    def read_books(self):
        print("\n---DAFTAR BUKU---\n")
         #view books added
        for k, v in self.books.items():
             print(k, end="\t")
             for b in v.values():
                 print(b, end="\t")
             print("\n")
        print("\n")

#-----------------------------------------------------------------\
#Fungsi Create
    def add_book(self):
         book = {}
         print("\t--- TAMBAH BUKU ---")
         
         #input untuk atribut buku, serta fungsi self untuk memasukkan ke dalam dictionary
         judul = input("\tMasukkan judul buku: ")
         book['judul'] = judul

         penulis = input("\tMasukkan nama penulis buku: ")
         book['penulis'] = penulis

         tahun = input("\tMasukkan tahun terbit buku: ")
         book['tahun'] = tahun

         jumlah = int(input("\tMasukkan jumlah stok buku yang tersedia: "))
         book['jumlah'] = jumlah

#kode buku akan menjadi key bagi value pair di dictionary
         code = int(input("\tMasukkan kode inventaris buku: "))
         self.books[code] = book
    
         print(f"\n\tBuku dengan kode {code} berhasil ditambahkan")

#-----------------------------------------------------------------\
#Fungsi Update

    def edit_book(self):
        print("\t---UBAH DATA---")

        code = int(input("Masukkan kode untuk buku yang ingin diubah: ")) 
        
        if code in self.books:
            while True:
                #mengubah atribut data buku yang ada
                print("\n\tPilih yang Data untuk Diubah \n")
                print("\t1: Judul\n\t2: Penulis\n\t3: Tahun Terbit\n\t4: Jumlah\n\t5: Kode Buku\n\t6: Kembali ke Menu")
            
                opt = int(input("\tPilih Opsi untuk Diubah: "))

                if opt == 1:
                    judul = input("\tMasukkan judul buku yang baru: ")
                    self.books[code]['judul'] = judul
                elif opt == 2:
                    penulis = input("\tMasukkan nama penulis baru: ")
                    self.books[code]['penulis'] = penulis
                elif opt == 3:
                    tahun = input("\tMasukkan tahun terbit yang baru: ")
                    self.books[code]['tahun'] = tahun
                elif opt == 4:
                    jumlah = int(input("\tMasukkan jumlah stok baru: "))
                    self.book[code]['jumlah'] = jumlah
                elif opt == 5:
                    code = int(input("\tMasukkan kode baru: "))
                    self.books[code] = code
                elif opt == 6: 
                    print("\n\t<- KEMBALI KE MENU UTAMA\n")
                    self.menu_book()
                    
                else:
                    print("\tTidak ada opsi tersedia\n")
                    opt = int(input("\tPilih Opsi: "))
        
        else:
            print("\n\t(ERROR) Kode yang dimasukkan tidak ada\n")
            print("\n\t<- KEMBALI KE MENU UTAMA\n")
            self.menu_book()


    
#-----------------------------------------------------------------\
#Fungsi Delete
    
    def delete_book(self):
        print("\t--- HAPUS DATA BUKU ---\n")

        code = int(input("\tMasukkan kode buku yang ingin dihapus: "))

        if code in self.books:
            del self.books [code]
            print(f"\tBuku dengan kode {code} berhasil dihapus\n")
        else:
            print("\n\tERROR: Tidak ada kode tersedia\n")

if __name__ == "__main__":
     b = Book()
     b.menu_book()
     