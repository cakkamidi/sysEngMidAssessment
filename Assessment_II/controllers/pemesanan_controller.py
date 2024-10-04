from odoo import http
from odoo.http import request, Response

class PemesananRuanganAPI(http.Controller):
    @http.route('/api/pemesanan/<string:nomor_pemesanan>', auth='public', methods=['GET'], type='json', csrf=False)
    def get_pemesanan_status(self, nomor_pemesanan):
        try:
            pemesanan = request.env['ruangan.pemesanan'].sudo().search([('nomor_pemesanan', '=', nomor_pemesanan)], limit=1)
            if not pemesanan:
                return {'status': 404, 'message': 'Pemesanan tidak ditemukan'}

            data = {
                'nomor_pemesanan': pemesanan.nomor_pemesanan,
                'ruangan': pemesanan.ruangan_id.nama_ruangan,
                'nama_pemesan': pemesanan.nama_pemesan,
                'tanggal_pemesanan': pemesanan.tanggal_pemesanan,
                'status_pemesanan': pemesanan.status_pemesanan,
                'catatan_pemesanan': pemesanan.catatan_pemesanan
            }

            return {'status': 200, 'data': data}

        except Exception as e:
            return {'status': 500, 'message': str(e)}