import csv
import time
import operator
import os, datetime

def CSV_BTTS_SORT(csv_reader):
    BTTS_Avg_Low = 90
    BTTS_interval = 11
    line_count = 0
    btts_pred_num = 0
    btts_res_num = 0
    BTTS_LIST = []

    def BTTS_YES(btts_pred_num, line_count, btts_res_num):
        btts_pred_num += 1
        if int(row["Result - Home Team Goals"]) >= 1 and int(row["Result - Away Team Goals"]) >= 1:
            line_count += 1
            btts_res_num += 1
            BTTS_LIST.append(
                f'{line_count}. {row["date_GMT"]} - {row["Country"]}: {row["League"]} ==> {row["Home Team"]} - {row["Away Team"]} -'
                f' {row["Result - Home Team Goals"]}:{row["Result - Away Team Goals"]} - {row["Match Status"]} - '
                f'BTTS Predictions: {row["BTTS Average"]}\n\n')
        return btts_pred_num, line_count, btts_res_num

    sorted_csv = sorted(csv_reader, key=lambda row: int(row["BTTS Average"]), reverse=True)

    for row in sorted_csv:
        if row["Match Status"] == "complete":
            if BTTS_Avg_Low > int(row["BTTS Average"]):
                if btts_pred_num > 0:
                    print(f'BTTS eseményszám a {BTTS_Avg_Low} - {BTTS_Avg_Low + BTTS_interval} tartományban: {btts_pred_num} - Bekövetkezett BTTS eseményszám: {btts_res_num} - A bekövetkezés aránya: {(btts_res_num / btts_pred_num) * 100}')
                    #print(''.join(BTTS_LIST))
                    BTTS_interval = 10
                    BTTS_Avg_Low = BTTS_Avg_Low - BTTS_interval
                    btts_pred_num = 0
                    btts_res_num = 0
                    BTTS_LIST.clear()
                else:
                    print(f'Nincs meghatározott esemény a {BTTS_Avg_Low} és a {BTTS_Avg_Low + BTTS_interval} tartományban!')
                    BTTS_interval = 10
                    BTTS_Avg_Low = BTTS_Avg_Low - BTTS_interval

            match BTTS_Avg_Low:
                case 90:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 80:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 70:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 60:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 50:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 40:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 30:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 20:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 10:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)
                case 0:
                    btts_pred_num, line_count, btts_res_num = BTTS_YES(btts_pred_num, line_count, btts_res_num)



start = time.time()

filename = "sample01.csv"

print(f'Első file felolvasása: {filename}; File mérete: {os.path.getsize(filename)}; Utolsó módosítás dátuma: {datetime.datetime.fromtimestamp(os.path.getmtime(filename))}')

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    CSV_BTTS_SORT(csv_reader)


end = time.time()

print("A szkript futásai ideje : ", (end-start)*10**3, "ms")

