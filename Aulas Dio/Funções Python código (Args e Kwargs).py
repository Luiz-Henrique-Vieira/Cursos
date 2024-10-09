def exibir_texto(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_texto(
        "Terça-feira, 27 de Agosto de 2024.",
        "Olá, me chamo Luiz.",
        "Tenho 18 anos.",
        "Quero ter como profissão, programador e cientista de dados.",
        "Atualemte estou trabalhando na Recofer.",
         autor = "Luiz", 
         ano= 2024
         )
