//Faça uma função que receba como parâmetros o
//valor de uma compra e o número de parcelas e
//imprima o valor da parcela a ser paga a prazo.
//Ao ser executada em um programa com as entradas
//3530.8 e 14, sua função deverá imprimir:

//COMPRA A PRAZO
//Valor da compra: R$ 3530.8
//Numero de parcelas: 14
//Valor da parcela a prazo: R$ 252.20


//setprecision()
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

void valorParcela(float valorCompra, float numeroParcelas){

    float valorParcela;
    valorParcela = valorCompra / numeroParcelas;
    cout << "Valor da compra: R$ " << valorCompra << endl;
    cout << "Numero de parcelas: " << numeroParcelas << endl;
    cout << "Valor da parcela a prazo: R$ " << fixed << setprecision(2) << valorParcela;

}

int main(){

    float valorCompra, numeroParcelas;
    cout << "Digite valor da compra e numero de parcelas: ";
    cin >> valorCompra >> numeroParcelas;
    valorParcela(valorCompra, numeroParcelas);
    return 0;
}