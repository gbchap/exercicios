a_f = "AAAAAA"
b_f = "B"
c_f = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a_f, nome2=b_f, nome3=c_f
    )

print (formato)



#ou pode ser escrito da seguinte forma (sem o uso de strings):
"""
a = "AAAAAA"
b = "B"
c = 1.1

formato = 'a={nome1} b={nome2} c={nome3:.2f}'

print (formato.format(nome1=a, nome2=b, nome3=c))

"""

#ou dessa, também sem  uso de string mas mais parecida
#com a primeira, só que mais direta:

"""
a = "AAAAAA"
b = "B"
c = 1.1
formato = 'a={0} b={1} c={2}'.format(a, b, c)

print (formato)

"""