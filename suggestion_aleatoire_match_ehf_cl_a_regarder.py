# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 18:28:06 2025

@author: licke
"""

###############################################################################

import pandas as pd
from itertools import permutations
from random import randint

import streamlit as st

###############################################################################

dico_clubs_ehf_cl_2024_2025 = {'Magdeburg' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jas-vqiyU1EEv0Gle-zAuCXAxYeahQz2Tdr7NVcc_CEVA' , 
                               'Berlin' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jaVwris8oNdHutJDAyJzJKzPNSjnbsbpM3lmqWrk8W6VA' , 
                               'Nantes' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jb8UDY5c25BnXnrltBstWeDg5BPv8oN6mvKBz0iAkOdkQ' , 
                               'Barcelone' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZO9QYuPwVD5p3itiYrR1zs0i6hTdKjwD8KRXJVN3v2wA' , 
                               'Veszprem' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jYN1mFoaGtZK7Q2XbsRieROd4JR3dt7CrAp8luKKcjBoA' , 
                               'Szeged' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZoP04aH1HnhzNTDSzrxhvyhxLtlbccItvTCM7kjIguYQ' , 
                               'Lisbonne' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZrtJvzFKCziAF7eNmM75-rGi61TfqEyKqdTspM44aGTw' , 
                               'Aalborg' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZt2KaYfYuN3wmKca4Tj18-VWALld7uxQXthroRI82qtg' , 
                               'Plock' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZl3n8H8B3RtadCIEeEQaeDnNuZm2S7pqnD1YOUlfzweg' , 
                               'Kielce' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jb2qoyLX6VCZwe2F8Tc756m_3ygGKTOqfHbNFLGIYOxKg' , 
                               'Bucarest' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZl3n8H8B3RtadCIEeEQaeDSIUurUKa9065SM42DaxGBQ' , 
                               'Paris' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jYFdCGWBmbq_74okUEKCu7zGulR2kNcQStcOSCtowKsDA' , 
                               'Zagreb' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZO9QYuPwVD5p3itiYrR1zsFyhz4ZGXD27To919BkMHlg' , 
                               'Kolstad' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jazpdDoU-abLHDLPqhbVk3CH7prf8ABfR92-8_eoEWdUw' , 
                               'Pelister' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jZFA9T9Z_gZJA4IDvW8cL913L6qbNAQ4_AgnNuKRU9PFw' ,
                               'Fredericia' : 'https://res.ehf.eu/doxtore/TLCEQLGQDD/e1GDx4hAd4m3OP2MUjZsUblI3hAS2CVXmCLcWXth6jaujFvAe9ZQ5F660W4sYuXzgoLdeOLdEn32r56O0w3aEQ'}



dico_groupes_ehf_cl_2024_2025 = {'Phase de groupes' : {'A' : ['Veszprem' , 'Lisbonne' , 'Berlin' , 'Paris' , 'Bucarest' , 'Plock' , 'Pelister' , 'Fredericia'] , 
                                                       'B' : ['Barcelone' , 'Aalborg' , 'Nantes' , 'Magdeburg' , 'Szeged' , 'Kielce' , 'Kolstad' , 'Zagreb']} , 
                                 
                                 'Playoffs' : {'PO1' : ['Bucarest' , 'Magdeburg'] , 
                                               'PO2' : ['Kielce' , 'Berlin'] , 
                                               'PO3' : ['Szeged' , 'Paris'] , 
                                               'PO4' : ['Plock' , 'Nantes']} , 
                                 
                                'Quarts de finale' : {'QF1' : ['Magdeburg' , 'Veszprem'] , 
                                                      'QF2' : ['Nantes' , 'Lisbonne'] , 
                                                      'QF3' : ['Szeged' , 'Barcelone'] , 
                                                      'QF4' : ['Berlin' , 'Aalborg']}}

###############################################################################

# Construction du DataFrame des matchs de phase de groupes de la saison 2024-2025 :

A = dico_groupes_ehf_cl_2024_2025['Phase de groupes']['A']
B = dico_groupes_ehf_cl_2024_2025['Phase de groupes']['B']

L_matchs_groupe_A = list(permutations(A,2))
L_matchs_groupe_B = list(permutations(B,2))
L_matchs_phase_groupes = L_matchs_groupe_A + L_matchs_groupe_B
nbr_matchs_phase_groupes = len(L_matchs_phase_groupes)

L_clubs_dom_matchs_phase_groupes = [couple[0] for couple in L_matchs_phase_groupes]
L_clubs_ext_matchs_phase_groupes = [couple[1] for couple in L_matchs_phase_groupes]

df_matchs_phase_groupes = pd.DataFrame(data = {'phase' : nbr_matchs_phase_groupes*['phase de groupes'] , 
                                               'domicile' : L_clubs_dom_matchs_phase_groupes , 
                                               'extérieur' : L_clubs_ext_matchs_phase_groupes})



# Construction du DataFrame des matchs de playoffs de la saison 2024-2025 :

PO1 = dico_groupes_ehf_cl_2024_2025['Playoffs']['PO1']
PO2 = dico_groupes_ehf_cl_2024_2025['Playoffs']['PO2']
PO3 = dico_groupes_ehf_cl_2024_2025['Playoffs']['PO3']
PO4 = dico_groupes_ehf_cl_2024_2025['Playoffs']['PO4']

L_matchs_PO1 = list(permutations(PO1,2))
L_matchs_PO2 = list(permutations(PO2,2))
L_matchs_PO3 = list(permutations(PO3,2))
L_matchs_PO4 = list(permutations(PO4,2))
L_matchs_playoffs = L_matchs_PO1 + L_matchs_PO2 + L_matchs_PO3 + L_matchs_PO4
nbr_matchs_playoffs = len(L_matchs_playoffs)

L_clubs_dom_matchs_playoffs = [couple[0] for couple in L_matchs_playoffs]
L_clubs_ext_matchs_playoffs = [couple[1] for couple in L_matchs_playoffs]

df_matchs_playoffs = pd.DataFrame(data = {'phase' : nbr_matchs_playoffs*['playoffs'] , 
                                          'domicile' : L_clubs_dom_matchs_playoffs , 
                                          'extérieur' : L_clubs_ext_matchs_playoffs})



# Construction du DataFrame des matchs de quarts de finale de la saison 2024-2025 :

QF1 = dico_groupes_ehf_cl_2024_2025['Quarts de finale']['QF1']
QF2 = dico_groupes_ehf_cl_2024_2025['Quarts de finale']['QF2']
QF3 = dico_groupes_ehf_cl_2024_2025['Quarts de finale']['QF3']
QF4 = dico_groupes_ehf_cl_2024_2025['Quarts de finale']['QF4']

L_matchs_QF1 = list(permutations(QF1,2))
L_matchs_QF2 = list(permutations(QF2,2))
L_matchs_QF3 = list(permutations(QF3,2))
L_matchs_QF4 = list(permutations(QF4,2))
L_matchs_quarts = L_matchs_QF1 + L_matchs_QF2 + L_matchs_QF3 + L_matchs_QF4
nbr_matchs_quarts = len(L_matchs_quarts)

L_clubs_dom_matchs_quarts = [couple[0] for couple in L_matchs_quarts]
L_clubs_ext_matchs_quarts = [couple[1] for couple in L_matchs_quarts]

df_matchs_quarts = pd.DataFrame(data = {'phase' : nbr_matchs_quarts*['quarts de finale'] , 
                                        'domicile' : L_clubs_dom_matchs_quarts , 
                                        'extérieur' : L_clubs_ext_matchs_quarts})



# Construction du DataFrame de tous les matchs de la saison 2024-2025 :

df_matchs = pd.concat([df_matchs_phase_groupes , df_matchs_playoffs , df_matchs_quarts] , axis = 0)
df_matchs.index = range(len(df_matchs))

###############################################################################
            
st.set_page_config(page_title = "suggestion_match_ehf_cl" , 
                   layout = "wide") # occupation de toute la largeur de la page

logo_ehf_cl = "https://ehfcl.eurohandball.com/media/5zmfmbar/ehfwcl202223.png?format=webp&quality=80&v=1d8bed5e4c8b560"
  
  
# Suggestion aléatoire : 
    
def suggestion_aleatoire_match(data) :
    
    
    index_data = data.index
    
    index_min = index_data.min()
    index_max = index_data.max()
    
    index_alea = randint(index_min , index_max)
    match_alea = data.loc[index_alea]
    
    phase_match_alea = match_alea.loc['phase']
    club_domicile_match_alea = match_alea.loc['domicile']
    club_exterieur_match_alea = match_alea.loc['extérieur']
    
    logo_club_domicile_match_alea = dico_clubs_ehf_cl_2024_2025[club_domicile_match_alea]
    logo_club_exterieur_match_alea = dico_clubs_ehf_cl_2024_2025[club_exterieur_match_alea]

    return phase_match_alea, club_domicile_match_alea, club_exterieur_match_alea, logo_club_domicile_match_alea, logo_club_exterieur_match_alea


st.image(logo_ehf_cl , 
           width = 250)

for i in range(2) :
    st.write("")
bouton_nouvel_essai = st.button("Suggestion")
if bouton_nouvel_essai == True :
    
    phase_match_alea, club_domicile_match_alea, club_exterieur_match_alea, logo_club_domicile_match_alea, logo_club_exterieur_match_alea = suggestion_aleatoire_match(data = df_matchs)

    col1, col2, col3 = st.columns(3)

    for i in range(3):
        col1.write("")
    st.write("Suggestion du jour :")
    col1.image(logo_club_domicile_match_alea , 
               caption  = club_domicile_match_alea , 
               width = 100)
    col2.image(logo_club_exterieur_match_alea , 
               caption  = club_exterieur_match_alea , 
               width = 100)
    for i in range(3):
        col3.write("")
    col3.write(f"({phase_match_alea})")
    
    

