import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """

    try:

        get_response = requests.get(url=url)

        status_code = get_response.status_code

        if status_code == 200:
            response = get_response.json()
        else:
            response = f"Error: Status Code {status_code}"

        return status_code, response
    
    except Exception as e:
        return 0, str(e)


    


