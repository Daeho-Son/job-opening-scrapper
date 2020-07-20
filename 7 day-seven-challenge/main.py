import os
from get_datas import get_alba_superbrands
from save_csv import save_brand_recruits


os.system("clear")


alba_superbrands = get_alba_superbrands()
print("=" * 4 + "모든 브랜드의 일반 채용정보 가져오기 완료." + "=" * 4)
for item in alba_superbrands:
    brand_name = item.get("brand_name")
    brand_recruits = item.get("brand_recruits")
    save_brand_recruits(brand_name, brand_recruits)
print("모든 작업이 성공적으로 완료되었습니다.")
