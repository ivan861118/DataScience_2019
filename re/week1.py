"""
131072
140319




"""


# =============

import csv

claim = []

with open("claim.csv", 'r') as csvFile:
    rows = csv.reader(csvFile)

    row_num = 0
    for i in rows:
        claim.append(i)

# for i in claim:
#     print(i[4])


# =============  # all illness count

ill = {}

for i in claim:
    if i[4] not in ill:
        ill[str(i[4])] = 1

    else:
        ill[str(i[4])] += 1

# print (ill)

# =============  # build data dict

req = {}

# column
req["CASE_NO"] = []
req["INSURED_SEX"] = []
req["AGE_RANK"] = []
req["TENURE"] = []
req["ILLNESS_CD"] = []
req["ILLNESS_CODE_DESC"] = []
req["HOSP_CD"] = []
req["HOSP_NAME"] = []
req["REIMB_AMT_K"] = []
req["SETTLE_DT"] = []
req["COUNTNO"] = []
req["REIMB_AMT_5Y_K"] = []
req["RECENCY_YEAR"] = []
req["COUNTCOVNO"] = []
req["SUM_AFYP_K"] = []
req["EFFECTDATE"] = []
req["TYPE_CODE"] = []
req["AFYP_K"] = []

# import data
for i in claim[1:-1]:
    req["CASE_NO"].append(i[0])
    req["INSURED_SEX"].append(i[1])
    req["AGE_RANK"].append(i[2])
    req["TENURE"].append(i[3])
    req["ILLNESS_CD"].append(i[4])
    req["ILLNESS_CODE_DESC"].append(i[5])
    req["HOSP_CD"].append(i[6])
    req["HOSP_NAME"].append(i[7])
    req["REIMB_AMT_K"].append(i[8])
    req["SETTLE_DT"].append(i[9])
    req["COUNTNO"].append(i[10])
    req["REIMB_AMT_5Y_K"].append(i[11])
    req["RECENCY_YEAR"].append(i[12])
    req["COUNTCOVNO"].append(i[13])
    req["SUM_AFYP_K"].append(i[14])
    req["EFFECTDATE"].append(i[15])
    req["TYPE_CODE"].append(i[16])
    req["AFYP_K"].append(i[17])

# print(req["CASE_NO"])


# ============= list-version of all data

req_list = []
for i in range(18):
    req_list.append([])

print(req_list)

for i in claim:
    k = 0
    for col in i:
        req_list[k].append(col)
        k += 1

print(req_list)
