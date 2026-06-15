from ai.resume_parser import load_resume
from ai.scorer import score_job

from jobs.search import search_jobs
from jobs.filters import filter_jobs

from notifications.email_sender import send_email

def run():

    resume = load_resume("data/resume.pdf")

    jobs = search_jobs()

    jobs = filter_jobs(jobs)

    report = []

    for job in jobs:

        score = score_job(
            resume,
            job["description"]
        )

        if score >= 70:

            report.append(
                f"""
Title: {job['title']}
Company: {job['company']}
Location: {job['location']}
Score: {score}
Apply: {job['url']}
"""
            )

    send_email(
        "\n\n".join(report)
    )

if __name__ == "__main__":
    run()
