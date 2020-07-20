import os
import csv


try:
    # 파일경로가 존재하지 않을 경우 경로생성
    if not (os.path.isdir("csv_files")):
        os.makedirs(os.path.join("csv_files"))
except OSError as e:  # 경로가 이미 존재할 경우 에러
    if e.errno != e.errno.EEXIST:
        print("Failed to create directory!")
        raise
    pass
f = open(f"csv_files/practice.csv", "w", encoding="utf-8")
wr = csv.writer(f)
wr.writerow(["place", "title", "time", "pay", "date"])
f.close