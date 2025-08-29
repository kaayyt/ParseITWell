# ParseITWell Resume Parser App (Gen AI + Flask)

### Objective

Creating a resume parser app using Flask is a great way to help job seekers test the ATS (Applicant Tracking System) friendliness of their resumes. The app allows users to upload their resumes in PDF format, which are then parsed to extract various pieces of information such as full name, email ID, GitHub portfolio, LinkedIn ID, employment details, technical skills, and soft skills. The extracted information is then presented in JSON format, providing users with valuable insights into the effectiveness of their resumes.

To build such an app, you can leverage various tools and libraries, including Python, Flask, Pyresparser, pdfminer.six, docx2txt, and NLP (natural language processing) libraries such as nltk and spacy. These tools enable the extraction of essential information from resumes in PDF and DOCx formats, making the process automated and efficient.

The app's functionality aligns with the growing need for streamlined recruitment processes and the increasing reliance on technology to evaluate and process job applications. By providing users with a detailed analysis of their resumes, the app empowers job seekers to optimize their resumes for better visibility and compatibility with ATS.


#### Overview: 
This App is created for job seekers to test whether their resumes are ATS friendly or not, if our App is able to parse your details and show it, then assume that everything is good.

#### Features: 
Ability to extract specific information from resumes, the use of JSON format for presenting the extracted data, and the integration of various libraries and tools for parsing resumes.

<img width="1882" height="845" alt="Screenshot 2025-08-29 144407" src="https://github.com/user-attachments/assets/846148de-ebef-40a4-8f16-6ebf8b01ac75" />


#### Installation: 
Run the pip install requirements.txt to install and set up the app, including any dependencies and prerequisites.

#### Usage: 
Just upload your resume in pdf format, and see for yourself :)


##### Running the program

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install all the required libraries (just run pip install -r /path/to/requirements.txt)
4. Provide your Groq API key in the .yaml file
5. Run the following command to start the chatbot -

    ```
    python app.py
    ```

    ```
    Go to: https://localhost:8000
    ```
    
The development of our Flask-based resume parser app marks a strategic leap forward in harnessing cutting-edge technology to empower job seekers in refining their resumes for today's competitive job market. This innovative solution directly addresses the growing need for streamlined, tech-enabled approaches to job applications, creating mutual value for both candidates and hiring professionals alike.
