# Frankfurter-currency-converter

## Description
The Application in general **converts** the curency from one to another with the usage of frankfurter opensource API. The Application has two sections to convert the Currency where **"Get Latest Rate"** is used to convert the given currency to another based on the latest rate available in the API. Whereas the **"Get Historical Rate"** utilizes the Historical Rate based on the selected date to convert. 
The main app imports other python file as modules where different functionalities are imported with each portion seperated out as modules to utilize it and create the application. The application wraps the frankfurter API responses to modify and only take the usable response which is used to make necessary calculations and displayed by formatting the output.

The **Challenges** that was encountered during the development of this application are:
- Formatting the data types to show the response as a output text in the streamlit section.
- Wrapping the API Endpoints to fit the requirements required testing and appropriate modifications for each functionalities.
- Writing a markdown and using it in streamlit along with the README.md itself required verification.
- Organizing the application based on guidelines required some portion to be made more flexible.

The **Features** that would be appropriate to implement in the **future** are:
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
- Streamlit Official Documentation "St.markdown" [Source URL](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- Frankfurter API documentation "Documentation" [Source URL](https://www.frankfurter.app/docs/)
- Jonathan Okah (May 1, 2023) "How I Created a Currency Converter App Using Streamlit" [Source URL](https://blog.finxter.com/how-i-created-a-currency-converter-app-and-a-currency-prediction-app-using-streamlit/)

