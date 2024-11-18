alert('Boas-vindas ao jogo do número secreto!'); //cria um alerta
let numeroSecreto = 5; //camelCase
console.log(numeroSecreto);
let chute;
let tentativas = 1;

//enquanto
while (chute != numeroSecreto) {
    chute = prompt('Escolha um número entre 1 e 10');

    if (numeroSecreto == chute) {
        alert(`Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas!`);
    } else {
        if (numeroSecreto > chute) {
            alert(`O número secreto é maior que ${chute}`);
        }
        else {
            alert(`O número secreto é menor que ${chute}`);
        }
    }
    //mesma coisa de tentativas += 1
    tentativas ++;
}
// live server (extensão que baixamos) faz com que não precise ficar 
// reinicializando a pag pra testar o código

