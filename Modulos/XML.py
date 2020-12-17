from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom
import xml.etree.cElementTree as ET

def Cria_xml():
    historico = ET.Element('Histórico')
    rodada = ET.SubElement(historico, 'Rodada')
    rodada.text = '1'
    localizacao = ET.SubElement(historico, 'Cor')
    azul = ET.SubElement(localizacao, 'Azul')
    vermelho = ET.SubElement(localizacao, 'Vermelho')
    verde = ET.SubElement(localizacao, 'Verde')
    amarelo = ET.SubElement(localizacao, 'Amarelo')
    cores = [azul, vermelho, verde, amarelo]
    posicoes_1 = [(330, 522), (285, 85), (725, 30), (770, 478)]
    posicoes_2 = [(260, 595), (205, 155), (655, 110), (700, 548)]
    posicoes_3 = [(400, 595), (355, 155), (795, 110), (850, 548)]
    posicoes_4 = [(330, 675), (285, 225), (725, 180), (770, 618)]
    for i in range(len(cores)):
        peao1 = ET.SubElement(cores[i], 'Peao1')
        peao1.text = str(posicoes_1[i])
        peao2 = ET.SubElement(cores[i], 'Peao2')
        peao2.text = str(posicoes_2[i])
        peao3 = ET.SubElement(cores[i], 'Peao3')
        peao3.text = str(posicoes_3[i])
        peao4 = ET.SubElement(cores[i], 'Peao4')
        peao4.text = str(posicoes_4[i])
    nome_arquivo = 'Salva_XML.xml'
    with open(nome_arquivo, 'w') as file_object:
        file_object.write(Formata_saida(historico))

def Formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent = " ")


def Le_xml():
    with open('../Partidas/Salva_XML.xml', 'rt') as salva:
        tree = ElementTree.parse(salva)
        root = tree.getroot()
    dict_historico = {}
    lista_historico = []
    for historico in root.findall('Histórico'):
        dict_historico = {}
        dict_historico['Rodada'] = historico.find('Rodada').text
        lista_rodada = []
        dict_rodada = {}
        dict_historico['Cor'] = historico.find('Cor').text
        lista_cor = []
        dict_cor = {}
        for rodada in historico.iter('Rodada'):
            dict_rodada = {}
            dict_rodada['num'] = rodada.text
            lista_rodada.append(dict_rodada)
        dict_historico['Rodada'] = lista_rodada
        lista_historico.append(dict_historico)
        for cor in historico.iter('Cor'):
            dict_cor = {}
            dict_cor['Peao'] = cor.find('Peao').text
            for peao in cor.iter('Cor'):
                dict_peao = {}
                dict_peao['Peao'] = cor.find('Peao').text
                lista_peao.append(dict_peao)
            dict_cor['Peao'] = lista_peao
            lista_cor.append(dict_cor)
        dict_historico['Cor'] = lista_cor
        lista_historico.append(dict_historico)
    print(lista_historico)

Cria_xml()
#Formata_saida()
Le_xml()
