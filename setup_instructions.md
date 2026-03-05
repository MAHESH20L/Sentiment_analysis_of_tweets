**INSTALLATION AND PROJECT SETUP**

<br>

**1 Create Project Folder**

Open File Explorer on your PC.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Create a new folder called `project_folder`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Inside the folder create two subfolders called `backend` and `frontend`.

<br>

**2 Project Structure**

project_folder/<br>
&nbsp;&nbsp;&nbsp;&nbsp;backend/<br>
&nbsp;&nbsp;&nbsp;&nbsp;frontend/

<br>

**3 Download Backend Code**

Go to the repository folder `src/backend`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Download all backend files.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Copy the downloaded files into the `backend` folder.

<br>

**4 Backend Folder Structure**

project_folder/<br>
&nbsp;&nbsp;&nbsp;&nbsp;backend/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirements.txt<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;model files<br>
&nbsp;&nbsp;&nbsp;&nbsp;frontend/

<br>

**5 Important Requirements File**

Download the `requirements.txt` file from the repository **sentiment_analysis_on_tweets**.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Save the `requirements.txt` file inside the `backend` folder.

<br>

**6 Download Frontend Code**

Go to the repository folder `src/frontend`.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Download all frontend files.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Place them inside the `frontend` folder.

<br>

**7 Frontend Folder Structure**

project_folder/<br>
&nbsp;&nbsp;&nbsp;&nbsp;backend/<br>
&nbsp;&nbsp;&nbsp;&nbsp;frontend/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style.css<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script.js

<br>

**8 Open Project in VS Code**

Open Visual Studio Code.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Click **File → Open Folder**.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Select your `project_folder`.

<br>

**9 Install Required Extensions**

Open the **Extensions tab** in VS Code.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Make sure the following extensions are installed.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HTML<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CSS<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JavaScript<br>
&nbsp;&nbsp;&nbsp;&nbsp;If they are not installed, install them from the Extensions marketplace.

<br>

**10 Open Terminal in VS Code**

Go to the menu.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Click **Terminal → New Terminal**.

<br>

**11 Navigate to Project Folder**

In the terminal type the following command.<br>

```
cd project_folder
```

<br>

**12 Move to Backend Folder**

Type the following command.

```
cd backend
```

<br>

**13 Install Backend Dependencies**

Make sure `requirements.txt` is inside the backend folder.<br>
Run the following command.

```
pip install -r requirements.txt
```

Install additional dependencies.

```
pip install uvicorn
pip install python-multipart
```

<br>

**14 Run Backend Server**

Run the backend server using the command.

```
python -m uvicorn main:app --reload 
```

The backend server will start at:<br>
&nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:8000

<br>

**15 Run Frontend**

Go to the `frontend` folder.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Open `index.html` file.<br>
&nbsp;&nbsp;&nbsp;&nbsp;Run it using a browser or **Live Server in VS Code**.

<br>

**Model Used**

The backend loads the trained model from Hugging Face.<br>
&nbsp;&nbsp;&nbsp;&nbsp;https://huggingface.co/PattimaniM/updated_sentiment<br>
&nbsp;&nbsp;&nbsp;&nbsp;This model performs sentiment analysis on tweets using transformer-based machine learning techniques.
