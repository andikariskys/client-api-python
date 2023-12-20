import requests

class ModulRequest:
    # parameter private yang digunakan untuk 
    __base_url = ''
    
    # membuat function untuk mengisi value dari variabel base_url
    def __init__(self, url):
        self.__base_url = url
    
    # buat method untuk mengambil data dari API
    def ambil_data(self):
        # menggunakan method GET untuk mengambil data dari server
        respon = requests.get(self.__base_url)
        # cek apakah dapat terhubung engan API atau tidak
        if respon.status_code == 200:
            # jika dapat terhubung maka ambil semua data dari response tersebut
            data_server = respon.json()
            # buat perulangan untuk menampilkan data dictionary dari list/array
            for data in data_server:
                print(data)
        else:
            # jika tidak dapat terhubung maka akan memunculkan pesan berikut berserta error code-nya
            print("Gagal mengambil data dari server, error code: ", respon.status_code)

# buat object dari class ModulRequest
req = ModulRequest('https://fakestoreapi.com/products')
# panggil method untuk menampilkan data
req.ambil_data()