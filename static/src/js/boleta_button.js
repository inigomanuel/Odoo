odoo.define('pos_boleta_button.BoletaButton', function (require) {
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');
    const { useListener } = require('@web/core/utils/hooks');
    const { Component } = owl;

    class BoletaButton extends Component {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }

        onClick() {
            const order = this.env.pos.get_order();
            if (order) {
                order.set_boleta(true);  
                //////////////////
            }
        }
    }

    BoletaButton.template = 'BoletaButton';

    Registries.Component.add(PaymentScreen, BoletaButton);

    return BoletaButton;
});
