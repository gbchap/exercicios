alert('Boas-vindas ao jogo do número secreto!'); //cria um alerta
let numeroSecreto = 5; //camelCase
console.log(numeroSecreto)
let chute = prompt('Escolha um número entre 1 e 10');

if (numeroSecreto == chute) {
    alert(`Isso aí! Você descobriu o número secreto ${numeroSecreto}`);
} else {
    alert ('Você errou!')
}
// live server faz com que não precise ficar 
// reinicializando a pag pra testar o código

