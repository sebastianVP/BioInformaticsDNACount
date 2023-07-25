#####################
# Import Libraries
#####################
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image



####################
# Page Title
####################

image = Image.open("dna-logo.png")

st.image(image,use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

This apps counts the **nucleotide** composition of query DNA!
***
""")
####################
# Input Text Box
####################

st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nGAACACGTGGAGA\nCTGACTGACTTGCACCC\nCCCCCCCAAAAAAA\nTTTTTGGGGGGGGG\n"
#BOX
# sequence es un textbox y si a la secuencia sequence_input le ponemos los \n podemos con split lines recuperar las lineas,
#  ahora si me salto la primera linea es decir >DNA Query\n solo usare la sequencia de DNA

sequence = st.text_area("Sequence Input",sequence_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # SKIPS THE SEQUENCE NAME(FIRST LINE)
sequence = ''.join(sequence) #concatenates list of string

st.write("""
***
""")

## PRINTS THE INPUT DNA SEQUENCE

st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print Dictionary
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
	      ('A',seq.count('A')),
	      ('T',seq.count('T')),
              ('G',seq.count('G')),
              ('C',seq.count('C'))
             ])

    return d

X  = DNA_nucleotide_count(sequence)
X_label  = list(X)
X_values = list(X.values())

X

### 2. PRINT TEXT

st.subheader('2. Print text')
st.write('There are ' + str(X['A'])+' adenine (A)')
st.write('There are ' + str(X['T'])+' thymine (T)')
st.write('There are ' + str(X['G'])+' quanine (G)')
st.write('There are ' + str(X['C'])+' cytosine (C)')

### 3. Display Dataframe

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X,orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)


### 4. DISPLAY BAR CHAR USING Altair

st.subheader('4. Display Bar chart')

p = alt.Chart(df).mark_bar().encode(
                 x='nucleotide',
                 y='count'
                 )

p = p.properties(
    width= alt.Step(80) #controls width of bar
   )

st.write(p)
