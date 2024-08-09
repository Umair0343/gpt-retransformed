# gpt-retransformed
This project is a Flask-based web application that leverages OpenAI's GPT-3.5-turbo models to perform various natural language processing tasks. Users can interact with the application through a web interface, where they can select a model, provide a prompt, and choose an operation (like sentiment analysis, text classification, translation, summarization, or text completion).

Here is how the main window looks like:
<img width="500" alt="Screenshot 2024-08-09 at 3 51 21 PM" src="https://github.com/user-attachments/assets/2f3d5fa1-8106-4409-9e9e-9ece8f99f34a">

Clicking on the "Completions" button will take you to the next window in which you can design/write your prompt:
<img width="500" alt="Screenshot 2024-08-09 at 3 56 45 PM" src="https://github.com/user-attachments/assets/72fc65fa-9d64-497e-a32d-f81542ac484d">

Finally to use specific tasks feature click on the "Specific Tasks" button. This will take you to the following window:
<img width="500" alt="Screenshot 2024-08-09 at 3 53 27 PM" src="https://github.com/user-attachments/assets/9da6c5da-6454-4e75-be76-bcf18bbbcaa2">

## Key Features:
- Model Selection: Users can choose from a list of available GPT-3.5-turbo models.
- Prompt Input: Users can input custom prompts for the selected model.
- Operation Selection: Users can specify the desired operation for the prompt.
- Dynamic Response Rendering: The application calls the OpenAI API with the provided inputs and displays the generated response on a results page.
- Multiple Endpoints: The app includes several routes to handle different types of requests and render the corresponding templates.

## The app includes the following endpoints:
- /results: Handles GET requests to process user input and display the generated response.
- /results_new: Similar to /results, but includes the additional functionality to specify an operation for the prompt.
- /: The main index page.
- /prompt_design: A page where users can design their prompts.
- /specific_tasks: A page focused on specific tasks like sentiment analysis or translation.

**Note:** Please generate OpenAI API key first from the OpenAI website and replace `YOUR_API_KEY` with your API key in `app.py` code file to generate the response.

## How to execute the code:
To install OpenAI and Flask libraries you can use the following terminal commands:
- `pip3 install openai`
- `pip3 install flask`

To execute the application run the following command:
- `python3 app.py`

To run the application, ensure you have Flask and OpenAI libraries installed, set up your OpenAI API key, and execute the script. The app will be accessible on your browser, allowing you to experiment with different prompts and operations using GPT-3.5-turbo models.
