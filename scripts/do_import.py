import rdflib
g=rdflib.Graph()
g.load('http://purl.obolibrary.org/obo/doid.owl')
print g

for s,p,o in g: 
  print s,p,o
