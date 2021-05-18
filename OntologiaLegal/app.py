import streamlit as st
import numpy as np
import pandas as pd
from owlready2 import *
import re 

def normalize_text(ontology):
    my_objs = []
    for x in ontology:
        text = re.split('OntologiaLegal.', str(x[0]))
        my_objs.append(text)

    return f"*{', '.join([str(elem[1]) for elem in my_objs])}*"
    #return my_objs

onto = get_ontology("OntologiaLegal.owl").load()

#sync_reasoner()

add_selectbox = st.sidebar.selectbox(
    "OntologiaLegal",
    ("Sobre a ontologia", "Ações", "Processos")
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

elif add_selectbox == 'Ações':
    st.header('Ações')
    st.subheader('Pesquise o motivo da ação')

    with st.form("my_form"):
        acao = st.text_input('Motivo')

        submitted = st.form_submit_button("Pesquisar")
        if submitted:
            if acao != '':
                query_string = ("""
                    SELECT DISTINCT ?acao 
                    WHERE {
                        ?acao rdf:type ?type .
                        ?type rdfs:subClassOf* OntologiaLegal:Ação .
                        ?acao OntologiaLegal:temMotivo ?m .
                        FILTER(?m = "%s") .
                    }
                    """%acao)

                #st.code(query_string)
                a = list(default_world.sparql(query_string))
                #st.markdown(a)
                st.markdown(normalize_text(a))
            else:
                st.markdown('Nada encontrado')

elif add_selectbox == 'Processos':
    st.header('Processos')

    query_string2 = ("""
        SELECT DISTINCT ?acao 
        WHERE {
            ?acao rdf:type ?type .
            ?type rdfs:subClassOf* OntologiaLegal:Processo .
        }
        """)

    query_string = ("""
        SELECT DISTINCT ?acao 
        WHERE {
            ?acao rdf:type ?type .
            ?type rdfs:subClassOf* OntologiaLegal:Ação .
            ?acao OntologiaLegal:temMotivo ?m .
            ?acao OntologiaLegal:temProcesso ?p .
        }
        """)

    #st.code(query_string)
    a = list(default_world.sparql(query_string))
    b = list(default_world.sparql(query_string2))

    for i in range(len(b)):
        p = str(b[i][0]).replace('OntologiaLegal.', '')
        m = str(a[i][0]).replace('OntologiaLegal.', '')
        st.subheader(p)
        st.text('Motivo:')
        st.markdown(m)
        st.text('---------------------------------------------')
