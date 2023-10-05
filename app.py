import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("FX Currency Converter")

# Get the list of available currencies from Frankfurter
currencies_list = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies_list is None:
    st.error("Error: Unable to fetch the list of available currencies.")
else:
    # Add input fields for capturing amount, from and to currencies
    amount = st.number_input("Enter the amount:", min_value=0.01)
    from_currency = st.selectbox("From Currency:", currencies_list)
    to_currency = st.selectbox("To Currency:", currencies_list)

    # Add a button to get and display the latest rate for selected currencies and amount
    if st.button("Get Latest Rate"):
        l_date, latest_rates = get_latest_rates(from_currency, to_currency, 1)
        if latest_rates is not None:
            converted_amount = round_rate(amount * latest_rates)
            st.success(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        else:
            st.error("Error: Unable to fetch the latest exchange rate.")


    # Add a date selector (calendar)
    selected_date = st.date_input("Select a date:", datetime.date.today())

    # Add a button to get and display the historical rate for selected date, currencies, and amount
    if st.button("Get Historical Rate"):
        historical_rate = get_historical_rate(selected_date, from_currency, to_currency)
        if historical_rate is not None:
            converted_amount = round_rate(amount * historical_rate)
            st.success(f"{amount} {from_currency} on {selected_date} was equal to {converted_amount} {to_currency}")
        else:
            st.error(f"Error: Unable to fetch historical rate for {selected_date}.")











