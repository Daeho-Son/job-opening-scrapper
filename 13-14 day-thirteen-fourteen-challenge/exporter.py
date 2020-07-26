import csv


def export_to_file(job_datas):
    f = open("job_datas.csv", "w")
    wf = csv.writer(f)
    wf.writerow(["title", "company", "url"])
    for data in job_datas:
        wf.writerow(data.values())
    print("=" * 50)
    print("=============     CSV 변환 완료      =============")
    print("=" * 50)
    return
