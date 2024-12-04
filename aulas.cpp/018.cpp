//Construa um programa que aplique um
//desconto de 25% sobre o preço de um produto
//recebido como entrada e imprima o valor
//resultante. Verifique se o programa está
//correto fazendo o teste de mesa. Use o valor
//150.00 como entrada.

#include <iostream>
using namespace std;

int main()
{

    float precoProd;
    float precoDesconto;

    cout << "Digite o preco original do produto: ";
    cin >> precoProd;

    precoDesconto = precoProd - (precoProd * 0.25);
    
    cout << "O seu novo preco com desconto e " << precoDesconto;

    return 0;

}