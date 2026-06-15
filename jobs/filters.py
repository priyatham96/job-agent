def filter_jobs(jobs):

    filtered = []

    for job in jobs:

        if "Hyderabad" in job["location"]:
            filtered.append(job)

    return filtered
