
function ModalCustom(titulo, desc, yes = function () {return true;}, no = function () {return true;}) {
    if (document.getElementById('generic_modal') == null){
        document.getElementById('modal_holder').innerHTML =
            '<div class="ui small modal" id="generic_modal">' +
            '<div class="header" id="header_modal"></div>' +
            '<div class="image content">' +
            '<div class="description" id="desc_modal"></div>' +
            '</div>' +
            '<div class="actions">' +
            '<div class="negative ui button ui df_button_width deny">Não</div>' +
            '<div class="ui positive right labeled icon button df_button_width">Sim<i class="checkmark icon"></i></div>' +
            '</div>' +
            '</div>';
    }

    document.getElementById('header_modal').innerHTML = titulo;
    document.getElementById('desc_modal').innerHTML = desc;

    $('#generic_modal')
        .modal({
            closable: true,
            onDeny: no,
            onApprove: yes
        }).modal('show');

}


