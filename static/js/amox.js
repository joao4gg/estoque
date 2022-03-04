function AlertSuccess(head, text, time = 3) {
    $('body').toast({
        title: head,
        message: text,
        showProgress: 'bottom',
         //make it look like 2.7.0
        showIcon: true,
        position: 'top right',
        progressUp: true,
        classActions: 'attached',
        class: 'success',
        opacity: 1,
        horizontal: true,
        className: {
            box:'toast-box',
            title:'header',
            icon: 'icon'
        },
        displayTime: time * 1000,
      })
    ;

}

function AlertDanger(head, text, time = 5) {
    $('body').toast({
        title: head,
        message: text,
        showProgress: 'bottom',
         //make it look like 2.7.0
        showIcon: true,
        position: 'top right',
        progressUp: true,
        classActions: 'attached',
        class: 'error',
        opacity: 1,
        className: {
            box:'toast-box',
            title:'header',
            icon: 'icon'
        },
        displayTime: time * 1000,
      })
    ;
}

function AlertWarning(head, text, time = 5) {
    $('body').toast({
        title: head,
        message: text,
        closeIcon: true,
        showProgress: 'bottom',
         //make it look like 2.7.0
        showIcon: true,
        position: 'top right',
        progressUp: true,
        classActions: 'attached',
        class: 'warning',
        opacity: 1,
        className: {
            box:'toast-box',
            title:'header',
            icon: 'icon'
        },
        displayTime: time * 1000,
      })
    ;
}

function AlertInfo(head, text, time = 3) {
    $('body').toast({
        title: head,
        message: text,
        showProgress: 'bottom',
         //make it look like 2.7.0
        showIcon: true,
        position: 'top right',
        progressUp: true,
        classActions: 'attached',
        class: 'info',
        opacity: 1,
        className: {
            box:'toast-box',
            title:'header',
            icon: 'icon'
        },
        displayTime: time * 1000,
      })
    ;
}

/**
 * @return {string}
 */

function FormataDataBD(data, dia = '00') {
    let date;
    if (data === '') {
        date = new Date();
    } else {
        if (data.length === 10) {
            date = new Date(data + ' 00:00:00');
        } else {
            date = new Date(data);
        }
    }
    let dd = date.getDate();
    if (dia !== '00') {
        dd = dia;
    }
    let mm = date.getMonth() + 1;
    let yyyy = date.getFullYear();

    if (dd < 10) {
        dd = '0' + dd;
    }

    if (mm < 10) {
        mm = '0' + mm;
    }

    return yyyy + '-' + mm + '-' + dd;
}

function abrir(link) {
    window.open(link.href, link.target, 'width=900, height=600, scrollbars=yes');
}

function open_window_dialog(url) {
    let win = window.open(url.href, url.target, "width=900, height=600, scrollbars=yes");
    let timer = setInterval(function () {
        if (win.closed){
            window.location.reload();
        }
        }, 2000);
}

function Loading(on=true) {
    let layer = document.getElementById('layer');
    let load = document.getElementById('load');
    if (on) {
        load.style.display = 'block';
        layer.style.display = 'block';
    } else {
        load.style.display = 'none';
        layer.style.display = 'none';
    }

}

function fx_placeholder(element) {
    element.innerHTML = '<div class="ui placeholder">' +
        '<div class="image header">' +
        '<div class="line"></div>' +
        '<div class="line"></div>' +
        '</div>' +
        '<div class="paragraph">' +
        '<div class="line"></div>' +
        '<div class="line"></div>' +
        '<div class="line"></div>' +
        '<div class="line"></div>' +
        '<div class="line"></div>' +
        '</div>' +
        '</div>';
}


function uptime(strtime, element) {
    let data = moment(strtime);
    let now = moment(new Date());

    let ms = moment(now.diff(data));
    let d = moment.duration(ms);

    let struptime = '';

    if (d.days() > 0) {
        if (d.days() === 1) {
            struptime = struptime + '1 Dia '
        } else {
            struptime = struptime + d.days() + ' Dias '
        }
    }

    let h = d.hours().toString().padStart(2, '0');
    let m = d.minutes().toString().padStart(2, '0');
    let s = d.seconds().toString().padStart(2, '0');

    struptime = struptime + h + ':' + m + ':' + s;

    element.innerHTML = struptime;

    setTimeout(uptime, 1000, strtime, element)
}

function apprend_script_popup(element) {
    let script = document.createElement("script");
    script.innerHTML = "$('.abre-popup').popup();";
    element.appendChild(script);
}

function open_boleto(ids, tipo='boleto'){
    let encode = btoa('{"ids":"' + ids + '", "tipo":"' + tipo +'"}')
    let link = '/titulo/boleto_pdf/' + encode
    window.open(link, this, 'width=900, height=600, scrollbars=yes');
}

function question_segunda_via(url){
    ModalCustom("Gerar Segunda Via com vencimento Atualizado",
        "Deseja realmente gerar a segunda via com vencimento atualizado desta cobrança?" +
        "<br> A COBRANÇA ANTERIOR NÃO TERÁ MAIS VALIDADE!",
        function (){
            Loading();

            $.get(url).done(function (){
                location.reload();
            }).fail(function (){
                AlertDanger('Acesso Negado', 'Não foi possível gerar segunda via');
                Loading(false);
            })
        }
    )
}

//---------------- Fim da funções resize textarea---------------------------------------------------------------------//


//---------------- Função envia NFE email-----------------------------------------------------------------------------//
function enviar_nfe(url) {
    ModalCustom(
        'Enviar NFE por e-mail',
        'Deseja realmente enviar a NFE por e-mail?',
        function () {
            Loading(true);
            $.get(url)
                .done(function (data) {
                    let decode = JSON.parse(data);
                    if (!decode.error) {
                        Loading(false);
                        if (decode.path){
                            window.location.href = decode.path
                        }else{
                            location.reload();
                        }
                    } else {
                        Loading(false);
                        location.reload();
                    }
                })
        }
        )
}
//---------------- Fim da função envia NFE email----------------------------------------------------------------------//

//---------------- Função copia código pix ---------------------------------------------------------------------------//
function code_pix_copy(code_pix) {
    let temp = document.createElement('textarea');
    document.body.appendChild(temp);
    temp.value = code_pix;
    temp.select();
    let copy = document.execCommand('copy');
    if (copy){
        AlertInfo('Sucesso', 'Código de pix copiado para área de transferência!');
        document.body.removeChild(temp);
    }else{
        AlertDanger('Erro', 'Erro ao copiar código pix, seu navegador pode não ter suporte a essa função!');
        document.body.removeChild(temp);
    }

}
//---------------- Fim da função copia código pix --------------------------------------------------------------------//

function get_float_money(value){
    value = value.replace('R$', '');
    value = value.replace(' ', '');
    value = value.replace('&nbsp;', '');
    value = value.replace(/\./, '');
    value = value.replace(/,/, '.');
    return parseFloat(value)
}

//---------------- Função data string para data BR -------------------------------------------------------------------//
function dataStringToDataBr(value, mais_um=false){
    let data = new Date(`${value} 00:00:00.0`);
    let dia = ''
    if (mais_um){
        dia = data.getDate() + 1;
    }else{
        dia = data.getDate();
    }
    let mes = (data.getMonth() + 1).toString().padStart(2, '0');
    let ano = data.getFullYear();
    if (dia < 10) {
        dia = '0' + dia;
    }

    if (`${dia}/${mes}/${ano}`.includes('NaN')){
        return '';
    }else{
        return `${dia}/${mes}/${ano}`;
    }
}
//---------------- Fim data string para data BR ----------------------------------------------------------------------//

//---------------- Função que calcula a diferença de dias entre duas datas -------------------------------------------//
function returnDays(final, inicio){
    let diff = Math.ceil(final.getTime() - inicio.getTime());
    return Math.ceil(diff / (1000 * 60 * 60 * 24));
}
//---------------- Fim da função que calcula a diferença de dias entre duas datas ------------------------------------//

//--------Função para salvar estado ao clicar em gravar---------------------------------------------------------------//
window.onload = function () {
    $('#data_tab').attr('value', 'dados');
};

function salvaEstadoGravar(obj) {
    let tab = obj.id;
    $('#data_tab').attr('value', tab);
}
//--------Fim da função para salvar estado ao clicar em gravar--------------------------------------------------------//