AI-Based Smart Queue Waiting Time Advisor

1) Project Description

The AI-Based Smart Queue Waiting Time Advisor is a web-based application that estimates the waiting time of a queue using LangChain, Gemini AI, and Fuzzy Logic.

The user can describe the queue in simple natural language, such as the number of people waiting, number of active counters, and average service time. The LangChain-based AI component extracts the required information from the user's description. The extracted values are then processed using a Fuzzy Inference System to estimate the waiting time.

The application is developed using Python and Streamlit and is deployed using Streamlit Community Cloud.

2) Main Features

- Accepts queue information in natural language.
- Uses LangChain and Gemini AI to extract queue details.
- Extracts:
  - Number of people waiting
  - Average service time per person
  - Number of active counters
- Uses Fuzzy Logic for waiting-time estimation.
- Uses fuzzy membership functions for queue length, service time, and number of counters.
- Applies fuzzy rules to evaluate the queue condition.
- Uses defuzzification to generate the estimated waiting time.
- Provides a simple Streamlit web interface.
- Hosted online using Streamlit Community Cloud.

3) Technologies / Tech Stack

- Programming Language: Python
- AI / LLM: Google Gemini
- LLM Framework: LangChain
- Fuzzy Logic: Scikit-Fuzzy
- Web Framework: Streamlit
- Numerical Computing: NumPy
- Scientific Computing: SciPy
- Graph/Dependency Library: NetworkX
- Environment Variables: python-dotenv
- Version Control: Git and GitHub
- Deployment: Streamlit Community Cloud

4) Project Structure

'''
queue_time_advisor/
│
├── app.py
├── fuzzy_system.py
├── llm_parser.py
├── requirements.txt
├── test_fuzzy.py
├── test_llm.py
├── .gitignore
└── README.md
'''

5) Installation and Setup

1. Clone the Repository

git clone https://github.com/sanchi272/queue_time_advisor.git

2. Open the Project Folder

cd queue_time_advisor

3. Install Required Dependencies

pip install -r requirements.txt

4. Set Up the Gemini API Key

The project requires a Gemini API key for the AI-based queue information extraction.

For local use, add the API key in a ".env" file:

GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"

For the deployed application, the API key is added through Streamlit Secrets.

6) How to Run the Project

Run the Streamlit application using:

python -m streamlit run app.py

The application will open in the web browser.

7) How to Use the Application

1. Open the Smart Queue Waiting Time Advisor.
2. Enter a description of the queue in natural language.
3. Click Estimate Waiting Time.
4. The AI component extracts the queue information.
5. The extracted information is displayed on the screen.
6. The Fuzzy Logic system processes the extracted information.
7. The estimated waiting time is displayed as the final result.

Example Input

There are around 20 people waiting, 2 counters are open and each person takes about 4 minutes.

Example Output

People waiting: 20
Service time: 4.0 minutes/person
Active counters: 2

Estimated Waiting Time: Approximately 45.0 minutes

8) Environment Variables

The project uses the following environment variable:

GOOGLE_API_KEY

The actual API key is kept private and is not included in the GitHub repository.

9) Screenshots

Screenshots of the working application can be added here to demonstrate:

- Main application interface
- Natural-language queue input
- Extracted queue information
- Estimated waiting time result

10) Live Deployment

Live Application:

https://queuetimeadvisor-9jtdsglwani76xw9e4tkbu.streamlit.app/

GitHub Repository:

https://github.com/sanchi272/queue_time_advisor

11) Student Details

Name: Sanchi Sorte
Roll Number: 19056
Project: AI-Based Smart Queue Waiting Time Advisor
