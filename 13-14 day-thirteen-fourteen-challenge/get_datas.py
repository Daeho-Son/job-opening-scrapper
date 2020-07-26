import requests
from bs4 import BeautifulSoup


"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


def get_so(job):
    so_url = f"https://stackoverflow.com/jobs?r=true&q={job}"
    so_soup = BeautifulSoup(requests.get(so_url).text, "html.parser")
    so_jobs_count = so_soup.select("div.seo-header span")[0].text.strip().split(" ")[0]

    if so_jobs_count == "0":
        print(f"stackoverflow에는 {job}에 관한 채용 정보가 없어")
        return []
    max_page = so_soup.select("div.s-pagination a")[-1]["title"].split(" ")[1]
    so_datas = []
    for pg in range(0, int(max_page)):
        so_url = f"https://stackoverflow.com/jobs?r=true&q={job}&pg={pg+1}"
        so_soup = BeautifulSoup(requests.get(so_url).text, "html.parser")
        so_select = so_soup.select("div.listResults div.js-result")
        for data in so_select:
            title = data.select("a.s-link")[0]["title"]
            company = data.select("h3.fc-black-700 span")[0].text.strip().splitlines()
            company = [a.strip() for a in company]
            url = (
                "https://stackoverflow.com/"
                + data.select("h2.fc-black-800 a")[0]["href"]
            )
            so_datas.append({"title": title, "company": " ".join(company), "url": url})
    return so_datas


def get_wwr(job):
    wwr_url = f"https://weworkremotely.com/remote-jobs/search?term={job}"
    wwr_soup = BeautifulSoup(requests.get(wwr_url).text, "html.parser")
    if wwr_soup.select("div.no_results"):
        print(f"weworkremotely에는 {job}에 관한 채용 정보가 없어")
        return []
    wwr_select = wwr_soup.select("div.jobs-container section.jobs > article li")
    wwr_datas = []
    for data in wwr_select:
        try:
            if data["class"][0] == "view-all":  # <li class="view-all">
                pass
            else:  # <li class="feature">
                data = data.find_all("a")[1]
                title = data.find("span", {"class": "title"}).text
                company = data.find("span", {"class": "company"}).text
                url = "https://weworkremotely.com/" + data["href"]
                wwr_datas.append({"title": title, "company": company, "url": url})
        except IndexError:  # <li class>
            title = data.find("span", {"class": "title"})
            company = data.find("span", {"class": "company"})
            url = "https://weworkremotely.com/" + data.find("a")["href"]
            wwr_datas.append({"title": title.text, "company": company.text, "url": url})
    return wwr_datas


def get_remote(job):
    remote_url = f"https://remoteok.io/remote-dev+{job}-jobs"
    remote_soup = BeautifulSoup(requests.get(remote_url).text, "html.parser")
    if remote_soup.find("title").text == "Not found":
        print(f"remoteok에는 {job}에 관한 채용 정보가 없어")
        return []
    remote_select = remote_soup.select(
        "div.page > div.container > table#jobsboard tr.job"
    )
    remote_datas = []
    for count, data in enumerate(remote_select):
        title = (
            data.select("td.company_and_position_mobile a.preventLink")[0]
            .find("h2")
            .text
        )
        company = (
            data.select("td.company_and_position_mobile a.preventLink")[1]
            .find("h3")
            .text
        )
        url = "https://remoteok.io/" + data["data-url"]
        remote_datas.append({"title": title, "company": company, "url": url})
    return remote_datas


def get_job_datas(job):
    so_data = get_so(job)
    wwr_data = get_wwr(job)
    remote_data = get_remote(job)
    job_datas = so_data + wwr_data + remote_data
    return job_datas
