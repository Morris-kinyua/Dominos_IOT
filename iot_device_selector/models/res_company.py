from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    iot_device_id = fields.Many2one(
        'iot.device',
        string='Fiscal Device',
        domain="[('company_id', '=', id)]",
        help='IoT device assigned to this company for fiscal operations'
    )
    
    @api.constrains('iot_device_id')
    def _check_device_company_match(self):
        for company in self:
            if company.iot_device_id and company.iot_device_id.company_id != company:
                raise UserError(_('Device must be assigned to this company'))
    
    def action_send_to_fiscal_device(self):
        """Override fiscal device send action with device validation"""
        self.ensure_one()
        
        if not self.iot_device_id:
            raise UserError(_('No fiscal device configured for this company. Please select a device.'))
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Select Fiscal Device'),
            'res_model': 'iot.device.selector',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_company_id': self.id, 'default_device_id': self.iot_device_id.id},
        }
