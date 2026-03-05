
CREATE PROJECT FOLDER


1. Open File Explorer on your PC.

2. Create a new folder called project_folder.

The project structure should look like this:

project_folder/
|
|---- backend/
|
|---- frontend/



DOWNLOAD BACKEND CODE


1. Go to the repository folder: src/backend

2. Download all backend files.

3. Copy the downloaded backend files into the backend folder.

Your folder should now look like:

project_folder/
|
|---- backend/
|       |
|       |---- main.py
|       |---- model files
|       |---- requirements.txt
|
|---- frontend/


IMPORTANT:

Download the requirements.txt file from the repository:
sentiment_analysis_on_tweets

Save this requirements.txt file inside the backend folder.


DOWNLOAD FRONTEND CODE


1. Go to the repository folder: src/frontend

2. Download all frontend files.

3. Copy them into the frontend folder.

The structure should now look like:

project_folder/
|
|---- backend/
|       |
|       |---- main.py
|       |---- requirements.txt
|
|---- frontend/
        |
        |---- index.html
        |---- style.css
        |---- script.js


OPEN PROJECT IN VISUAL STUDIO CODE


1. Open Visual Studio Code.

2. Click File → Open Folder.

3. Select your project_folder.



INSTALL REQUIRED EXTENSIONS IN VS CODE


Make sure the following extensions are installed:

Python
HTML
CSS
JavaScript

If they are not installed:

1. Click the Extensions icon in VS Code.
2. Search for the extensions.
3. Install them.



OPEN TERMINAL IN VS CODE


Open the terminal by selecting:

Terminal → New Terminal



NAVIGATE TO PROJECT FOLDER


In the terminal, type:

cd project_folder


Then move to backend folder:

cd backend



INSTALL BACKEND DEPENDENCIES


Make sure requirements.txt is inside the backend folder.

Run the following command:

pip install -r requirements.txt


Then install additional packages:

pip install uvicorn
pip install python-multipart



RUN THE BACKEND SERVER


Run the backend server using the command:

uvicorn main:app --reload


The backend server will start at:

http://127.0.0.1:8000



RUN THE FRONTEND


1. Go to the frontend folder.

2. Open the file:

index.html

3. Run it using a browser or using Live Server in VS Code.



MODEL USED


The backend loads the trained model from Hugging Face:

https://huggingface.co/PattimaniM/updated_sentiment

This model performs sentiment analysis on tweets using
machine learning techniques and a transformer-based architecture.
