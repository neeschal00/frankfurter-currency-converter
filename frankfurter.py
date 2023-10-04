from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list() -> list:
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """

    currency_url = BASE_URL + "/currencies"

    status_code, currency_json = get_url(currency_url)

    if status_code == 0:
        return None
    
    # currency_list = [str(key)+" - "+str(value) for key,value in currency_json.items()]

    return list(currency_json.keys())


    

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """

    converter_url = BASE_URL+ f"/latest?amount={amount}&from={from_currency}&to={to_currency}"

    status_code, response = get_url(converter_url)

    if status_code == 0:
        return None
    
    l_date = None 
    conversion_rate = None

    if response["date"]:
        l_date = response["date"]
    if response["rates"][to_currency]:
        conversion_rate = float(response["rates"][to_currency])

    return l_date,conversion_rate

    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """

    history_url = BASE_URL+ f"/{from_date}?amount={amount}&from={from_currency}&to={to_currency}"

    status_code, response = get_url(history_url)

    if status_code == 0:
        return None
    
    
    conversion_rate = None

    if response["rates"][to_currency]:
        conversion_rate = float(response["rates"][to_currency])

    return conversion_rate

    



if __name__ == "__main__":
    resp = get_latest_rates("AUD","USD",50)
    print(resp)