from odoo import models, fields, api

class PemesananRuangan(models.Model):
    _name = 'ruangan.pemesanan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', readonly=True, required=True, copy=False, default='New')
    ruangan_id = fields.Many2one('ruangan.master', string='Ruangan', required=True)
    nama_pemesan = fields.Char(string='Nama Pemesan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')], string='Status Pemesanan', default='draft')
    catatan_pemesanan = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('unique_nama_pemesan', 'unique(nama_pemesan)', 'Nama pemesan harus unik!'),
        ('unique_ruangan_tanggal', 'unique(ruangan_id, tanggal_pemesanan)', 'Ruangan sudah dipesan pada tanggal tersebut!'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('nomor_pemesanan', 'New') == 'New':
            vals['nomor_pemesanan'] = self.env['ir.sequence'].next_by_code('ruangan.pemesanan') or 'New'
        return super(PemesananRuangan, self).create(vals)

    def action_set_ongoing(self):
        self.status_pemesanan = 'ongoing'

    def action_set_done(self):
        self.status_pemesanan = 'done'