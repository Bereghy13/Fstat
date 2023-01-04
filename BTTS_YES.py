import csv
import time

def BTTS_YES(csv_reader):
    line_count = 0

    #BTTS_90_YES = False
    BTTS_90_event_count = 0
    BTTS_90_YES_list = []

    BTTS_80_YES = False
    BTTS_80_event_count = 0
    BTTS_80_YES_list = []

    BTTS_70_YES = False
    BTTS_70_event_count = 0
    BTTS_70_YES_list = []

    BTTS_60_YES = False
    BTTS_60_event_count = 0
    BTTS_60_YES_list = []

    BTTS_50_YES = False
    BTTS_50_event_count = 0
    BTTS_50_YES_list = []

    tmp_List = []

    strNM = "Nem található esemény ebben a forgatókönyvben!\n\n"

    def BTTS_check_res(row, line_count, BTTS_Avg_Low, BTTS_Avg_High):
        BTTS_flag = False
        BTTS_list = []

        if row["Match Status"] == "complete" and int(row["Result - Home Team Goals"]) >= 1 and int(
                row["Result - Away Team Goals"]) >= 1 \
                and int(row["BTTS Average"]) >= BTTS_Avg_Low and int(row["BTTS Average"]) < BTTS_Avg_High:
            BTTS_flag = True
            BTTS_list = (f'{line_count}. {row["date_GMT"]} - {row["Country"]}: {row["League"]} ==> {row["Home Team"]} - {row["Away Team"]} -'
                f' {row["Result - Home Team Goals"]}:{row["Result - Away Team Goals"]} - {row["Match Status"]} - '
                f'BTTS Predictions: {row["BTTS Average"]}\n\n')

        if BTTS_flag == True:
            return BTTS_list

    def BTTS_check_pred(row, line_count, BTTS_Avg_Low, BTTS_Avg_High):
        BTTS_flag = False
        BTTS_list = []

        if int(row["BTTS Average"]) >= BTTS_Avg_Low and int(row["BTTS Average"]) < BTTS_Avg_High :
            BTTS_flag = True
            BTTS_list = (f'{line_count}. {row["date_GMT"]} - {row["Country"]}: {row["League"]} ==> {row["Home Team"]} - {row["Away Team"]} -'
                f' {row["Result - Home Team Goals"]}:{row["Result - Away Team Goals"]} - {row["Match Status"]} - '
                f'BTTS Predictions: {row["BTTS Average"]}\n\n')

        if BTTS_flag == True:
            return BTTS_list

    def print_pred_res(scen_id, f, range, btts_flag, btts_list, btts_event_count):
        with open(f, 'a') as f:
            f.writelines("###############################################################\n")
            f.writelines(f"Scenario {scen_id} - BTTS_{range}_YES - Megjósolt és bekövetkezett esemény!\n")
            f.writelines("###############################################################\n")
            f.writelines(f"BTTS_{range}_YES - Összes jósolt esemény száma: {btts_event_count}\n")
            f.writelines("###############################################################\n")
            if btts_flag == False:
                f.writelines(strNM)
            else:
                f.writelines(btts_list)

    print("A BTTS események kiértékelése megkezdődött...")
    for row in csv_reader:
        # if BTTS_check_pred(row, line_count, 80, 101) is not None:
        #     tmp_List = BTTS_check_pred(row, line_count, 80, 101)
        #     BTTS_90_YES = True
        #     BTTS_90_YES_list.append(tmp_List)
        #print("Scenario01 - BTTS_90_YES esemény értékelése...")
        if BTTS_check_res(row, line_count, 90, 101) is not None:
            tmp_List = BTTS_check_res(row, line_count, 90, 101)
            BTTS_90_YES = True
            BTTS_90_event_count += 1
            BTTS_90_YES_list.append(tmp_List)

        #print("Scenario02 - BTTS_80_YES esemény értékelése...")
        if BTTS_check_res(row, line_count, 80, 90) is not None:
            tmp_List = BTTS_check_res(row, line_count, 80, 90)
            BTTS_80_YES = True
            BTTS_80_event_count += 1
            BTTS_80_YES_list.append(tmp_List)

        # print("Scenario03 - BTTS_70_YES esemény értékelése...")
        if BTTS_check_res(row, line_count, 70, 80) is not None:
            tmp_List = BTTS_check_res(row, line_count, 70, 80)
            BTTS_70_YES = True
            BTTS_70_event_count += 1
            BTTS_70_YES_list.append(tmp_List)

        # print("Scenario04 - BTTS_60_YES esemény értékelése...")
        if BTTS_check_res(row, line_count, 60, 70) is not None:
            tmp_List = BTTS_check_res(row, line_count, 60, 70)
            BTTS_60_YES = True
            BTTS_60_event_count += 1
            BTTS_60_YES_list.append(tmp_List)

        # print("Scenario04 - BTTS_50_YES esemény értékelése...")
        if BTTS_check_res(row, line_count, 50, 60) is not None:
            tmp_List = BTTS_check_res(row, line_count, 50, 60)
            BTTS_50_YES = True
            BTTS_50_event_count += 1
            BTTS_50_YES_list.append(tmp_List)

        # print("Scenario04 - BTTS_30_NO esemény értékelése...")
        # print("Scenario05 - BTTS_20_NO esemény értékelése...")
        # print("Scenario06 - BTTS_10_NO esemény értékelése...")
        line_count += 1

    print_pred_res('01', 'BTTS_YES.txt', 90, BTTS_90_YES, BTTS_90_YES_list, BTTS_90_event_count)
    print_pred_res('02', 'BTTS_YES.txt', 80, BTTS_80_YES, BTTS_80_YES_list, BTTS_80_event_count)
    print_pred_res('03', 'BTTS_YES.txt', 70, BTTS_70_YES, BTTS_70_YES_list, BTTS_70_event_count)
    print_pred_res('04', 'BTTS_YES.txt', 60, BTTS_60_YES, BTTS_60_YES_list, BTTS_60_event_count)
    print_pred_res('05', 'BTTS_YES.txt', 50, BTTS_50_YES, BTTS_50_YES_list, BTTS_50_event_count)

    print("A BTTS események kiértékelélse befejeződött! Az eredmények file-ba kerültek!")

start = time.time()

print("Első file felolvasása...")

with open('sample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    BTTS_YES(csv_reader)

end = time.time()

print("A szkript futásai ideje : ", (end-start)*10**3, "ms")