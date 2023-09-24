import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]["infNFe"]
        else:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        nuemro_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]["xNome"]
        nome_cliente = infos_nf["dest"]["xNome"]
        rua = infos_nf["dest"]["enderDest"]["xLgr"]
        cep = infos_nf["dest"]["enderDest"]["CEP"]
        bairro = infos_nf["dest"]["enderDest"]["xBairro"]
        cidade = infos_nf["dest"]["enderDest"]["xMun"]
        #endereco = infos_nf["dest"]["enderDest"]
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"
        valores.append([nuemro_nota, empresa_emissora, nome_cliente, rua, cep, bairro, cidade, peso])


lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "rua", "cep", "bairro", "cidade", "peso"]
valores = []

for arquivos in lista_arquivos:
    pegar_infos(arquivos, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
print(tabela)
tabela.to_excel("NotasFiscais.xlsx", index=False)