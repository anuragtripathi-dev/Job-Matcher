import json

roles = [
 ("Python Backend Intern", "Python, FastAPI, SQL, REST APIs", "Build and maintain REST APIs, write SQL queries and work with databases."),
 ("Frontend Developer Intern", "React, JavaScript, CSS", "Build responsive user interfaces and connect them to backend APIs."),
 ("Data Analyst Intern", "SQL, Excel, Power BI, Python", "Analyze data, build dashboards and share insights with the team."),
 ("Machine Learning Intern", "Python, scikit-learn, pandas, NumPy", "Train and evaluate machine learning models and clean datasets."),
 ("LLM Engineer Intern", "LLMs, prompting, RAG, embeddings, Python", "Build LLM-powered agents with tool calling and retrieval."),
 ("DevOps Intern", "Docker, Linux, CI/CD, AWS", "Automate deployments and monitor cloud infrastructure."),
 ("Android Developer Intern", "Kotlin, Android, REST APIs", "Build Android app features and fix bugs."),
 ("QA Automation Intern", "Selenium, Python, testing", "Write automated tests and report bugs."),
 ("Full Stack Developer Intern", "React, Node.js, MongoDB", "Build features end to end across frontend and backend."),
 ("Cybersecurity Intern", "networking, Linux, Wireshark", "Help with vulnerability scans and security monitoring."),
]
companies = ["TechNova", "DataLeaf", "CloudNest", "CodeBridge", "AppForge"]
cities = ["Bhopal", "Gurugram", "Bengaluru", "Remote", "Indore"]

jobs = []
i = 1
for title, skills, desc in roles:
    for c in companies:
        jobs.append({"id": i, "title": title, "company": c,
                     "location": cities[i % 5], "skills": skills,
                     "description": desc})
        i += 1

json.dump(jobs, open("jobs.json", "w"), indent=2)
print(len(jobs), "jobs saved")