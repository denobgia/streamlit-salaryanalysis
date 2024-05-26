import streamlit as st
import pandas as pd

# Daten aus Excel-Datei laden
data = pd.read_excel('Quelle.xlsx')

# Titel der App
st.title('Datenvisualisierung: Alter und Lohn')

# Sidebar-Einstellungen
st.sidebar.header('Filteroptionen')

# Alter Filter
min_age = int(data['Alter'].min())
max_age = int(data['Alter'].max())
selected_age = st.sidebar.slider('Alter auswählen:', min_age, max_age, (min_age, max_age))

# Daten filtern
filtered_data = data[(data['Alter'] >= selected_age[0]) & (data['Alter'] <= selected_age[1])]

# Median, Minimum und Maximum Lohn berechnen
median_salary = filtered_data['Lohn'].median()
min_salary = filtered_data['Lohn'].min()
max_salary = filtered_data['Lohn'].max()

# Anzeige der Ergebnisse
st.subheader(f'Ergebnisse für die Altersspanne {selected_age[0]} - {selected_age[1]} Jahre')
st.write(f'Medianlohn: {median_salary:.2f}')
st.write(f'Minimum Lohn: {min_salary:.2f}')
st.write(f'Maximum Lohn: {max_salary:.2f}')

# Statistik der gefilterten Daten
st.subheader('Statistik der gefilterten Daten')
st.write(filtered_data.describe())