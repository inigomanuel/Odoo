odoo.define('prueba.precio_cero_alerta', function (require) {
    const { PosGlobalState } = require('point_of_sale.models');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { patch } = require('@web/core/utils/patch');

    patch(ProductScreen.prototype, {
        async _clickProduct(evento) {
            const producto = evento.detail;
            if (producto.lst_price === 0) {
                await this.showPopup('ErrorPopup', {
                    title: 'Alerta de Precio',
                    body: 'Este producto tiene un precio de S/ 0.0. Por favor verifica.',
                });
                return; // No añade
            }
        },
    });
});
