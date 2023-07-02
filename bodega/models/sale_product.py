from odoo import models,fields,api,exceptions

class SaleProduct(models.Model):
    _name='bodega.sale_product'
    _description='Compra de Productos'

    name=fields.Many2one(string="Producto",comodel_name="bodega.purchase_product")
    description=fields.Char(string="Descripcion")
    quanty=fields.Integer(string="Cantidad")
    price_unit=fields.Float(string="Precio/Unit")
    price_total=fields.Float(string="Total")
    detail_invoice_id=fields.Many2one(comodel_name="bodega.detail_invoice")

    @api.model
    def create(self,values):
        return super(SaleProduct,self).create(values)
    
    def btn_delete(self):
        pass

    def btn_update(self):
        pass
    