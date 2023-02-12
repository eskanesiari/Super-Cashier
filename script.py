import pandas as pd

class Transaction:
    def __init__(self):
        """
        fungsi untuk menginisialisasi dictionary
        """
        self.data_item = dict()
        self.daftar_belanja = dict()

    def add_item(self, item, jumlah, harga):
        """
        fungsi untuk menambahkan item barang
        parameters =
        item    : nama item yang akan ditambahkan (str)
        jumlah  : jumlah item yang akan ditambahkan (int)
        harga   : harga item yang akan ditambahkan (int)
        output  : daftar item yang dibeli
        """
        self.data_item.update({item: [jumlah, harga]})
        return f'Item yang dibeli adalah : {self.data_item}'

    def update_item_name(self, item, item_baru):
        """
        fungsi untuk mengubah nama item
        parameters =
        item      : nama item lama (str)
        item_baru : nama item baru (str)
        output    : daftar item yang dibeli
        """
        temp = self.data_item[item]
        self.data_item.pop(item)
        self.data_item.update({item_baru: temp})
        return f'Item yang dibeli adalah : {self.data_item}'
    
    def update_item_qty(self, item, jumlah_baru):
        """
        fungsi untuk mengubah jumlah item
        parameters =
        item        : jumlah item lama (str)
        jumlah_baru : jumlah item baru (str)
        output      : daftar item yang dibeli
        """
        self.data_item[item][0] = jumlah_baru
        return f'Item yang dibeli adalah : {self.data_item}'

    def update_item_price(self, item, harga_baru):
        """
        fungsi untuk mengubah harga item
        parameters =
        item        : harga item lama (str)
        jumlah_baru : harga item baru (str)
        output      : daftar item yang dibeli
        """
        self.data_item[item][1] = harga_baru
        return f'Item yang dibeli adalah : {self.data_item}'
    
    def index_item(self, item):
        """
        fungsi untuk mengembalikan nilai index dari baris yang mengandung value 'item'
        parameters = 
        item     : item yang mau dicari (str)
        return i : index dari baris yang mengandung item (int)
        """
        for i in range(len(self.data_item)):
            if item == self.data_item[i][0]:
                return i
    
    def delete_item(self, item):
        """
        fungsi untuk menghapus item
        parameters = 
        item  : item yang ingin dihapus (str)
        output: daftar item yang dibeli
        """
        self.data_item.pop(item)
        return f'Item yang dibeli adalah : {self.data_item}'
    
    def reset_transaction(self):
        """
        fungsi untuk menghapus seluruh transaksi
        output: keterangan tidak ada item yang dibeli
        """
        self.data_item.clear()
        return f'Semua item berhasil di delete!'

    def check_order(self):
        """
        fungsi untuk melihat dan mengecek pesanan
        output : daftar item yang dipesan
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 0:
                data = pd.DataFrame(self.data_item).T
                data.columns = ['jumlah', 'harga']
                print(data.to_markdown())
                print('Pemesanan sudah benar')
            else:
                print('Tidak terdapat pesanan')
        except:
            print('Terdapat kesalahan input data. Harap melakukan reset transaksi')
    
    def total_price(self):
        """
        fungsi untuk menghitung diskon dan total belanja
        output : keterangan diskon yang didapatkan dan total belanja
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 200_000:
                total_belanja = total_belanja - (0.05*total_belanja)
                return f'Item yang dibeli adalah : {self.data_item}. Anda Mendapat Diskon 5%. Total belanja anda adalah : {total_belanja}'
            elif total_belanja > 300_000:
                total_belanja = total_belanja - (0.08*total_belanja)
                return f'Item yang dibeli adalah : {self.data_item}. Anda Mendapat Diskon 8%. Total belanja anda adalah : {total_belanja}'
            elif total_belanja > 500_000:
                total_belanja = total_belanja - (0.1*total_belanja)
                return f'Item yang dibeli adalah : {self.data_item}. Anda Mendapat Diskon 10%. Total belanja anda adalah : {total_belanja}'
            elif total_belanja <= 200_000:
                return f'Item yang dibeli adalah : {self.data_item}. Anda Tidak Mendapat Diskon. Total belanja anda adalah : {total_belanja}'
        except:
            print('Harap kembali memeriksa daftar belanja')
