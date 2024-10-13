# absen-list

Bikin list absen untuk mahasiswa

* tambah siswa melalui input value by End User

# Cara Clone (Copy) project ini 🍎

## Tools yang harus dimiliki ⚙️

1. Python Interpreter. Minimal versi 3.5+ (3.5 atau lebih). Karena project ini pakai fitur Type Hint :)
2. Shell (CLI). Untuk Windows OS, bisa pakai Windows PowerShell.
3. Git (Control Version System). Install versi terbaru aja.
4. Text Editor. Kita pakai yang sejuta umat. Pakai VSCode.

## Cara Copy Project ini ke local (PC anda) 💻

1. Buka Windows PowerShell.
2. Pastikan Git telah terinstall dengan baik.
   * coba command : "git version"
   * output diharapkan : "git version versi_git_anda"
3. Buat akun github anda melalui web browser. Kunjungi web ini:  https://github.com
4. Pastikan anda berhasil login dengan akun github anda.
5. Kunjungi Repo Project ini dengan link : https://github.com/crafzdog/absen-list
6. Buka kembali Windows PowerShell, masuk ke folder downloads.
7. Copy project init.
   * coba command : "git clone https://github.com/crafzdog/absen-list.git"
   * ouput diharapkan : Di folder downloads akan ada folder "absen-list"
8. Masuk ke folder tersebut.
9. Selesai. Project berhasil di Copy.

*note: project yg di copy defaultnya branch master, jadi yg di copy ke pc anda merupakan branch master atau utama 
## Cara Copy Project branch/cabang tertentu ke local (PC anda) 💻

### Opsi 1 
Dengan ini, Anda mengambil semua cabang di repositori, memeriksa cabang yang Anda tentukan, dan cabang tertentu menjadi cabang lokal yang dikonfigurasi.
 
1. Buka Windows PowerShell.
2. Masukkan command cd untuk menggati direktori folder ke folder Downloads agar saat copy repo, folder akan tersimpan di folder tersebut.

   ```bash
   cd Downloads
   ```
4. Copy project branch fitur-input-data-mahasiswa (sebagai contoh kasus):

   bentuk command :
   ```bash
   git clone -b <branchname> <remote-repo-url>
   ```
   contoh command :
   ```bash
   git clone -b fitur-input-data-mahasiswa https://github.com/crafzdog/absen-list.git
   ```
6. Selesai. Project berhasil di Copy ke folder downloads anda.
   

### Opsi 2
Klon/copy repositori dan ambil satu cabang saja.
 
1. Buka Windows PowerShell.
2. Masukkan command cd untuk menggati direktori folder ke folder Downloads agar saat copy repo, folder akan tersimpan di folder tersebut.

   ```bash
   cd Downloads
   ```
4. Copy project branch fitur-input-data-mahasiswa (sebagai contoh kasus):

   bentuk command :
   ```bash
   git clone --branch <branchname> --single-branch <remote-repo-url>
   ```
   contoh command :
   ```bash
   git clone --branch fitur-input-data-mahasiswa --single-branch https://github.com/crafzdog/absen-list.git
   ```
6. Selesai. Project berhasil di Copy ke folder downloads anda.
