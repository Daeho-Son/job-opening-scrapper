import csv


def export_to_file(job_datas, term):
    f = open(f"{term}.csv", "w")
    wf = csv.writer(f)
    wf.writerow(["title", "company", "url"])
    for data in job_datas:
        wf.writerow(data.values())
    return
