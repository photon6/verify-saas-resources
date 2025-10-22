from odoo import http
from odoo.http import request
import json

class LetsMeetController(http.Controller):

    @http.route('/letsmeet/slots', type='json', auth='public', methods=['POST'])
    def get_available_slots(self, **kwargs):
        # Example: Fetch available slots from calendar.event or a custom model
        slots = request.env['calendar.event'].sudo().search([], limit=10)
        return [{
            'id': slot.id,
            'name': slot.name,
            'start': slot.start.strftime('%Y-%m-%d %H:%M'),
            'end': slot.stop.strftime('%Y-%m-%d %H:%M'),
        } for slot in slots]

    @http.route('/letsmeet/book', type='json', auth='public', methods=['POST'])
    def book_slot(self, **kwargs):
        data = request.jsonrequest
        slot_id = data.get('slot_id')
        attendee_name = data.get('name')
        attendee_email = data.get('email')

        slot = request.env['calendar.event'].sudo().browse(slot_id)
        if slot.exists():
            slot.write({
                'partner_ids': [(4, request.env['res.partner'].create({
                    'name': attendee_name,
                    'email': attendee_email
                }).id)]
            })
            return {'status': 'success', 'message': 'Booking confirmed'}
        return {'status': 'error', 'message': 'Slot not found'}