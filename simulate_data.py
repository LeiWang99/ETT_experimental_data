import pandas as pd
import datetime
import random

'''
simulate normal physiological index data series
'''
def simulate_normal_data(num, count):
    time_list = [(datetime.datetime.now() + datetime.timedelta(seconds=i * 1)).strftime("%Y-%m-%d %H:%M:%S") for i in
                 range(0, count)]

    # the normal range for heart rate is in [60, 180]
    heart_rate_list = [random.randint(60, 180) for i in range(0, count)]

    # systolic blood pressure
    systolic_blood_pressure_list = [random.randint(90, 140) for i in range(count)]

    # diastolic blood pressure
    diastolic_blood_pressure_list = [random.randint(60, 90) for i in range(count)]

    step_num_list = [random.randint(1000, 8000) for i in range(count)]
    step_num_list.sort()

    distance_list = [round(random.uniform(0.3, 0.9) * step_num, 2) for step_num in step_num_list]

    label_list = [0 for i in range(count)]
    dataframe = pd.DataFrame({'date': time_list, 'heart_rate': heart_rate_list, 'systolic_blood_pressure': systolic_blood_pressure_list,
                              'diastolic_blood_pressure': diastolic_blood_pressure_list, 'step_num': step_num_list, 'distance': distance_list, 'labels': label_list})

    dataframe.to_csv("data/test/test_normal_original" + str(num) + ".csv", index=False, sep=',')

    return

'''
simulate abnormal physilogical index data series
'''
def simulate_abnormal_data(sequence_num):
    time_list = []
    heart_rate_list = []
    systolic_blood_pressure_list = []
    diastolic_blood_pressure_list = []
    step_num_list = []
    distance_list = []
    label_list = []

    # mock sequence_num data series, each sequence includes 10 timestamps
    for i in range(sequence_num):
        num = random.randint(1, 9)
        tl, hrl, sbpl, dbpl, ll = mock_abnormal(num)
        time_list += tl
        heart_rate_list += hrl
        systolic_blood_pressure_list += sbpl
        diastolic_blood_pressure_list += dbpl
        label_list += ll


    step_num_list = [random.randint(1000, 8000) for i in range(10 * sequence_num)]
    distance_list = [round(random.uniform(0.3, 0.9) * step_num, 2) for step_num in step_num_list]
    step_num_list.sort()
    distance_list.sort()

    dataframe = pd.DataFrame(
        {'date': time_list, 'heart_rate': heart_rate_list,
         'systolic_blood_pressure': systolic_blood_pressure_list,
         'diastolic_blood_pressure': diastolic_blood_pressure_list, 'step_num': step_num_list,
         'distance': distance_list, 'labels': label_list})

    dataframe.to_csv("data/test/test_abnormal_original"+ ".csv", index=False, sep=',')

    return


'''
mock abnormal data for each sequence, parameter 'low_num' in range [1,10]
'''
def mock_abnormal(low_num):
    ri = random.randint(0, 1)
    label_list = []

    time_list = [(datetime.datetime.now() + datetime.timedelta(seconds=i * 1)).strftime("%Y-%m-%d %H:%M:%S") for i in
                 range(0, 10)]

    heart_rate_list_1 = [random.randint(0, 60) for i in range(low_num)]
    heart_rate_list_2 = [random.randint(60, 180) for i in range(low_num)]

    if ri == 0:
        heart_rate_list = heart_rate_list_1 + [random.randint(180, 300) for i in range(10 - low_num)]

        systolic_blood_pressure_list = [random.randint(30, 100) for i in range(low_num)]
        systolic_blood_pressure_list += [random.randint(140, 200) for i in range(10 - low_num)]

        diastolic_blood_pressure_list = [random.randint(30, 60) for i in range(low_num)]
        diastolic_blood_pressure_list += [random.randint(90, 150) for i in range(10 - low_num)]

        label_list = [1 for i in range(10)]
    elif ri == 1:
        heart_rate_list = heart_rate_list_2 + [random.randint(180, 300) for i in range(10 - low_num)]

        systolic_blood_pressure_list = [random.randint(90, 140) for i in range(low_num)]
        systolic_blood_pressure_list += [random.randint(140, 200) for i in range(10 - low_num)]

        diastolic_blood_pressure_list = [random.randint(60, 90) for i in range(low_num)]
        diastolic_blood_pressure_list += [random.randint(90, 150) for i in range(10 - low_num)]

        label_list = [0 for i in range(low_num)] + [1 for i in range(10 - low_num)]

    return time_list, heart_rate_list, systolic_blood_pressure_list, diastolic_blood_pressure_list, label_list



