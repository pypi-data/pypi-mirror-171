import logging
from odoo.addons.component.core import Component
from odoo.addons.base_rest.http import wrapJsonException
from werkzeug.exceptions import BadRequest
from odoo import _
from . import schemas

_logger = logging.getLogger(__name__)


class CRMLeadService(Component):
    _inherit = "base.rest.private_abstract_service"
    _name = "crm.lead.services"
    _collection = "ce.services"
    _usage = "crm-lead"
    _description = """
        CRMLead requests
    """

    def create(self, **params):
        company_id = self.env['res.company'].get_real_ce_company_id(params['odoo_company_id']).id
        params.update({'odoo_company_id': company_id})

        sources = {s.name:s.res_id for s in self.env['ir.model.data'].search([
            ('module','=','ce'), ('model','=','utm.source')])}
        if params['source_xml_id'] not in sources:
            raise wrapJsonException(
                BadRequest(
                    _("Source {} not found").format(
                        params["source_xml_id"])
                ),
                include_description=True,
            )

        params.update({'source_xml_id': sources[params['source_xml_id']]})

        try:
            tag_ids = params['tag_ids']
        except:
            tag_ids = False
        if tag_ids:
            for tag_id in tag_ids:
                tag_id_res = self.env['crm.lead.tag'].search([('id','=',tag_id)]).id
                if not tag_id_res:
                    raise wrapJsonException(
                        BadRequest(
                            _("Tag {} not found").format(tag_id)
                        ),
                        include_description=True,
                    )

        params = self._prepare_create(params)
        sr = self.env["crm.lead"].sudo().create(params)
        return self._to_dict(sr)

    def _validator_create(self):
        source = self.work.request.params.get('source_xml_id', False)
        if source == 'ce_source_creation_ce_proposal':
            return schemas.S_CRM_LEAD_CREATE_ALTA_CE
        return schemas.S_CRM_LEAD_CREATE

    def _validator_return_create(self):
        return schemas.S_CRM_LEAD_RETURN_CREATE

    @staticmethod
    def _to_dict(crm_lead):
        return {
            "id": crm_lead.id
        }

    def _prepare_create(self, params):

        contact_name = params.get("partner_firstname", None) or params.get("partner_lastname",None) or None
        if params.get("partner_firstname",None) and params.get("partner_lastname",None):
            contact_name =  "{} {}".format(params.get("partner_firstname",""),params.get("partner_lastname",""))

        vals = {
            "submission_type": 'place_proposal_submission',
            "type": 'opportunity',
            "contact_name": contact_name,
            "name": params.get("partner_name"),
            "description": params.get("partner_description"),
            "street": params.get("partner_full_address"),
            "zip": params.get("partner_zip"),
            "city": params.get("partner_city"),
            "email_from": params.get("partner_email"),
            "phone": params.get("partner_phone"),
            "tag_ids": [(6, 0, params.get("tag_ids", []))],
            "company_id": params.get("odoo_company_id"),
            "source_id": params.get("source_xml_id"),
            "form_submission_metadata_ids": [
                (0,0,{'key':'partner_qty_members','value':params.get("partner_qty_members"),'type':'string'}),
                (0,0,{'key':'partner_legal_state','value':params.get("partner_legal_state"),'type':'string'}),
                (0,0,{'key':'partner_foundation_date','value':params.get("partner_foundation_date"),'type':'string'}),
                (0,0,{'key':'partner_vat','value':params.get("partner_vat"),'type':'string'}),
                (0,0,{'key':'partner_comments','value':params.get("partner_comments"),'type':'string'}),
                (0,0,{'key':'partner_state','value':params.get("partner_state"),'type':'string'}),
                (0,0,{'key':'partner_firstname','value':params.get("partner_firstname"),'type':'string'}),
                (0,0,{'key':'partner_lastname','value':params.get("partner_lastname"),'type':'string'}),
                (0,0,{'key':'contact_email','value':params.get("partner_email"),'type':'string'}),
                (0,0,{'key':'contact2_firstname','value':params.get("contact2_firstname"),'type':'string'}),
                (0,0,{'key':'contact2_lastname','value':params.get("contact2_lastname"),'type':'string'}),
                (0,0,{'key':'contact2_email','value':params.get("contact2_email"),'type':'string'}),
                (0,0,{'key':'contact2_mobile','value':params.get("contact2_mobile"),'type':'string'}),
                (0,0,{'key':'partner_map_place_form_url','value':params.get("partner_map_place_form_url"),'type':'string'}),
                (0,0,{'key':'partner_twitter','value':'','type':'string'}),
                (0,0,{'key':'partner_facebook','value':'','type':'string'}),
                (0,0,{'key':'partner_instagram','value':'','type':'string'}),
                (0,0,{'key':'partner_telegram','value':'','type':'string'}),
                (0,0,{'key':'partner_group_image_url','value':'','type':'string'}),
                (0,0,{'key':'partner_latitude','value':'','type':'string'}),
                (0,0,{'key':'partner_longitude','value':'','type':'string'}),
                (0,0,{'key':'partner_initial_share_amount','value':'100','type':'string'})
                ],
        }
        if params.get("partner_phone", False) and params.get("partner_phone").strip()[:1] in ('6','7'):
            vals['mobile'] = params.get("partner_phone")

        return vals
