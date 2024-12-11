//Faça um programa para calcular quantas
//latas de verniz serão necessárias para cobrir um
//deque de madeira. O usuário do programa
//informará a largura e o comprimento da superfície a
//ser coberta e o programa deverá imprimir o número
//de latas necessárias (valor inteiro), dado que cada
//lata de verniz cobre até 3 m2 de superfície.

//O programa deverá ter no mínimo 3 funções. Teste o
//programa calculando o necessário para cobrir uma
//superfície de 4.5 x 5m.
//Observação: tente identificar as tarefas que poderão
//constituir diferentes funções e, para cada tarefa,
//especifique os dados de entrada (parâmetros)
//necessários para sua execução e defina se esta
//tarefa produzirá ou não um resultado (retorno).

#include <iostream>
#include <cmath>
using namespace std;


float calculaArea(float altura, float largura){
    float area;
    area = altura * largura;
    return area;
}

float calculaVerniz(float area){
    float latas;
    latas = 3 * area;
    return ceil(latas);
}

int main(){

    float altura, largura, area;
    cout << "Informe a altura e a largura do espaco: ";
    cin >> altura >> largura;
    cout << calculaVerniz(calculaArea(altura, largura));

    return 0;
}