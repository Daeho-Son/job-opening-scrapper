import requests
from bs4 import BeautifulSoup
import os


os.system("clear")


"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


def get_so(job):
    so_url = f"https://stackoverflow.com/jobs?r=true&q={job}"
    max_page = (
        so_soup.select(
            "div.previewable-results > div.py32 > div.fd-column div.s-pagination"
        )[0]
        .find_all("a")[-1]["title"]
        .split(" ")[1]
    )
    print(f"max_page: {max_page}")

    jobs_count = (
        so_soup.select(
            "div.js-search-container > form.search-form > div.ai-center > div.js-search-title"
        )[0]
        .text.strip()
        .split(" ")[0]
    )
    return


def get_so_datas():
    so_soup = BeautifulSoup(requests.get(so_url).text, "html.parser")
    so_select = so_soup.select(
        "div.previewable-results > div.listResults > div.js-result"
    )
    so_datas = []
    for data in so_select:
        title = data.find("a", {"class": "s-link"})["title"]
        url = (
            "https://stackoverflow.com/"
            + data.find("a", {"class": "s-link"})["href"]
        )
        company = data.find("h3", {"class": "fc-black-700"}).find("span").text
        so_datas.append(
            {"title": title, "url": url, "company": company.splitlines()[0]}
        )
    return so_datas


# def get_wwr(job):
# wwr_url = f"https://weworkremotely.com/remote-jobs/search?term={job}"
#     return


# def get_remote(job):
# remote_url = f"https://remoteok.io/remote-dev+{job}-jobs"
#     return


# def get_job_datas(job):
#     so_data = get_so(job)
#     wwr_data = get_wwr(job)
#     remote_data = get_remote(job)
#     job_datas = ""
#     return job_datas


