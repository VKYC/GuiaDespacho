from odoo import fields, models, api, _


class dteEmail(models.Model):
    '''
    Email for DTE stuff
    '''
    _inherit = 'res.company'

    dte_email = fields.Char(
            'DTE Email',
            related='partner_id.dte_email'
    )
    dte_service_provider = fields.Selection(
        (
            ('SIIHOMO', 'SII - Certification process'),
            ('SII', 'www.sii.cl'),
        ), 'DTE Service Provider', help='''Please select your company service \
provider for DTE service. Select \'None\' if you use manual invoices, fiscal \
controllers or MiPYME Sii Service. Also take in account that if you select \
\'www.sii.cl\' you will need to provide SII exempt resolution number in order \
to be legally enabled to use the service. If your service provider is not \
listed here, please send us an email to soporte@blancomartin.cl in order to \
add the option.
''', default='SIIHOMO')
    dte_resolution_number = fields.Char(
        string='SII Exempt Resolution Number',
        help='''This value must be provided \
and must appear in your pdf or printed tribute document, under the electronic \
stamp to be legally valid.''',
        default='0',
    )
    dte_resolution_date = fields.Date(
            'SII Exempt Resolution Date',
    )
    sii_regional_office_id = fields.Many2one(
        'sii.regional.offices',
        string='SII Regional Office',
        )
    state_id = fields.Many2one(
            "res.country.state",
            'Ubication',
            domain="[('country_id','=',country_id),('type','=','normal')]",
        )

    company_activities_ids = fields.Many2many(
        string='Activities Names',
        related='partner_id.partner_activities_ids',
        relation='partner.activities')
