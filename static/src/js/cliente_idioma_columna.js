odoo.define('prueba.cliente_idioma_columna', function (require) {
    const ClientListScreen = require('point_of_sale.ClientListScreen');
    const Registries = require('point_of_sale.Registries');

    const ClienteIdiomaColumna = (ClientListScreen) =>
        class ClientListScreen {
            _getPartnerList() {
                const list = super._getPartnerList();

            }

            _renderList(partners) {
                super._renderList(partners);
                
                };
            }
        };

    Registries.Component.extend(ClientListScreen, ClienteIdiomaColumna);
);
