/** @odoo-module **/

import { Component, useState, onWillStart } from '@odoo/owl';
import { jsonrpc } from 'web.rpc';

export class SlotPicker extends Component {
    setup() {
        this.state = useState({
            slots: [],
            selectedSlot: null,
            loading: true,
        });

        onWillStart(async () => {
            const result = await jsonrpc('/letsmeet/slots', {});
            this.state.slots = result;
            this.state.loading = false;
        });
    }

    selectSlot(slot) {
        this.state.selectedSlot = slot;
    }

    async confirmBooking() {
        if (!this.state.selectedSlot) return;
        const payload = {
            slot_id: this.state.selectedSlot.id,
            name: this.el.querySelector('#name').value,
            email: this.el.querySelector('#email').value,
        };
        const result = await jsonrpc('/letsmeet/book', payload);
        alert(result.message);
    }
}
SlotPicker.template = 'letsmeet.SlotPicker';