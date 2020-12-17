#!/bin/sh

cd Modulos

echo "Testando módulos:\n"

echo "Testando Banco_de_dados:"
python3 Testa_Banco_de_dados.py | grep 'FAIL'

echo "Testando Dado:"
python3 Testa_Dado.py | grep 'FAIL'

echo "Testando Partida:"
python3 Testa_Partida.py | grep 'FAIL'

echo "Testando Peao:"
python3 Testa_Peao.py | grep 'FAIL'

echo "Testando Player:"
python3 Testa_Player.py | grep 'FAIL'

echo "Testando Tabuleiro:"
python3 Testa_Tabuleiro.py | grep 'FAIL'

echo "Testando Main:"

python3 Testa_Main.py | grep 'FAIL'

