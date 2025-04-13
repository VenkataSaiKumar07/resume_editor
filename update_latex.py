import re

latex_input_file_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\latex_form.tex"
latex_output_file_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\edited_latex_form.tex"
experience_template_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\experience_template.tex"
education_template_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\education_template.tex"
project_template_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\project_template.tex"
skills_template_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\skills_template.tex"

def get_user_details():
    user_details = {
        "NAME": "Sai Jetti",
        "MAILID": "venkatj2@umbc.edu",
        "PHONE": "2404575305",
        "LINKEDIN": "https://www.linkedin.com/in/sai-jetti",
        "SUMMARY": "Experienced in developing scalable backend systems, microservices, and cloud-based solutions using Java, Python, Golang, and AWS. Skilled in building RESTful APIs, optimizing system performance, automating deployments with Kubernetes and CI/CD, and integrating LLM-powered applications for intelligent data processing.",
        "EXPERIENCE": [
            {
                "ROLE": "Software &Engineer",
                "COMPANY": "TechCorp",
                "DURATION": "Jan 2020 - Present",
                "SKILLS": "Java, Spring Boot, AWS, SQL, RESTful API",
                "DESCRIPTION":  [
                    "Developed and optimized RESTful APIs using Java (Spring Boot) to enhance data retrieval efficiency, reducing response time by 35%.",
                    "Integrated AWS services such as S3, Lambda, and RDS to build scalable backend solutions and improve cloud adoption.",
                    "Designed and implemented database schemas in PostgreSQL, improving data integrity and query performance by 40%.",
                    "Implemented authentication and authorization using Spring Security and JWT, strengthening system security.",
                    "Built event-driven microservices with Apache Kafka by implementing Spring Boot Kafka producers & consumers.",
                    "Assisted in containerizing microservices using Docker and deploying them to AWS ECS, improving scalability."
                ]
            },
            {
                "ROLE": "Intern",
                "COMPANY": "Data Inc.",
                "DURATION": "Jun 2019 - Dec 2019",
                "SKILLS": "Python, Flask, MongoDB, Docker",
                "DESCRIPTION":  [
                    "Developed a Flask-based web application for data visualization, improving user engagement by 50%.",
                    "Implemented RESTful APIs for data retrieval and manipulation, enhancing system performance.",
                    "Containerized the application using Docker for consistent deployment across environments."
                ]
            }
        ],
        "EDUCATION": [
            {
                "DEGREE": "Master of Science in Computer Science",
                "COLLEGE": "University of Maryland, Baltimore County",
                "DURATION": "Aug 2018 - May 2020",
                "GPA": "3.8/4.0",
                "COURSES": "Java, Python, AWS, SQL, Machine Learning",
            },
            {
                "DEGREE": "BTech in ECE",
                "COLLEGE": "RVR&JCCE, India",
                "DURATION": "Aug 2017 - Jul 2021",
                "GPA": "9.02/10",
                "COURSES": "Data Structures, Algorithms, Operating Systems, Computer Networks",
            }
        ],
        "PROJECTS": [
            {
                "TITLE": "LLM-Powered Chatbot",
                "DURATION": "Jan 2023 - Apr 2023",
                "INTRODUCTION": "Developed a chatbot using LLMs for intelligent data processing and user interaction using python, flask, and AWS.",
                "DESCRIPTION": [
                    "Developed a chatbot using LLMs for intelligent data processing and user interaction.",
                    "Integrated with RESTful APIs for real-time data retrieval and processing.",
                    "Implemented CI/CD pipelines for automated deployment using Jenkins and Docker."
                ]
            },
            {
                "TITLE": "E-commerce Web Application",
                "DURATION": "May 2022 - Aug 2022",
                "INTRODUCTION": "Designed and developed a full-stack e-commerce application using Java, Spring Boot, and React.",
                "DESCRIPTION": [
                    "Designed and developed a full-stack e-commerce application using Java, Spring Boot, and React.",
                    "Implemented RESTful APIs for product management, user authentication, and payment processing.",
                    "Deployed the application on AWS using EC2 and RDS."
                ]
            }
        ],
        "SKILLS": {
            "Languages": ["Java", "Python", "Golang", "JavaScript", "SQL"],
            "Frameworks and Packages": ["Springboot", "Angular", "Mockito", "MySQL", "Neo4j", "PostgreSQL", "Scikit Learn", "Pytorch"],
            "Cloud and Databases": ["AWS (SageMaker, Lambda, EC2)", "Snowflake", "MySQL", "MongoDB"],
            "Tools": ["Gerrit", "Git", "Docker", "Kubernetes", "AWS", "Linux", "REST APIs", "Postman", "Jenkins"],
            "Big Data and ETL Tools": ["Apache Spark", "Hadoop", "Kafka", "Airflow", "Apache Nifi", "Pentaho"]
        },
    }

    return user_details

def escape_latex_special_chars(text):
    latex_special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
    }
    if('&' in text):
        print(f"Escaping LaTeX special characters")
    return re.sub(
        r'([&%$#_{}])',
        lambda match: latex_special_chars[match.group()],
        text
    )

def getFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def writeFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def fillValues(user_details, file_path, isLatexReady=False):

    lines = getFile(file_path)

    for placeholder, value in user_details.items():
        if not isLatexReady:
            value = escape_latex_special_chars(value)
        lines = lines.replace(f"{{{{{placeholder}}}}}", value)

    return lines

def update_latex(user_details):
    print("Updating LaTeX Resume")

    lines = fillValues(user_details, latex_input_file_path, True)

    writeFile(latex_output_file_path, lines)

    print("LaTeX Resume Updated")
    
def format_user_details_experience(user_details):

    for i in range(len(user_details["EXPERIENCE"])):
        description ="\n".join([f"\item {desc}" for desc in user_details["EXPERIENCE"][i]["DESCRIPTION"]])
        user_details["EXPERIENCE"][i]["DESCRIPTION"] = description
    
        user_details["EXPERIENCE"][i] = fillValues(user_details["EXPERIENCE"][i], experience_template_path, False)

    user_details["EXPERIENCE"] = "\n".join(user_details["EXPERIENCE"])
    return user_details

def format_user_details_education(user_details):

    for i in range(len(user_details["EDUCATION"])):
        user_details["EDUCATION"][i] = fillValues(user_details["EDUCATION"][i], education_template_path, False)

    user_details["EDUCATION"] = "\n".join(user_details["EDUCATION"])
    return user_details

def format_user_details_projects(user_details):

    for i in range(len(user_details["PROJECTS"])):
        description ="\n".join([f"\item {desc}" for desc in user_details["PROJECTS"][i]["DESCRIPTION"]])
        user_details["PROJECTS"][i]["DESCRIPTION"] = description

        user_details["PROJECTS"][i] = fillValues(user_details["PROJECTS"][i], project_template_path, False)

    user_details["PROJECTS"] = "\n".join(user_details["PROJECTS"])
    return user_details

def format_user_details_skills(user_details):
    all_skills = []
    for cateogry, skills in user_details["SKILLS"].items():
        all_skills.append(fillValues({"CATEGORY": cateogry, "SKILLS": ", ".join(skills)}, skills_template_path, False))
    user_details["SKILLS"] = "\n".join(all_skills)

    return user_details

if __name__ == "__main__":
    
    print("Getting User Details")
    user_details = get_user_details()

    user_details = format_user_details_experience(user_details)

    user_details = format_user_details_education(user_details)

    user_details = format_user_details_projects(user_details)

    user_details = format_user_details_skills(user_details)

    print(user_details.keys())
    update_latex(user_details)

