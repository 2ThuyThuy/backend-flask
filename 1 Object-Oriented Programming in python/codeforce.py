def outlier_processing(data):
    # out possible range value
    all_error_units = []
    for sensor_id in range(20, 30):
        error_units = live_segments[(live_segments[f'min_{sensor_id}'] < -50) | 
                                    (live_segments[f'max_{sensor_id}'] > 350) |
                                    (live_segments[f'avg_{sensor_id}'] < -50) |
                                    (live_segments[f'max_{sensor_id}'] > 350)][['Timestamp', 'Unit']].Unit.unique()
        all_error_units.append(error_units)

    # upper outlier
    over_outlier = {'max_1': 250, 'stdev_1': 70, 'max_8': 100, 'percentile_7_50': 40, 
                    'max_8':100, 'stdev_15': 10000, 'max_17':1e6, 'min_35': 60000, 
                    'min_36':4000, 'max_36':50000, 'stdev_66': 100}
    for key, values in over_outlier.items():
        error_units = live_segments[live_segments[key] > values][['Timestamp', 'Unit']].Unit.unique()
        all_error_units.append(error_units)

    # lower outlier
    under_outlier = {'min_7': -40, 'min_8': -40, }
    for key, values in under_outlier.items():
        error_units = live_segments[live_segments[key] < values][['Timestamp', 'Unit']].Unit.unique()
        all_error_units.append(error_units)

    # recorded cumulative outlier
    temp = live_segments.copy().reset_index(drop=True)

    temp['diff_15'] = temp['max_15'] - temp['min_15']
    temp['diff_16'] = temp['max_16'] - temp['min_16']
    temp['diff_17'] = temp['max_17'] - temp['min_17']
    temp['diff_64'] = temp['max_64'] - temp['min_64']

 

    s1 = temp[(temp.diff_15 < 0)][['Timestamp', 'Unit']].Unit.unique()
    s2 = temp[(temp.diff_16 < 0)][['Timestamp', 'Unit']].Unit.unique()
    s3 = temp[(temp.diff_17 < 0)][['Timestamp', 'Unit']].Unit.unique()
    s4 = temp[(temp.diff_64 < 0)][['Timestamp', 'Unit']].Unit.unique()

 

    s5 = temp[(temp.diff_15 > 400)][['Timestamp', 'Unit']].Unit.unique()
    s6 = temp[(temp.diff_16 > 400)][['Timestamp', 'Unit']].Unit.unique()
    s7 = temp[(temp.diff_17 > 400)][['Timestamp', 'Unit']].Unit.unique()
    s8 = temp[(temp.diff_64 > 1e8)][['Timestamp', 'Unit']].Unit.unique()

    error_units = np.unique(np.concatenate([s1, s2, s3, s4, s5, s6, s7, s8]))
    all_error_units.append(error_units)
    all_error_units = set(np.concatenate(all_error_units))

    data = data[~data.Unit.isin(all_error_units)].reset_index(drop=True)
    return data