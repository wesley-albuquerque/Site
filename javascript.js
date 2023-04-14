const cep = document.getElementById('CEP');
const logradouro = document.getElementById('logradouro');
const complemento = document.getElementById('complemento');
const bairro = document.getElementById('bairro');
const localidade = document.getElementById('cidade');
const uf = document.getElementById('estado');
const pais = document.getElementById('pais');
var fantasia = document.getElementById("divfantasia");


function cepOnchange(){

  var cepRequest = cep.value;
  cepRequest = cepRequest.replace(/\D/g, "");
  
  if(cepRequest != null && cepRequest != ""){

    if(cepRequest.length == 8){
        var req = new XMLHttpRequest();
        req.open("GET", encodeURI("https://viacep.com.br/ws/" + cepRequest + "/json"), false);
    
        req.send(null);
        data = JSON.parse(req.responseText);
        logradouro.value = data.logradouro;
        complemento.value = data.complemento;
        bairro.value = data.bairro;
        localidade.value = data.localidade;
        uf.value = data.uf;
        pais.value = "Brasil";
        cepRequest = cepRequest.replace(/(\d{5})(\d{3})/, "$1-$2");
        cep.value = cepRequest;
    }
  }
}

function onchangeCPF_CNPJ(){
    var cpf_cnpj = document.getElementById("cpf_cnpj");
    cpf_cnpjReq = cpf_cnpj.value
    cpf_cnpjReq = cpf_cnpjReq.replace(/[^\d]/g, "");
    if(cpf_cnpjReq.length == 11){
        if(validaCPF(cpf_cnpjReq)){
            cpf_cnpjReq = cpf_cnpjReq.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
            cpf_cnpj.value = cpf_cnpjReq;
            fantasia.style.display = "none";

        }
        else{
            alert("CPF inválido")
            cpf_cnpj.value = "";
            cpf_cnpj.focus();
        }
    }
    else if(cpf_cnpjReq.length == 14){
        if(validaCNPJ(cpf_cnpjReq)){
            cpf_cnpjReq = cpf_cnpjReq.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5")
            cpf_cnpj.value = cpf_cnpjReq;
            fantasia.style.display = "inline";
        }
        else{
            alert("CNPJ inválido")
            cpf_cnpj.focus();
        }
    }else{
        alert("CPF ou CNPJ inválido")
        cpf_cnpj.value = "";
        cpf_cnpj.focus();
    }
}

function validaCPF(cpf) {
    var rep = 0;
    for (var g = 1; g > 11; g++) {
        if (cpf[0] == cpf[g])
            rep++
    }
    if (rep == 10) {
        return false
    }
    var mult = 11
    var soma1Digito = 0
    var soma2Digito = 0
    for (var i = 0; i < 10; i++) {
        if (i < 9) {
            soma1Digito += cpf[i] * (mult - 1)
        }
        soma2Digito += cpf[i] * mult
        mult--
    }
    var resto = (soma1Digito * 10) % 11
    var resto2 = (soma2Digito * 10) % 11
    if (resto == 10) {
        resto = 0
    }
    if (resto == cpf[9] && resto2 == cpf[10]) {
        return true
    }
    else {
        return false
    }
}

function validaCNPJ(cnpj) {
  
    if (cnpj.length !== 14) { 
      return false;
    }
  
    let soma = 0;
    for (let i = 0; i < 12; i++) {
      soma += parseInt(cnpj.charAt(i)) * (i < 4 ? 5 - i : 13 - i);
    }
    let digito1 = (11 - soma % 11) % 10;
  
    soma = 0;
    for (let i = 0; i < 13; i++) {
      soma += parseInt(cnpj.charAt(i)) * (i < 5 ? 6 - i : 14 - i);
    }
    let digito2 = (11 - soma % 11) % 10;
  
    return (parseInt(cnpj.charAt(12)) === digito1 && parseInt(cnpj.charAt(13)) === digito2);
  }

  function onchangeEmail() {
    var email = document.getElementById("email");
    var emailValida = email.value;
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(email.value != "")
    if(!regexEmail.test(emailValida)){
        alert("E-mail inválido");
        email.focus();
    };

  }

  function enviarDados() {
    
    // Cria um objeto com os valores do formulário
    
      var cpf_cnpj = document.getElementById("cpf_cnpj").value;
      var nome = document.getElementById("nome").value;
      var fantasia = document.getElementById("fantasia").value;
      var email = document.getElementById("email").value;
      var telefone = document.getElementById("telefone").value;
      var celular = document.getElementById("celular").value;
      var CEP = document.getElementById("CEP").value;
      var logradouro = document.getElementById("logradouro").value;
      var complemento = document.getElementById("complemento").value;
      var numero = document.getElementById("numero").value;
      var bairro = document.getElementById("bairro").value;
      var cidade = document.getElementById("cidade").value;
      var estado = document.getElementById("estado").value;
      var pais = document.getElementById("pais").value;
    
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      myHeaders.append("Accept", "*/*");
      myHeaders.append("Accept-Encoding", "gzip, deflate, br");
      myHeaders.append("Connection", "keep-alive");

      
      var raw = JSON.stringify({
        "cpf_cnpj": "123.456.789-03",
        "nome": "Exemplo de Nome",
        "fantasia": "Exemplo de Nome Fantasia",
        "email": "exemplo@exemplo.com",
        "telefone": "(00) 0000-0000",
        "celular": "(00) 00000-0000",
        "CEP": "00000-000",
        "logradouro": "Exemplo de Logradouro",
        "complemento": "Exemplo de Complemento",
        "numero": "123",
        "bairro": "Exemplo de Bairro",
        "cidade": "Exemplo de Cidade",
        "estado": "Ex",
        "pais": "Brasil"
      });
      
      var requestOptions = {
        method: 'OPTIONS',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
      
      fetch("http://127.0.0.1:5000/inserir-dados", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
    }