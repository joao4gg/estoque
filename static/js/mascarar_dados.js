//Mascarar campos de celular/telefone
function Mask(){
    let selector = document.getElementsByClassName('mask_fone');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'fone', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_cnpj');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'cnpj', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_cpf');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'cpf', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_money');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'currency', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_integer');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'integer', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_percent');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'percentage', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_float');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'float', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_ip');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'ip', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_ip_network');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'ip_network_mask', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_mac');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'mac', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_cep');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'cep', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_port');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'port', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_vlan');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'vlan', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_sn_onu');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:'sn_onu', greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_hour');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:"hh:mm", greedy: true}).mask(selector[i])
    }

    selector = document.getElementsByClassName('mask_cto');
    for (let i = 0; i < selector.length; i++){
        new Inputmask({alias:"cto", greedy: true}).mask(selector[i])
    }
}



Mask();

function somenteNumeros(num) {
    let campo = num;
    campo.value = campo.value.replace(/[^0-9]/g, '');
}





