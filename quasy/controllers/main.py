from odoo import http
from odoo.http import request

class QuasyController(http.Controller):
    @http.route('/quasy/anonymize', type='json', auth='public', methods=['POST'])
    def anonymize_query(self, query=None):
        if not query:
            return {'error': 'No query provided'}
        anonymizer = request.env['quasy.anonymizer']
        result = anonymizer.anonymize_text(query)
        return {'anonymized_query': result}