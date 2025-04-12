latex_input_file_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\latex_form.tex"
latex_output_file_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\edited_latex_form.tex"
experience_template_path = r"C:\Users\Venkat\Study_Folder\PERSONAL_PROJECTS\resume_editor\resume_editor\experience_template.tex"

def get_user_details():
    user_details = {
        "NAME": "Sai Jetti",
        "MAILID": "venkatj2@umbc.edu",
        "PHONE": "2404575305",
        "LINKEDIN": "https://www.linkedin.com/in/sai-jetti",
        "SUMMARY": "Experienced in developing scalable backend systems, microservices, and cloud-based solutions using Java, Python, Golang, and AWS. Skilled in building RESTful APIs, optimizing system performance, automating deployments with Kubernetes and CI/CD, and integrating LLM-powered applications for intelligent data processing.",
        "EXPERIENCE": [
            {
                "ROLE": "Software Engineer",
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
    }

    return user_details

def getFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def writeFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def fillValues(user_details, file_path):

    lines = getFile(file_path)

    for placeholder, value in user_details.items():
        lines = lines.replace(f"{{{{{placeholder}}}}}", value)

    return lines

def update_latex(user_details):
    print("Updating LaTeX Resume")

    lines = fillValues(user_details, latex_input_file_path)

    writeFile(latex_output_file_path, lines)

    print("LaTeX Resume Updated")
    
def format_user_details_experience(user_details):

    for i in range(len(user_details["EXPERIENCE"])):
        description ="\n".join([f"\item {desc}" for desc in user_details["EXPERIENCE"][i]["DESCRIPTION"]])
        user_details["EXPERIENCE"][i]["DESCRIPTION"] = description
    
        user_details["EXPERIENCE"][i] = fillValues(user_details["EXPERIENCE"][i], experience_template_path)

    user_details["EXPERIENCE"] = "\n".join(user_details["EXPERIENCE"])
    return user_details

if __name__ == "__main__":
    
    print("Getting User Details")
    user_details = get_user_details()

    user_details = format_user_details_experience(user_details)

    print(user_details.keys())
    update_latex(user_details)

