google_hackathon

Overview
This project is a Flask-based Intelligent Process Automation system that extracts data from documents and displays it on a UI. The system utilizes SQLite as the database.

Setup Instructions
Prerequisites
Ensure you have the following installed:
Python (3.8 or later)

Clone the Repository
```sh
 git clone <repository_url>
 cd <project_directory>
```

Create a Virtual Environment 
```sh
python -m venv venv 
```

Activate the virtual environment:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
Running the Application

Set Up the Database (SQLite)
Ensure you have an SQLite database file (`automation.db`). If not, run:
```sh
python setup_database.py  
```

Start the Flask Application
```sh
python render_template.py
```

Open in Browser
Once the server is running, open your browser and go to:
```
http://127.0.0.1:5000/
```

Troubleshooting

Flask Import Errors
If you see `Import "flask" could not be resolved`, ensure Flask is installed in the correct environment:
```sh
pip install flask
```

Template Not Found Error
Ensure `index.html` is inside a `templates/` folder:
```
project_directory/
│── render_template.py
│── templates/
│   ├── index.html
```

Database Connection Issues
Check if `automation.db` exists in the project directory:
```sh
ls | grep automation.db  # Mac/Linux
```
```sh
dir | findstr automation.db  # Windows
```
If missing, create it using `setup_database.py` (if applicable).

Additional Information
- This project uses **Tesseract OCR** for text extraction. Ensure it is installed and configured properly.
- If using **Windows**, verify `Tesseract-OCR` is installed and its path is set:
  ```sh
  setx TESSDATA_PREFIX "C:\Program Files\Tesseract-OCR"
  ```
  
Contributing
Feel free to fork this repository, raise issues, or submit pull requests.

License
This project is open-source under the MIT License.

