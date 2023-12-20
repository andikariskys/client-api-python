import requests

class AmbilDataApi:
    """Class ini digunakan untuk mengambil data dari sebuah API"""
    # variabel private yang digunakan untuk menyimpan url dari API yang akan digunakan
    __base_url = ''
    
    # membuat function untuk mengisi value dari variabel base_url
    def __init__(self, url):
        self.__base_url = url
    
    # buat method untuk mengambil data dari API
    def ambil_data(self):
        # cek menggunakan try except apakah dapat terhubung dengan server API atau tidak
        try:
            # menggunakan method GET untuk mengambil data dari server
            respon = requests.get(self.__base_url)

            # buat dokumen untuk menyimpan data (nama dan value) dari API
            file = open("hasil.txt", "w")
            
            data_server = respon.json()
            # print(data_server)
            # buat perulangan untuk mengubah data dari json ke tipe dictionary
            for data in data_server:
                # print(data)
                # ambil value dari dictionary dengan format data['key'] lalu buat baris baru dibawahnya
                file.write('Nama Produk: ' + data['title'] + '\n')
                # karena key price pada dictionary menggunakan tipe data float, maka ubah terlebih dahulu menjadi string
                file.write('Harga: $' + str(data['price']) + '\n')
                file.write('Deskripsi: ' + data['description'] + '\n')
                file.write('Foto Produk: ' + data['image'] + '\n')
                
                # setiap data yang diambil berikan jeda menggunakan enter pada file
                file.write('\n')
            
            # jika data sudah tersimpan kedalam file, maka tutup file-nya
            file.close()
            # berikan pesan bahwa data dari link API sudah berhasil diambil
            print("Data dari API berhasil diambil, silakan buka file 'hasil.txt'")
            
        except:
            # jika tidak dapat terhubung maka akan memunculkan pesan berikut berserta error code-nya
            print("Gagal mengambil data dari server")

# buat object dari class ModulRequest
req = AmbilDataApi('https://fakestoreapi.com/products')
# panggil method untuk menampilkan data
req.ambil_data()