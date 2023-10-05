
def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """

    rounded_rate = round(rate, 4)
    return rounded_rate
    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    
    if rate != 0:
        inverse_rate = 1 / rate
        rounded_inverse_rate = round(inverse_rate, 4)
        return rounded_inverse_rate
    else:
        return 0



def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """

    #round the rate
    rate = round_rate(rate)
    converted_amount = round_rate * amount
    
    inverse_rate = reverse_rate(rate)

    formatted_output = f"The Conversion rate on {str(date)} From Currency: {from_currency}\
          To Currency: {to_currency} was {str(rate)}, So. {str(amount)} in {from_currency} \
          corresponds to {str(converted_amount)} in {to_currency}. The inverse rate was {str(inverse_rate)}"
    
    return formatted_output
   