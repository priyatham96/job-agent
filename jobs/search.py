import requests

def search_jobs():

    jobs = []

    keywords = [
        "DevOps Engineer",
        "Cloud Engineer",
        "Platform Engineer",
        "SRE"
    ]

    for keyword in keywords:

        jobs.append({
            "title": keyword,
            "company": "Sample Company",
            "location": "Hyderabad",
            "description": "AWS Kubernetes Terraform CI/CD",
            "url": "https://example.com"
        })

    return jobs
