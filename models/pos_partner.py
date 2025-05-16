from odoo import models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        return res

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_fields'].append('lang')
        result['fields'].append('lang')
        return result
