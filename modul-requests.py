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
        # menggunakan method GET untuk mengambil data dari server
        respon = requests.get(self.__base_url)
        # cek apakah dapat terhubung dengan API atau tidak
        if respon.status_code == 200:
            # jika dapat terhubung (status code = 200) maka ambil semua data dari response tersebut
            
            # buat dokumen untuk menyimpan data (nama dan value) dari API
            file = open("hasil.txt", "w")
            
            data_server = respon.json()
            # print(data_server)
            # buat perulangan untuk mengubah data dari json ke tipe dictionary
            for data in data_server:
                # print(data)
                # ambil key pada dictionary, untuk memberikan judul
                api_keys = data.keys()
                # print(api_keys)
                # selanjutnya buat perulangan lagi untuk mengambil value dari dictionary yang telah dibuat diatas
                for key in api_keys:
                    # print(key)
                    # buat format untuk menyimpan file (cth. Nama makanan : Pizza)
                    # karena data pada API memiliki tipe data yang berbeda, maka kita ubah ke string terlebih dahulu
                    key_value = key + ': ' + str(data[key]) + '\n'
                    file.write(key_value)
                
                # setiap data yang diambil berikan jeda menggunakan enter pada file
                file.write('\n')
            
            # jika data sudah tersimpan kedalam file, maka tutup file-nya
            file.close()
            # berikan pesan bahwa data dari link API sudah berhasil diambil
            print("Data dari API berhasil diambil, silakan buka file 'hasil.txt'")
        else:
            # jika tidak dapat terhubung maka akan memunculkan pesan berikut berserta error code-nya
            print("Gagal mengambil data dari server, error code: ", respon.status_code)

# buat object dari class ModulRequest
req = AmbilDataApi('https://fakestoreapi.com/products')
# panggil method untuk menampilkan data
req.ambil_data()