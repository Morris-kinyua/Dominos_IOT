from odoo import models


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf_prepare_streams(self, report_ref, data, res_ids=None):
        # EXTENDS 'base'
        # Auto-select company's default IoT device if no device specified
        collected_streams = super()._render_qweb_pdf_prepare_streams(report_ref, data, res_ids)
        
        report = self._get_report(report_ref)
        if not report.device_ids and self.env.company.iot_device_id:
            report.device_ids = [(4, self.env.company.iot_device_id.id)]
        
        return collected_streams

    def render_document(self, device_id_list, res_ids, data=None):
        # EXTENDS 'iot'
        # If no devices specified, use company default
        if not device_id_list and self.env.company.iot_device_id:
            device_id_list = [self.env.company.iot_device_id.id]
        
        return super().render_document(device_id_list, res_ids, data)
