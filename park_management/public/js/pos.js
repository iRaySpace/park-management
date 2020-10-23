erpnext.pos.PointOfSale = erpnext.pos.PointOfSale.extend({
  get_customer_info: async function(customer) {
    // initialize cache
    if (!this.__customer_info) this.__customer_info = {};
    if (!this.__customer_info[customer]) {
      this.__customer_info[customer] = await _get_customer_info(customer);
    }
    const customer_info = this.__customer_info[customer];
    _validate_customer_info(customer_info);
    return customer_info;
  },
  set_default_customer: function() {
    this._super();
    this.get_customer_info(this.default_customer).then((res) => {
      this.customer_info = res;
    });
  },
  make_customer: function() {
    this._super();
    this.party_field.$input.on('awesomplete-select', (e) => {
      const customer = e.target.value;
      this.get_customer_info(customer).then((res) => {
        this.customer_info = res;
      })
    });
  },
  validate_add_to_cart: function() {
    const me = this;
    const current_item = this.items[0];

    const has_expired = current_item['item_name'].includes('Resident') && me.customer_info.lease_expired;
    if (has_expired) {
      frappe.throw(__('Lease is already expired. Please pay for the entrance fee'));
    }

    const children_allowed = me.customer_info.pm_children_allowed;
    _validate_allowed(
      this.frm.doc.items,
      current_item,
      children_allowed,
      'Resident Child',
      `Only ${children_allowed} child(ren) allowed`
    );

    const adults_allowed = me.customer_info.pm_adults_allowed;
    _validate_allowed(
      this.frm.doc.items,
      current_item,
      adults_allowed,
      'Resident Adult',
      `Only ${adults_allowed} adult(s) allowed`
    )
  },
});


async function _get_customer_info(customer) {
  const { message: customer_info } = await frappe.call({
    method: "park_management.api.customer.get_customer_info",
    freeze: true,
    args: { customer },
  });
  return customer_info;
}


function _validate_allowed(items, current_item, allowed, type, error_text) {
  const items_length = items
    .filter((item) => item.item_name.includes(type))
    .reduce((total, item) => total + item.qty, 0);
  if (current_item['item_name'].includes(type) && items_length + 1 > allowed) {
    frappe.throw(__(error_text));
  }
}


function _validate_customer_info(customer_info) {
  if (customer_info.lease_expired) {
    frappe.msgprint(__('Lease is expired. Customer has to Pay'));
  }
}
