# checklist
Ejemplo de uso

./queryhostname.py lvmcopasjbnp01 1473773400000 1474378200000

host = lvmcopasjbnp01
fecha inicial = 1473773400000
fecha final = 1474378200000

Para varios host en un for bash:
for servidor in lvemxpasjbbm07 lvemxpasjbbm08 lvemxpasjbbm09 lvemxpasjbbm10 lvemxpasjbbm11 lvemxpasjbbm12; do ./queryhostname.py $servidor 1473773400000 1474378200000; done;
