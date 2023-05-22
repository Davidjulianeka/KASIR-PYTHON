def pembuka():
    print("SELAMAT DATANG DI TOKO GROSIR")
    print("               TOKO GROSIR              ")
    print("            GROSIR MAJU MUNDUR           ")
    print("        Aplikasi kasir TOKO GROSIR       ")
    print("============================================")

    
def pilihan():
    print("1. Jadwal Toko")
    print("2. Daftar Barang")
    pilih = input("Apa yang ingin anda lakukan?")
    print("")
    if (pilih == '1'):
        jam()
    elif (pilih == '2'):
        menu()
    else:
        print("Pilihan Salah")
    print("")

    
def jam():
    print("jadwal Toko: ")
    for weekday in ("Senin", "Selasa", "Rabu", "Kamis"):
        print("Hari", weekday, "Dibuka jam 8 Pagi - 9 malam")
    for weekend in ("Jumat", "Sabtu", "Minggu"):
        print("Hari", weekend, "Dibuka jam 6 pagi - 8 malam")
    print("")
    lanjut = input("Apakah anda ingin melanjutkan? (Y/T)")
    if (lanjut == 'Y'):
        pilihan()
    else:
        print("Terimah kasih Telah Datang di toko Grosir Maju Mundur")

        
def menu():
    print("")
    print("___________________________")
    print("Daftar Barang Grosir: ")
    print("___________________________")
    barang = ["BERAS 1 LITER   ", "TELOR 1 KILO    ", "TEPUNG 1 KILO   ", "BERAS MERAH 1LT ", "BAWANG MERAH 1KG", "BAWANG PUTIH 1KG", "MINYAK 1 LITER  "]
    harga = [10000, 8000, 10000, 12000, 8000, 6000, 28000]
    print("No| Nama Barang      | Harga")
    i = 0 
    for menu in (barang, harga):
        for a in range(0, 7):
            i += 1 
            print(str(i) + " | " + str(barang[a]) + " | " + str(harga[a]))
        break 
    print("")
    pilihmenu= input("Barang apa yang anda beli? ")
    if (pilihmenu == '1'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[0]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
     
    elif (pilihmenu == '2'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[1]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    elif (pilihmenu == '3'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[2]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    elif (pilihmenu == '4'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[3]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    elif (pilihmenu == '5'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[4]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    elif (pilihmenu == '6'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[5]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    elif (pilihmenu == '7'):
        try:
            pesanan = input("Berapa Barang? ")
            total = int(harga[6]) * int(pesanan)
            print("Totalnya adalah Rp.  ", total)
            bayar = input("Berapa Pembayaran? ")
            kembalian = int(bayar) - int(total)
            print("Kembalian anda adalah", kembalian)
        except ValueError:
                print("Anda salah memasukan input")
    else:
        print("Menu Tidak Tersedia")
    print("")
    lanjut = input("Apakah ada yang ingin anda beli lagi?")
    if (lanjut == 'Y'):
        pilihan()
    else:
        print("Terimahkasih telah datang di Grosir Maju Mundur")

pembuka()
print("")
pilihan()
