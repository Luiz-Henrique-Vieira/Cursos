nome = "Luiz"
idade = 18
profissão = "Programador e Tecnico em TI"
linguagem = "Python"
dados = {"Nome": "Luizz", "Idade":18, "Profissão": "Programador e Tecnico em TI"}

print("Nome:%s  Idade: %d  Profissão:%s" % (nome, idade, profissão))

print("Nome:{} Idade:{}   Profissão:{}".format(nome, idade, profissão))

print("Nome:{0} Idade:{1}  Profissão:{2}" .format(nome, idade, profissão))

print("Nome:{1} Idade:{2}  Profissão:{0}" .format(profissão, nome, idade))

print("Nome:{nome}  Idade:{idade}  Profissão:{profissão}".format(nome=nome, idade=idade, profissão=profissão))

print("Nome:{name}  Idade:{age}  Profissão:{proficion}".format(name=nome, age=idade, proficion=profissão))

print("Nome:{nome}  Idade:{idade}  Profissão:{profissão}".format(**dados))


"""#print("Olá, me chamo %s. Tenho %a anos de idade, atualemte estou ctrabando como %s e estou matriculado no curso de %s." % (nome,idade,profissão, linguagem,))

print("Olá, me chamo {}. Tenho {} anos de idade, atualemte estou trabando como {} e estou matriculado no curso de {}.".format(nome,idade,profissão,linguagem))
print("Olá, me chamo {3}. Tenho {0} anos de idade, atualemte estou trabando como {1} e estou matriculado no curso de {2}.".format(idade,profissão,linguagem,nome))"""
