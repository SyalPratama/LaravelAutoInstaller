# Laravel Auto Installer (Python CLI)

Skrip Python ini adalah **installer otomatis Laravel berbasis CLI** yang memudahkan proses instalasi Laravel, pemilihan versi, pemasangan paket populer (Breeze, Jetstream, Sanctum, Livewire, Inertia), serta pengaturan awal file `.env` untuk koneksi database.

---

## Fitur

- Instalasi Laravel versi tertentu menggunakan Composer
- Pilih dan install paket tambahan Laravel:
  - `breeze`
  - `jetstream`
  - `sanctum`
  - `livewire`
  - `inertia`
- Update otomatis konfigurasi `.env` untuk koneksi database
- Interface interaktif via terminal/command prompt

---

## Prasyarat

Pastikan kamu sudah menginstal:

- Python 3.x
- PHP >= 8.1
- Composer
- Git (opsional, untuk clone repo)

---

## Cara Menggunakan

### 1. Clone Repository

```bash
git clone https://github.com/SyalPratama/LaravelAutoInstaller.git
cd LaravelAutoInstaller
```
### 2. Jalankan Installer

```bash
python laravel.py
```

### 3. Ikuti Langkah-langkah di Terminal

- Masukkan nama proyek Laravel
- Pilih versi Laravel
- Pilih paket tambahan (opsional)
- Pilih driver database (mysql atau pgsql)

### 4. Jalankan Laravel

```bash
cd nama_proyek_anda
php artisan serve
```

## Contoh Output

![Tampilan Installer](https://raw.githubusercontent.com/SyalPratama/LaravelAutoInstaller/refs/heads/main/Laravel.png)
