import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("covid_vaccine_statewise.csv")

# Group data by state
state_data = df.groupby('State').sum()

# Bar chart of first dose vaccinations by state
fig1 = px.bar(state_data, x=state_data.index, y='First Dose Administered',
              labels={'x':'State', 'y':'First Dose Vaccinations'},
              title='First Dose Vaccinations by State')

# Bar chart of second dose vaccinations by state
fig2 = px.bar(state_data, x=state_data.index, y='Second Dose Administered',
              labels={'x':'State', 'y':'Second Dose Vaccinations'},
              title='Second Dose Vaccinations by State')

# Bar chart of male vaccinations by state
fig3 = px.bar(state_data, x=state_data.index, y='Male(Individuals Vaccinated)',
              labels={'x':'State', 'y':'Male Vaccinations'},
              title='Male Vaccinations by State')

# Bar chart of female vaccinations by state
fig4 = px.bar(state_data, x=state_data.index, y='Female(Individuals Vaccinated)',
              labels={'x':'State', 'y':'Female Vaccinations'},
              title='Female Vaccinations by State')

# Create dictionary to map state names to index
state_dict = {state:i for i,state in enumerate(state_data.index)}

# Show bar chart based on selected state
def show_state_data(state_name):
    index = state_dict[state_name]
    state_row = df.loc[df['State'] == state_name]
    st.write(state_row)
    st.write(f"Total first dose vaccinations in {state_name}: {state_data.iloc[index]['First Dose Administered']}")
    st.write(f"Total second dose vaccinations in {state_name}: {state_data.iloc[index]['Second Dose Administered']}")
    st.write(f"Total male vaccinations in {state_name}: {state_data.iloc[index]['Male(Individuals Vaccinated)']}")
    st.write(f"Total female vaccinations in {state_name}: {state_data.iloc[index]['Female(Individuals Vaccinated)']}")

# Streamlit app
st.title("COVID-19 Vaccination Data by State")
st.write("Bar charts of vaccinations by state")

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)

# Button to show state data
state_name = st.text_input("Enter a state name:")
if st.button("Show state data"):
    if state_name in state_dict:
        show_state_data(state_name)
    else:
        st.write("Invalid state name")
