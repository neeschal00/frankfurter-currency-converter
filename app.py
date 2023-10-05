import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import format_output


st.title("FX Currency Converter")


currencies_list = get_currencies_list()


if currencies_list is None:
    st.error("Error: Unable to fetch the list of available currencies.")
else:
    
    amount = st.number_input("Enter the amount:", min_value=0.01)
    from_currency = st.selectbox("From Currency:", currencies_list)
    to_currency = st.selectbox("To Currency:", currencies_list)

    
    if st.button("Get Latest Rate"):
        l_date, latest_rate = get_latest_rates(from_currency, to_currency, 1)
        if latest_rate is not None:
            output_text = format_output(l_date,from_currency,to_currency,latest_rate,amount)
            st.markdown(f"""
                ## Latest Rate Conversion

                {output_text}
            """)
        else:
            st.error("Error: Unable to fetch the latest exchange rate.")


    
    selected_date = st.date_input("Select a date:", datetime.date.today())
    
    
    if st.button("Get Historical Rate"):
        historical_rate = get_historical_rate(from_currency, to_currency,str(selected_date),1)
        if historical_rate is not None:
            output_text = format_output(selected_date,from_currency,to_currency,historical_rate,amount)
            st.markdown(f"""
                ## Historical Rate Conversion

                {output_text}
            """)
        else:
            st.error(f"Error: Unable to fetch historical rate for {selected_date}.")











