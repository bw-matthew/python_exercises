columns = ['INSPECTION_DATE', 'APPROVED_DATE']

for column in columns:
    print('transcoding the', column, 'column')
    for date_str in rodent_df[column]:
        inspection_datetime =datetime.datetime.strptime(date_str, format_descriptor)
        print(date_str, '-->', inspection_datetime) # compare before and after