import pandas as pd
# 以下计算出了五年和三年的存活状态
data = pd.read_csv('Combine.CSV')
print(data)
alive = pd.DataFrame()
# 增加五年生存率和三年生存率
for i in range(0, len(data)):
    print('第', i, '个患者')
    # 病人是否生存期超过三年
    Three = -1
    Five = -1
    if data.iloc[i].status == 'Dead' and data.iloc[i].time <= 365*3:
        Three = 1
    else:
        Three = 0
    # 病人生存期是否超过五年
    if data.iloc[i].status == 'Dead' and data.iloc[i].time <= 365*5:
        Five = 1
    else:
        Five = 0
    temp = pd.Series({
        'Keys': data.iloc[i].Keys,
        'Three': Three,
        'Five': Five
    })
    print(temp)
    alive = alive.append(temp, ignore_index=True)

alive.to_csv('alive.csv')
combine = pd.merge(alive, data, on=['Keys'])
print(combine)
combine.to_csv('newCombine.csv')

# 将患者信息与基因数据进行合并
# 读入基因数据
data = pd.read_csv('LGG_data.csv', header=None, index_col=0)
data = data.T

# 将基因数据Keys中多余的三位删除
for i in range(0, len(data.Keys)):
    data.iloc[i].Keys = data.Keys.values[i][0:12]

# 读取患者随访信息，并只取出Keys和grade列
patient = pd.read_csv('alive.CSV')

# 根据Keys将基因数据和患者信息合并
combine = pd.merge(data, patient, on=['Keys'])

print(combine)
# 输出合并后的数据
combine.to_csv('CombineThreeFive.CSV')