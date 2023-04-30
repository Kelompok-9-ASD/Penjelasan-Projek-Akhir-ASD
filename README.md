# Penjelasan-Projek-Akhir-ASD


KELOMPOK 9 ASD

AGUSTIAN ARDIANSYAH

NABIL FIKRI

RIVALDO


DESKRIPSI PROGRAM


Linked list adalah struktur data yang terdiri dari serangkaian record, setiap record memiliki field yang menyimpan alamat/referensi dari record berikutnya (berurutan). Data yang dihubungkan oleh tautan dalam daftar tertaut disebut node. 

Pada pemograman Python kali ini akan mengusung tema pharmacy medicines list yang dirancang untuk mengelola operasi sorting & searching pada pharmacy secara efektif. Program dapat menstock obat dan produk lainnya, produk dapat ditambahkan ke inventori. class Pharmacy merepresentasikan sebuah linked list dari node Medicine, dimana setiap node berisi nama, quantity, id, serta referensi ke node berikutnya dalam daftar.

Class Pharmacy berisi daftar objek Pengguna, yang mewakili pengguna yang dapat mengakses program, serta turunan dari class pharmacy. Pada main_menu menampilkan menu utama dengan opsi masuk dan mendaftar sebagai pengguna, atau keluar dari program. Dan pada user_menu menampilkan menu pengguna dengan opsi untuk menambah, menghapus, menampilkan list medicines, atau log out.

Metode login_required meminta pengguna untuk memasukan nama pengguna dan kata sandi mereka dan memverifikasi kredensial mereka menggunakan metode login, yang memeriksa apakah nama pengguna dan kata sandi cocok dengan pengguna yang terdaftar. Metode add_user dan remove_user memungkinkan pengelolaan akun pengguna jadi efisien.


STRUKTUR PROJECT


Struktur data linked list memiliki beberapa elemen penting, yaitu:

Node:
Node adalah elemen dasar dari linked list. Setiap node memiliki dua bagian yaitu data dan pointer. data adalah informasi yang disimpan dalam sebuah node sedangkan pointer adalah alamat memori dari node berikutnya dalam daftar tertaut.

Head:
Head adalah penunjuk ke simpul pertama dari daftar tertaut. Head digunakan untuk membuka linked list dari awal. 

Tail:
Tail adalah penunjuk yang menunjuk ke simpul terakhir dari daftar tertaut. Antrian digunakan untuk menambahkan node baru ke linked list.

Next:
Setiap node memiliki penunjuk berikutnya yang menunjuk ke node berikutnya dalam daftar tertaut. 

Operasi/operator yang digunakan adalah:

1. Add : fungsi untuk menambah data baru.
2. Remove : fungsi untuk menghapus data.
3. Display : fungsi untuk menampilkan data.
4. Search : fungsi untuk mencarikan data.
5. Sort : fungsi untuk mengurutkan data.


FITUR & FUNGSI


Linked List adalah struktur data dinamis yang sering digunakan dalam pemrograman untuk menyimpan dan memanipulasi data dalam urutan tertentu. Beberapa fitur dan fungsionalitas pemrograman Linked List yang penting antara lain:

1. Memungkinkan penyimpanan data secara dinamis: Linked List memungkinkan data disimpan secara dinamis, sehingga memudahkan penambahan dan penghapusan data tanpa harus memindahkan elemen-elemen lain dalam struktur data.

2. Memudahkan manipulasi data: Linked List memudahkan manipulasi data dalam urutan tertentu. Dengan menggunakan operator-operator seperti insert, delete, traverse, search, dan update, data dalam Linked List dapat dimanipulasi sesuai kebutuhan.

3. Efisien dalam penggunaan memori: Linked List mengalokasikan memori secara dinamis, sehingga hanya membutuhkan ruang yang diperlukan oleh data yang disimpan. Hal ini membuat Linked List efisien dalam penggunaan memori.

4. Fleksibel: Linked List sangat fleksibel karena memungkinkan pengaturan urutan data secara mudah dan cepat. Linked List juga mudah diimplementasikan dalam berbagai bahasa pemrograman.

5. Mampu mengatasi perubahan ukuran data: Jika ukuran data dalam Linked List berubah, struktur data akan menyesuaikan ukuran yang diperlukan. Hal ini membuat Linked List ideal untuk digunakan dalam aplikasi yang membutuhkan perubahan ukuran data yang sering terjadi.

6. Dapat digunakan untuk implementasi struktur data lain: Linked List dapat digunakan sebagai dasar dari struktur data lain seperti stack, queue, dan tree.
