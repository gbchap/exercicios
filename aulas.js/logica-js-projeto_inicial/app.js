alert('Boas-vindas ao jogo do número secreto!'); //cria um alerta
let numeroMaximo = 100
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1); //camelCase
console.log(numeroSecreto);
let chute;
let tentativas = 1;

//enquanto
while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);

    if (numeroSecreto == chute) {
        break;
    } else {
        if (numeroSecreto > chute) {    
            alert(`O número secreto é maior que ${chute}`);
        } else {
            alert(`O número secreto é menor que ${chute}`);
        }
        //mesma coisa de tentativas += 1
        tentativas ++;
    }
    
}
let palavraTentativa = tentativa > 1 ? 'tentativas' : 'tentativa';
alert (`Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}!`)

// live server (extensão que baixamos) faz com que não precise ficar 
// reinicializando a pag pra testar o código

