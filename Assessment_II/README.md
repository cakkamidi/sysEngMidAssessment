# Modul Pemesanan Ruangan Odoo

Modul ini berfungsi untuk mengelola master ruangan dan pemesanan ruangan dalam sistem Odoo. Modul ini mencakup:

## Fitur
- **Master Ruangan**: Menyimpan informasi mengenai ruangan seperti nama, tipe, lokasi, kapasitas, dan foto ruangan.
- **Pemesanan Ruangan**: Sistem pemesanan yang mencakup nomor pesanan, pemesan, ruangan, tanggal, dan status pemesanan.
- **Status Pemesanan**: Pemesanan dapat diperbarui dari `Draft` ke `On Going` dan `Done`.
- **Validasi**: 
  - Tidak bisa memesan ruangan yang sudah dipesan pada tanggal yang sama.
  - Nama ruangan dan nama pemesan harus unik.
- **API Tracking**: Endpoint untuk melacak status pemesanan berdasarkan nomor pemesanan.

### API Tracking Pemesanan

- **URL**: `/api/pemesanan/<nomor_pemesanan>`
- **Method**: GET
- **Response**:
  - **Success (200)**:
    ```json
    {
      "status": 200,
      "data": {
        "nomor_pemesanan": "BOOK0001",
        "ruangan": "Meeting Room Kecil",
        "nama_pemesan": "John Doe",
        "tanggal_pemesanan": "2024-01-01",
        "status_pemesanan": "draft",
        "catatan_pemesanan": "Some notes here"
      }
    }
    ```
  - **Error (404)**:
    ```json
    {
      "status": 404,
      "message": "Pemesanan tidak ditemukan"
    }
    ```
  
## Instalasi

1. Salin direktori ini ke folder `addons` Odoo Anda.
2. Restart server Odoo Anda.
3. Aktifkan modul melalui menu Aplikasi di Odoo.

## Penggunaan
- **Master Ruangan**: Digunakan untuk membuat dan mengelola data ruangan.
- **Pemesanan Ruangan**: Membuat pemesanan dan mengatur status pemesanan ruangan.

## Validasi
- Nama ruangan dan nama pemesan harus unik.
- Tidak dapat memesan ruangan pada tanggal yang sudah ada pemesanan.