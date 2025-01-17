# skes_name = np.loadtxt(skes_name_file, dtype=str)
# num_files = skes_name.size
# print('Found %d available skeleton files.' % num_files)

import os
files = os.listdir("C:\Projects\HD-GCN\data\\nturgbd_raw\\nturgb+d_skeletons120")
output_file = "C:\Projects\HD-GCN\\tmp_for_me"
with open(output_file, 'w', encoding='utf-8') as f:
    for file in files:
        f.write(file.replace('.skeleton', '') + '\n')
#последнюю пустую строку в получившемся файле удалю вручную пока