from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def score_job(resume_text, job_description):

    prompt = f"""
    Compare resume and job.

    Resume:
    {resume_text}

    Job:
    {job_description}

    Return only a score between 0 and 100.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return float(response.choices[0].message.content)
