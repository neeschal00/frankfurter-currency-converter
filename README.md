# frankfurter-currency-converter

## Description
The Application in general **converts** the curency from one to another with the usage of frankfurter opensource API.
<Some of the challenges you faced>

The Features that would be appropriate to implement in the future are:
- Showcase the difference between the rate before and current in the application.
- Use Line Chart to showcase the historical data for a particular currency.
- Create a currency rates comparison based on historical data.

## How to Setup

**Requirements:**
Python Version Used: Python 3.10.11

**Libraries:**
Install Streamlit package which will return all the necesary libraries including http libraries such as requests, pandas, cachetools, etc.
```streamlit==1.27.2```  [Streamlit][1]

**Setup:**
- CD to the project directory:

```
cd frankfuter-currency-converter
```

- Create a Python Virtual Environment:

```
python -m venv venv
```

- Activate the virtual Environment:

```
venv\Scripts\activate
```

or if **linux** or **mac**

```
source venv/bin/activate
```

- Install **Streamlit** package

```
pip install streamlit==1.27.2
```


## How to Run the Program
The **app.py** module consists of all 
```
streamlit run app.py
```

## Project Structure
The project is comprised of four Python files where three files with their names represent the respective logic for that portion.

- **app.py:**
The main application file which consists of necessary code to setup and run the application. It holds the UI components logic and output display logic utilizing the functions from other modules to showcase and display the functionalities seamlessly.

- **README.md:**
The markdown file which holds the documentation information regarding the application. It consists of steps and procedure to run the application along with a brief discription about the project and its structure.

- **api.py**
This python file consists of a function which wraps the process of making a request to a certain endpoint with status code and response(i.e. json for api)

- **currency.py**
This python file holds useful functionalities to calculate the reverse, round the value and create a formatted output to display in the streamlit frontend.

- **frankfurter.py**
This python file holds the functionalities to display the response from different api.frankfurter.com endpoints based on the given instructions.


## Citations:
[1]: https://docs.streamlit.io/library/get-started/installation
- Streamlit Official Documentation "Get-Started Installation" [Source URL](https://docs.streamlit.io/library/get-started/installation)
