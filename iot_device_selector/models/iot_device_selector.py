from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IotDeviceSelector(models.TransientModel):
    _name = 'iot.device.selector'
    _description = 'IoT Device Selector'
    
    company_id = fields.Many2one('res.company', required=True)
    device_id = fields.Many2one(
        'iot.device',
        string='Select Device',
        domain="[('company_id', '=', company_id)]",
        required=True
    )
    available_devices = fields.Many2many(
        'iot.device',
        compute='_compute_available_devices',
        string='Available Devices'
    )
    
    @api.depends('company_id')
    def _compute_available_devices(self):
        for wizard in self:
            wizard.available_devices = self.env['iot.device'].search([
                ('company_id', '=', wizard.company_id.id)
            ])
    
    def action_confirm_device(self):
        """Validate device and proceed with fiscal operation"""
        self.ensure_one()
        
        if self.device_id.company_id != self.company_id:
            raise UserError(
                _('Wrong device selected. Device "%s" is not assigned to company "%s"',
                  self.device_id.device_name or self.device_id.name,
                  self.company_id.name)
            )
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Fiscal Device Operation'),
            'res_model': 'account.move',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_company_id': self.company_id.id,
                'iot_device_id': self.device_id.id,
            },
        }
