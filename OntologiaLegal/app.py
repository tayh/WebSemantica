import streamlit as st
import numpy as np
import pandas as pd
from owlready2 import *
import re 

onto = get_ontology("OntologiaLegal.owl").load()

#sync_reasoner()

add_selectbox = st.sidebar.selectbox(
    "OntologiaLegal",
    ("Sobre a ontologia", "Pesquisar", "Inserir")
)


if add_selectbox == 'Sobre a ontologia':


    st.title('Ontologia Legal')
    st.subheader('Classes')

    my_classes = list(onto.classes())
    classes_names = []
    my_propreties = list(onto.data_properties())
    properties_names = []
    my_obj = list(onto.object_properties())
    obj_names = []


    for k in my_classes:
        text = re.split('OntologiaLegal.', str(k))
        classes_names.append(text)

    st.markdown(f"*{', '.join([str(elem[1]) for elem in classes_names])}*")

    st.subheader('Data properties')

    for i in my_propreties:
        text = re.split('OntologiaLegal.', str(i))
        properties_names.append(text)

    st.markdown(f"*{', '.join([str(prop[1]) for prop in properties_names])}*")

    st.subheader('Objective properties')

    for x in my_obj:
        text = re.split('OntologiaLegal.', str(x))
        obj_names.append(text)

    st.markdown(f"*{', '.join([str(prop[1]) for prop in obj_names])}*")

# if st.checkbox('Mostrar Classes'):
#     query_string = """
#     SELECT DISTINCT ?acao 
#     WHERE {
#         ?acao rdf:type ?type .
#         ?type rdfs:subClassOf* OntologiaLegal:Ação .
#         ?acao OntologiaLegal:temMotivo ?m .
#     }
#     """

#     a = list(default_world.sparql(query_string))
#     st.markdown(a)
#     st.markdown(f"*{', '.join([str(elem) for elem in a])}*")