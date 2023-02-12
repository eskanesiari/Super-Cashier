## SUPER CASHIER
Python Project Pacmann - AI/ML Engineering

---

## MENGENAI PROJECT
Ini merupakan suatu project Self-Service Cashier dengan menggunakan bahasa pemograman Python.

## LATAR BELAKANG
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


**Test 1**
Customer ingin membuat ID transaksi.
---
![1  ID customer](https://user-images.githubusercontent.com/101574764/218291152-b3e34d57-4544-40a6-9a16-635ff4fd2002.jpg)


**Test 2**
Customer ingin menambahkan dua item baru menggunakan method `add_item()`, dan item yang ditambahkan adalah 
- Nama item : Ayam Goreng, Quantity : 2, Harga : 20.000
- Nama item : Pasta Gigi, Quantity : 3, Harga : 15.000
---
![2  add item](https://user-images.githubusercontent.com/101574764/218290996-1a93cef5-2e0a-4d42-a37b-38a1a7124d08.jpg)


