import sys

colores = {"aliceblue":"#f0f8ff","antiquewhite":"#faebd7", "aqua": "#00ffff", "aquamarine":"#7fffd4", "azure":"#f0ffff", "darkorchid":"#9932cc",
          "darkred":"#8b0000","darksalmon":"#e9967a", "navajowhite":"#ffdead","navy":"#000080","orchid":"#da70d6"}

search_hexas = sys.argv[1:]
'''
found = False
for name, hexa in colores.items():
    if hexa == search:
        found = True
        print(name)

if not found:
    print("no-no") '''   

colores_inv = {v:k for k, v in colores.items()}

'''
if search in colores_inv:
    print(colores_inv[search])
else:
    print("no-no")'''

for search in search_hexas:
    if search in colores_inv:
        print(colores_inv[search])
    else:
        print("no-no")