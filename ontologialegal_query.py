from owlready2 import *

onto = get_ontology("OntologiaLegal.owl").load()

sync_reasoner()

query_string = """
SELECT DISTINCT ?acao 
WHERE {
    ?acao rdf:type ?type .
    ?type rdfs:subClassOf* OntologiaLegal:AçãoDanosMorais .
    ?acao OntologiaLegal:temMotivo ?m .
}
"""

a = list(default_world.sparql(query_string))

#print(list(onto.classes()))

print(a)