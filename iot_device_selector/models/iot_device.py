from odoo import fields, models


class IotDevice(models.Model):
    _inherit = 'iot.device'
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        help='Company this device is assigned to'
    )
    device_name = fields.Char(
        string='Device Name',
        help='Friendly name for device identification'
    )
