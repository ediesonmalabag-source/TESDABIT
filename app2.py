import streamlit as st
from datetime import date

month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

today = date.today()

st.title("Birthdate Age Test")

birth_month = st.selectbox("Month", list(month_map.keys()), key="birth_month")
birth_day = st.selectbox("Day", list(range(1, 32)), key="birth_day")
birth_year = st.selectbox("Year", list(range(1950, today.year + 1)), key="birth_year")

st.write("RAW SELECTION →", birth_month, birth_day, birth_year)

try:
    month_number = month_map[birth_month]
    birthdate = date(int(birth_year), month_number, int(birth_day))
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )
    st.write("DEBUG:", birthdate, "→ Age:", age)
except Exception as e:
    st.write("DEBUG ERROR:", e)
