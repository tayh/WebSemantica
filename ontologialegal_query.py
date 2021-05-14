from owlready2 import *

onto = get_ontology("OntologiaLegal.owl").load()

query_string = "SELECT ?s ?p ?o  WHERE {?s ?p ?o .}"

a = list(default_world.sparql(query_string))

#print(list(onto.classes()))

print(a)