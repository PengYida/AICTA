# 利用卡方检验筛选特征
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2

# 1.提取出方差分析后保留的特征
data = pd.read_excel('FiveFeature.xlsx')

print(data.name)
gene = pd.read_csv('newCombine.csv', index_col='Keys')
print(gene)
del gene['Unnamed: 0']
columns = data.name.values.tolist()
print(columns)
columns.append('Five')


gene = gene[columns]
# 输出处理好的数据
gene.to_csv('DataAfterProFive.csv')

#2.进行卡方检验提取K个最好的特征
#先将数据分为基因数据和Label
data = pd.read_csv('DataAfterProFive.csv', index_col='Keys')
target = data.Five.values

del data['Five']

gene_name = data.columns.values
gene = data.values
score = SelectKBest(chi2).score_func(gene, target)
print(gene_name)
zd = {
            'Name': gene_name,
            'Score': score[0],
            'P_value': score[1]
        }

feature = pd.DataFrame(zd)
feature = feature.sort_values(by='Score', ascending=False)
feature.to_csv('featureFive.csv')



