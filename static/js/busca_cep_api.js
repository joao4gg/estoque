let classe;

function limpa_formulario_cep() {
    //Limpa valores do formulário de cep.
    let tela = {
        rua: "",
        bairro: "",
        cidade: "",
        uf: "",
        estado: "",
        ibge: ""
    };

    joga_resultados_tela(tela)
}


function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.

        let tela = {
            rua: conteudo.logradouro,
            bairro: conteudo.bairro,
            cidade: conteudo.localidade,
            uf: conteudo.uf,
            estado: nome_estado(conteudo.uf),
            ibge: conteudo.ibge
        };

        Loading(false);
        joga_resultados_tela(tela);
    } //end if.
    else {
        Loading(false);

        limpa_formulario_cep();
        AlertWarning("Alerta", "CEP não encontrado.");
    }
}

function pesquisacep(valor, origem) {
    classe = origem;
    //Nova variável "cep" somente com dígitos.
    let cep = valor.replace(/[^0-9]/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep !== "") {

        //Expressão regular para validar o CEP.
        let validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {
            Loading(true);

            //Cria um elemento javascript.
            let script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            AlertWarning('Atenção', "Formato de CEP inválido.");
        }
    }
}


function nome_estado(uf) {
    switch (uf) {
        case 'AC':
            return 'Acre';
        case 'AL':
            return 'Alagoas';
        case 'AP':
            return 'Amapá';
        case 'AM':
            return 'Amazonas';
        case 'BA':
            return 'Bahia';
        case 'CE':
            return 'Ceará';
        case 'DF':
            return 'Distrito Federal';
        case 'ES':
            return 'Espírito Santo';
        case 'GO':
            return 'Goiás';
        case 'MA':
            return 'Maranhão';
        case 'MT':
            return 'Mato Grosso';
        case 'MS':
            return 'Mato Grosso do Sul';
        case 'MG':
            return 'Minas Gerais';
        case 'PR':
            return 'Paraná';
        case 'PB':
            return 'Paraíba';
        case 'PA':
            return 'Pará';
        case 'PE':
            return 'Pernambuco';
        case 'PI':
            return 'Piauí';
        case 'RJ':
            return 'Rio de Janeiro';
        case 'RN':
            return 'Rio Grande do Norte';
        case 'RS':
            return 'Rio Grande do Sul';
        case 'RO':
            return 'Rondônia';
        case 'RR':
            return 'Roraima';
        case 'SC':
            return 'Santa Catarina';
        case 'SE':
            return 'Sergipe';
        case 'SP':
            return 'São Paulo';
        case 'TO':
            return 'Tocantins';
    }

}

function joga_resultados_tela(result) {
    if (classe === 'tecnico') {
        document.getElementById('txt_rua_tecnico').value = result.rua;
        document.getElementById('txt_bairro_tecnico').value = result.bairro;
        document.getElementById('txt_cidade_tecnico').value = result.cidade;
        document.getElementById('txt_uf_tecnico').value = result.uf;
    }else if (classe === 'cto'){
        document.getElementById('txt_rua_cto').value = result.rua
        document.getElementById('txt_bairro_cto').value = result.bairro
        document.getElementById('txt_cidade_cto').value = result.cidade
        document.getElementById('txt_estado_cto').value = result.estado
        document.getElementById('txt_uf_cto').value = result.uf
    }else if (classe === '_oper'){
        document.getElementById('txt_rua_oper').value = result.rua
        document.getElementById('txt_bairro_oper').value = result.bairro
        document.getElementById('txt_cidade_oper').value = result.cidade
        document.getElementById('txt_estado_oper').value = result.estado
        document.getElementById('txt_uf_oper').value = result.uf
        document.getElementById('txt_codigo_ibge_oper').value = result.ibge
    }else if (classe === '_parc'){
        document.getElementById('txt_rua_parc').value = result.rua
        document.getElementById('txt_bairro_parc').value = result.bairro
        document.getElementById('txt_cidade_parc').value = result.cidade
        document.getElementById('txt_estado_parc').value = result.estado
        document.getElementById('txt_uf_parc').value = result.uf
        document.getElementById('txt_codigo_ibge_parc').value = result.ibge
    }else if (classe === '_mud_end_new'){
        document.getElementById('txt_rua_mud_end_new').value = result.rua
        document.getElementById('txt_numero_mud_end_new').value = ''
        document.getElementById('txt_bairro_mud_end_new').value = result.bairro
        document.getElementById('txt_cidade_mud_end_new').value = result.cidade
        document.getElementById('txt_estado_mud_end_new').value = result.estado
        document.getElementById('txt_uf_mud_end_new').value = result.uf
        document.getElementById('txt_codigo_ibge_mud_end_new').value = result.ibge
    }
    else{
        if (classe !== "_cid") {
            if (result.rua !== ""){
                document.getElementById('txt_rua' + classe).value = result.rua;
            }
            if (result.bairro !== ''){
                document.getElementById('txt_bairro' + classe).value = result.bairro;
            }
        }
        if (result.cidade !== ''){
            document.getElementById('txt_cidade' + classe).value = result.cidade;
        }

        if(result.uf !== ''){
            document.getElementById('txt_uf' + classe).value = result.uf;
        }

        if(result.ibge !== ''){
            document.getElementById('txt_codigo_ibge' + classe).value = result.ibge;
        }

        if(result.estado !== ''){
            document.getElementById('txt_estado' + classe).value = result.estado;
        }
    }

}