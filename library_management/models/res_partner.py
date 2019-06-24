from odoo import fields , models

class Partner():
	_inherit = 'res.partner'
	publish_book_ids = fields.One2many('library.book' , 'publisher_id' , #field for this on_Related field# 
	string = 'Published Books')
	book_ids = fields.Many2many( 'library.book', string='Authored Books')
