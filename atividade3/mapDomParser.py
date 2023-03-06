from xml.dom.minidom import parse
import time
BancoDocument = parse('atividade3/map.osm')

print("Starting DOM Parser...")
i = 0
str = ''
initTime = time.time()
for node in BancoDocument.getElementsByTagName("node"):
	flag = False	
	for tag in node.getElementsByTagName("tag"):
		if tag.getAttribute('k') == 'amenity':
			flag = True
			str = f"Estabelecimento: {i},Lat: {node.getAttribute('lat')}, Lon: {node.getAttribute('lon')}, Tipo: {tag.getAttribute('v')}"
		elif tag.getAttribute('k') == "name":
			str += f", Nome: {tag.getAttribute('v') if tag.getAttribute('v') else 'Não informado'}"
	if flag:
		flag = False
		print(str)
		i+=1
endTime = time.time()
print("Tempo de Execução: ", endTime-initTime)
			

                

			
		