from flask import Flask, render_template, request, redirect, url_for, flash
import os
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            flash('No resume file part')
            return redirect(request.url)

        resume_file = request.files['resume']
        job_desc_text = request.form.get('job_desc_text')

        if resume_file.filename == '' or job_desc_text.strip() == '':
            flash('No selected file or job description text')
            return redirect(request.url)

        if resume_file and allowed_file(resume_file.filename):
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume.docx')
            resume_file.save(resume_path)

            # Process the documents and calculate the similarity score
            resume = docx2txt.process(resume_path)
            job_desc = job_desc_text.strip()

            text = [resume, job_desc]

            cv = CountVectorizer()
            count_matrix = cv.fit_transform(text)

            match = cosine_similarity(count_matrix)[0][1]
            match = match * 100
            match = round(match, 2)

            result = f"The resume matches about {match}% of the job description"
            return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
