from odoo import api, fields, models, _, Command
from odoo.addons.base.models.decimal_precision import DecimalPrecision
from odoo.addons.account.tools import format_rf_reference
from odoo.exceptions import UserError, ValidationError, AccessError, RedirectWarning

class PlanogramView(models.Model):
    _name = "planogram.view"
    _description = 'Planogram Form'

    
