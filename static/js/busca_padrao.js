$(document).ready(function (){
    let order = $('#order').val();
    let direction = $('#direction').val();

    let elements = document.getElementsByClassName('busca');

    for (let i = 0; i < elements.length; i++){
        if(elements[i].attributes[0].value === order){
            if(direction === ""){
                elements[i].children[0].children[0].classList.add('up');
            }else{
                elements[i].children[0].children[0].classList.add('down');
            }
        }
    }

});

$('.busca').on('click', function () {
    let tr = this.parentElement;

    for (let i = 0; i < tr.childElementCount; i++){
        if(tr.children[i] !== this && tr.children[i].childElementCount > 0){
            tr.children[i].children[0].children[0].classList.remove('up');
            tr.children[i].children[0].children[0].classList.remove('down');
        }
    }

    if(this.children[0].children[0].classList.contains('up')){
        this.children[0].children[0].classList.remove('up');
        this.children[0].children[0].classList.add('down');
        $('#direction').val('-');
    }else if(this.children[0].children[0].classList.contains('down')){
        this.children[0].children[0].classList.remove('down');
        this.children[0].children[0].classList.add('up');
        $('#direction').val('');
    }else{
        this.children[0].children[0].classList.add('up');
        $('#direction').val('');
    }

    $('#order').val(this.attributes[0].value);
    $('#action_busca').click();
});

$('#clear').click(function () {
    $('th div input[type = search]').val('');
    $('th div input[type = text]').val('');
    $('th div input[type = date]').val('');
    $('th div input[type = datetime-local]').val('');
    $('th div input[type = time]').val('');
    $('th div select').val('');
    $('.ui.fluid.search.dropdown').find('[value=""]').attr('selected', true);
});

if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}

//--------------------------Função Xlsx---------------------------------------------------------------------------------
$('#floating_xls').click(function () {
    let load = document.getElementById('load');
    let layer = document.getElementById('layer');
    let path = location.pathname;
    let encoded = btoa(`{"path": "${path}"}`);

    load.style.display = 'block';
    layer.style.display = 'block';

    $.get('/exp/' + encoded)
        .done(function (data) {
            let decode = JSON.parse(data);
            if (decode.msg) {
                AlertSuccess('Sucesso', decode.msg, 5)
            } else {
                AlertDanger('Erro', decode.msg_error, 5)
            }

            load.style.display = 'none';
            layer.style.display = 'none';
            //window.open(floating_xls.href = '/' + decode.x);
        })
})
//--------------------------Fim da Xlsx---------------------------------------------------------------------------------