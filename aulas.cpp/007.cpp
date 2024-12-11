//a) Considerando Pi = 3,14159, para cada opção
//abaixo, escreva uma função que recebe como
//parâmetro o raio de um círculo e:
//▪ retorne seu diâmetro;
//▪ retorne sua circunferência;
//▪ retorne sua área;
//▪ imprima o diâmetro, a circunferência e a área
//chamando as funções anteriores.
//b) Elabore um programa que leia do teclado o valor
//do raio de dois círculos e, para cada círculo, chame a
//função que imprime as informações.

#include <iostream>
#include <cmath>
const double PI = 3.14159;

using namespace std;

void CaracteristicasCirculo (float raio){
    float diam, circunf, area;
    diam = raio * 2;
    circunf = 2 * PI * raio;
    area = PI * raio * raio;

    cout << "diametro: " << diam <<endl;
    cout << "circunferencia: " << circunf <<endl;
    cout << "area: " << area <<endl;
}
int main(){
    float raio1, raio2;
    cout << "Digite 2 raios para 2 circulos: ";
    cin >> raio1 >> raio2;
    CaracteristicasCirculo(raio1);
    cout << "e, para o outro circulo: " << endl;
    CaracteristicasCirculo(raio2);
    return 0;
}