import csv

sample = [{ 'stc': 'TJEHCMWVS03166', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }, { 'stc': 'TJEHCMWVS03165', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' },
          { 'stc': 'TJEHCMWVS03164', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }, { 'stc': 'TJEHCMWVS03163', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' },
          { 'stc': 'TJEHCMWVS03162', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }, { 'stc': 'TJEHCMWVS03161', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' },
          { 'stc': 'TJEHCMWVS03160', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }, { 'stc': 'TJEHCMWVS03159', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' },
          { 'stc': 'TJEHCMWVS03158', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }, { 'stc': 'TJEHCMWVS03157', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' },
          { 'stc': 'TJEHCN4OC00001', 'inqueue': '', 'inlog': '', 'outqueue': '', 'outlog': '' }]


def write_csv(filename: str, datalist: list):
    file = open(filename, 'w', newline = '')
    try:
        writer = csv.writer(file)
        for data in datalist:
            writer.writerow(data.values())
    finally:
        file.close()


write_csv('test_result.csv', sample)
