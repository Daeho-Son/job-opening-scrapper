import os
import csv


def save_brand_recruits(brand_name, brand_recruits):
    print(f"{brand_name}.csv 변환")
    try:
        if not (os.path.isdir("csv_files")):
            os.makedirs(os.path.join("csv_files"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!")
            raise
    f = open(f"csv_files/{brand_name}.csv", "w", encoding="utf-8")
    wr = csv.writer(f)
    wr.writerow(["place", "title", "time", "pay", "date"])
    for recruits in brand_recruits:
        wr.writerow(
            [
                recruits.get("place"),
                recruits.get("title"),
                recruits.get("time"),
                recruits.get("pay"),
                recruits.get("date"),
            ]
        )
        
    f.close
