Overview
--
This project is a web application built with Flask that allows users to upload their resume and input a job description to see how well their resume matches the job description. The application uses the '**doc2txt'** library to extract text from DOCX files and the '**sklearn'** library to calculate the similarity between the resume and the job description using cosine similarity.

Installation Guide
--
**Step 1: Prerequisites**
* Before setting up the application, ensure you have the following installed:
  * Python (version 3.6 or later)
  * Pip (Python package installer)

**Step 2: Clown or Download the Project**
1. Clone the repository
   * ```git clone https://github.com/youngdiggsa006/Resume-Scanner.git```
2. Download the project
   * ```cd path/to/extracted/folder```

**Step 3: Create a Virtual Environment**
* ```python -m venv venv```
* Activate the virtual environment
  - On Windows ```venv\Scripts\activate```
  - On macOS/Linux ```source venv/bin/activate```

**Step 4: Install Dependencies**
* Install the required Python packages using 'pip': ```pip install -r requirements.txt```
* Run ```pip install Flask docx2txt scikit-learn```

**Step 5: Set up the Uploads Directory**
* ```mkdir uploads```
