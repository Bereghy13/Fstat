import csv
import time

def BTTS_YES(csv_reader):
    line_count = 0
    BTTS_90_YES = False
    BTTS_80_YES = False
    BTTS_70_YES = False
    BTTS_60_YES = False
    BTTS_50_YES = False
    BTTS_90_YES_list = []
    BTTS_80_YES_list = []
    BTTS_70_YES_list = []
    BTTS_60_YES_list = []
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

        if int(row["BTTS Average"]) >= BTTS_Avg_Low and int(row["BTTS Average"]) < BTTS_Avg_High and int(row["Over25 Average"]) >= BTTS_Avg_Low\
                and int(row["Over25 Average"]) < BTTS_Avg_High:
            BTTS_flag = True
            BTTS_list = (f'{line_count}. {row["date_GMT"]} - {row["Country"]}: {row["League"]} ==> {row["Home Team"]} - {row["Away Team"]} -'
                f' {row["Result - Home Team Goals"]}:{row["Result - Away Team Goals"]} - {row["Match Status"]} - '
                f'BTTS Predictions: {row["BTTS Average"]}\n\n')

        if BTTS_flag == True:
            return BTTS_list

    print("A BTTS események kiértékelése megkezdődött...")
    for row in csv_reader:
        if BTTS_check_pred(row, line_count, 80, 101) is not None:
        #BTTS_90_YES, BTTS_90_YES_list = BTTS_check(row, line_count, 90, 101)
            tmp_List = BTTS_check_pred(row, line_count, 80, 101)
            BTTS_90_YES = True
            BTTS_90_YES_list.append(tmp_List)
        #print("Scenario01 - BTTS_90_YES esemény értékelése...")
        # if BTTS_check_res(row, line_count, 90, 101) is not None:
        #     #BTTS_90_YES, BTTS_90_YES_list = BTTS_check(row, line_count, 90, 101)
        #     tmp_List = BTTS_check_res(row, line_count, 90, 101)
        #     BTTS_90_YES = True
        #     BTTS_90_YES_list.append(tmp_List)
        #
        # #print("Scenario02 - BTTS_80_YES esemény értékelése...")
        # if BTTS_check_res(row, line_count, 80, 90) is not None:
        #     #BTTS_80_YES, BTTS_80_YES_list = BTTS_check(row, line_count, 80, 90)
        #     tmp_List = BTTS_check_res(row, line_count, 80, 90)
        #     BTTS_80_YES = True
        #     BTTS_80_YES_list.append(tmp_List)
        #
        # # print("Scenario03 - BTTS_70_YES esemény értékelése...")
        # if BTTS_check_res(row, line_count, 70, 80) is not None:
        #     #BTTS_70_YES, BTTS_70_YES_list = BTTS_check(row, line_count, 70, 80)
        #     tmp_List = BTTS_check_res(row, line_count, 70, 80)
        #     BTTS_70_YES = True
        #     BTTS_70_YES_list.append(tmp_List)
        #
        # # print("Scenario04 - BTTS_60_YES esemény értékelése...")
        # if BTTS_check_res(row, line_count, 60, 70) is not None:
        #     #BTTS_60_YES, BTTS_60_YES_list = BTTS_check(row, line_count, 60, 70)
        #     tmp_List = BTTS_check_res(row, line_count, 60, 70)
        #     BTTS_60_YES = True
        #     BTTS_60_YES_list.append(tmp_List)
        #
        # # print("Scenario04 - BTTS_50_YES esemény értékelése...")
        # if BTTS_check_res(row, line_count, 50, 60) is not None:
        #     #BTTS_50_YES, BTTS_50_YES_list = BTTS_check(row, line_count, 50, 60)
        #     tmp_List = BTTS_check_res(row, line_count, 50, 60)
        #     BTTS_50_YES = True
        #     BTTS_50_YES_list.append(tmp_List)

        # print("Scenario04 - BTTS_30_NO esemény értékelése...")
        # print("Scenario05 - BTTS_20_NO esemény értékelése...")
        # print("Scenario06 - BTTS_10_NO esemény értékelése...")
        line_count += 1

    with open('szombat_mix.txt', 'a') as f:
        f.writelines("###############################################################\n")
        f.writelines("Scenario 01 - BTTS_90_YES - Megjósolt és bekövetkezett esemény!\n")
        f.writelines("###############################################################\n")
        if BTTS_90_YES == False:
            f.writelines(strNM)
        else:
            f.writelines(BTTS_90_YES_list)


    #with open('BTTS_YES.txt', 'a') as f:
        # f.writelines("###############################################################\n")
        # f.writelines("Scenario 01 - BTTS_90_YES - Megjósolt és bekövetkezett esemény!\n")
        # f.writelines("###############################################################\n")
        # if BTTS_90_YES == False:
        #     f.writelines(strNM)
        # else:
        #     f.writelines(BTTS_90_YES_list)
        #
        # f.writelines("###############################################################\n")
        # f.writelines("Scenario 02 - BTTS_80_YES - Megjósolt és bekövetkezett esemény!\n")
        # f.writelines("###############################################################\n")
        # if BTTS_80_YES == False:
        #     f.writelines(strNM)
        # else:
        #     f.writelines(BTTS_80_YES_list)
        #
        # f.writelines("###############################################################\n")
        # f.writelines("Scenario 03 - BTTS_70_YES - Megjósolt és bekövetkezett esemény!\n")
        # f.writelines("###############################################################\n")
        # if BTTS_70_YES == False:
        #     f.writelines(strNM)
        # else:
        #     f.writelines(BTTS_70_YES_list)
        #
        # f.writelines("###############################################################\n")
        # f.writelines("Scenario 04 - BTTS_60_YES - Megjósolt és bekövetkezett esemény!\n")
        # f.writelines("###############################################################\n")
        # if BTTS_60_YES == False:
        #     f.writelines(strNM)
        # else:
        #     f.writelines(BTTS_60_YES_list)
        #
        # f.writelines("###############################################################\n")
        # f.writelines("Scenario 05 - BTTS_50_YES - Megjósolt és bekövetkezett esemény!\n")
        # f.writelines("###############################################################\n")
        # if BTTS_50_YES == False:
        #     f.writelines(strNM)
        # else:
        #     f.writelines(BTTS_50_YES_list)

    print("A BTTS események kiértékelélse befejeződött! Az eredmények file-ba kerültek!")

start = time.time()

print("Első file felolvasása...")

with open('sample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    BTTS_YES(csv_reader)

end = time.time()

print("A szkript futásai ideje : ", (end-start)*10**3, "ms")