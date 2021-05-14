from franz.openrdf.connect import ag_connect
from franz.openrdf.query.query import QueryLanguage

with ag_connect('OntologiaLegal', host='127.0.0.1', port='10035',
                user='tayh', password='kazu1416') as conn:
    print(conn.size())

query_string = "SELECT ?s ?p ?o  WHERE {?s ?p ?o .}"

tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query_string)
result = tuple_query.evaluate()

with result:
   for binding_set in result:
        s = binding_set.getValue("s")
        p = binding_set.getValue("p")
        o = binding_set.getValue("o")
        print("%s %s %s" % (s, p, o))
