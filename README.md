## SUPER CASHIER
Python Project Pacmann - AI/ML Engineering

---

## OVERVIEW PROJECT
Ini merupakan suatu project Self-Service Cashier dengan menggunakan bahasa pemograman Python.

## BACKGROUND
- Untuk mempersingkat bisnis proses yaitu dengan membuat sistem kasir yang self-serice, sehingga customer bisa langsung memasukan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli.
- Agar customer yang berada di luar kota juga dapat melakukan pembelian di supermarket ini.
- Agar proses transaksi menjadi lebih efisien, karena customer tidak perlu menunggu untuk dilayani dan menghitung total belanja secara manual.

## REQUIREMENTS
- Fitur untuk membuat ID Transaksi customer
- Fitur untuk memasukkan nama item, jumlah item, dan harga barang.
- Fitur untuk meng-update nama item, jumlah item, dan harga item.
- Fitur untuk menghapus salah satu item dari nama item.
- Fitur untuk menghapus semua transaksi (reset transaksi)
- Fitur untuk melakukan pengecekan pesanaan (check order)
- Fitur untuk menghitung total belanja yang dibeli customer.

## FLOWCHART
![Untitled Diagram](https://user-images.githubusercontent.com/24706517/210150924-1bea1e4e-c470-417c-9b0a-7e93188c96c8.jpg)

## CODE "SCRIPT"
Semua kode di bawah ini berada pada file `script.py`.
- Membuat fungsi untuk memasukkan nama item, jumlah item, dan harga barang dengan `def add_item(self, item, jumlah, harga):`
- Membuat fungsi untuk meng-update nama item dengan `def update_item_name(self, item, item_baru):`
- Membuat fungsi untuk meng-update quantity/jumlah item dengan `def update_item_qty(self, item, jumlah_baru):`
- Membuat fungsi untuk meng-update harga item dengan `def update_item_price(self, item, harga_baru):`
- Membuat fungsi untuk menghapus salah satu item dengan `def delete_item(self, item):`
- Membuat fungsi untuk menghapus semua transaksi (reset) dengan `def reset_transaction(self):`
- Membuat fungsi untuk mengecek pesanan (check order) dengan `def check_order(self):`
- Membuat fungsi untuk menghitung total belanja yang dibeli dengan `def total_price(self):`

## CODE "TEST CASE"
Semua code di bawah ini berada pada file `test_case.ipyb`.

**Test 1 :** Customer ingin membuat ID transaksi.
![1  ID customer](https://user-images.githubusercontent.com/101574764/218291988-770badf7-a5d4-4c16-8475-5c429100cfda.jpg)

**Test 2 :** Customer ingin menambahkan dua item baru yaitu item yang ditambahkan adalah 
- Nama item : Ayam Goreng, Quantity : 2, Harga : 20.000
- Nama item : Pasta Gigi, Quantity : 3, Harga : 15.000
![2  add item](https://user-images.githubusercontent.com/101574764/218290996-1a93cef5-2e0a-4d42-a37b-38a1a7124d08.jpg)

**Test 3 :** Customer ingin mengganti jumlah dari Ayam goreng yang sebelumnya dibeli sebanyak 2 ekor menjadi 4 ekor.
![3  update quantity](https://user-images.githubusercontent.com/101574764/218291163-eff62c76-a4ac-4c5d-8906-b8a2694b75dc.jpg)

**Test 4 :** Customer ingin mengganti harga Ayam goreng yang sebelumnya ukuran kecil sebesar 20.000 menjadi Ayam goreng yang ukuran besar dengan harga 30.000.
![4  update price](https://user-images.githubusercontent.com/101574764/218291166-ab12134a-f50b-4919-add9-917a199d1fa2.jpg)

**Test 5 :** Customer ingin mengganti item yang sebelumnya Ayam goreng menjadi Ayam bakar.
![5  update name](https://user-images.githubusercontent.com/101574764/218291168-622efbb9-36da-4cc4-8ba9-686a9ddaf834.jpg)

**Test 6 :** Customer ingin menghapus item Pasta Gigi dikarenakan tidak menjadi membeli, sehingga pesanan terakhir nya menjadi Ayam Bakar saja yang harga 30.000 sebanyak 4 ekor.
![6  delete](https://user-images.githubusercontent.com/101574764/218291171-b810c12f-0edd-4aa3-8807-10db8cf2e214.jpg)

**Test 7 :** Customer ingin menghapus semua pesanan yang sudah dimasukkan dan mengecek apakah pesanannya sudah terhapus semua.
![7  reset dan co](https://user-images.githubusercontent.com/101574764/218291172-4521297c-3677-4d3d-9890-3e8c76a68e4f.jpg)

**Test 8 :** Customer ingin mengulang kembali dengan memasukan semua item barang yang ingin dibeli dan mengecek pesanannya apakah sudah sesuai. Item yang dimasukkan adalah :
- Nama item : Ayam Goreng, Quantity : 2, Harga : 20.000
- Nama item : Pasta Gigi, Quantity : 3, Harga : 15.000
- Nama item : Mainan Mobil, Quantity : 1, Harga : 200.000
- Nama item : Mi Instan, Quantity : 5, Harga : 3.000
![8  check order](https://user-images.githubusercontent.com/101574764/218291823-95196f3b-cd32-444a-b622-2ff45b33b59e.jpg)

**Test 9 :** Customer selesai berbelanja dan menghitung total belanja yang harus dibayarkan.
![9  total](https://user-images.githubusercontent.com/101574764/218291188-c10d7eb1-8818-4f72-aa51-d1e341683f89.jpg)


##SUMMARY
1. Super Cashier merupakan suatu program yang dapat membantu penjual/pemilik supermarket untuk menjual produknya secara efiesien dan tercatat.
2. Semua fitur yang ada dalam program ini sangat membantu customer dengan mudah, tepat dan cepat dalam proses transaksi yang dilakukan secara mandiri.

##NEXT DEVELOPMENT
1. Sebaiknya dibuatkan dalam suatu aplikasi yang friendly user
2. Sebaiknya ditambahkan dengan fitur pengiriman, live chat dan refund jika terjadi complain.


