import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

results = pd.read_csv('Data/nh_results.csv', header = 0)
results = results.rename(index = str, columns = {
'Town': "township"})


incomes = pd.read_csv('Data/pc_income_NH.csv', header = 0)

incomes = incomes[['Place', 'Per capita income']]
incomes = incomes.rename(index = str, columns = {
'Place': "township",
'Per capita income': "pci"})

incomes['township'] = incomes['township'].map(lambda x: x.lstrip('+-').rstrip(', New Hampshire'))
incomes['pci'] = incomes['pci'].str.replace('$', '')
incomes['pci'] = incomes['pci'].str.replace(',', '')
incomes['pci'] = incomes['pci'].astype(float)

merged = pd.merge(incomes, results)

merged['margin'] = merged.apply(lambda row: 100*(row.Sanders - row.Buttigieg)/(row.Sanders+row.Buttigieg),
                axis=1)

pci = np.array(merged['pci']).reshape(-1,1)
margin = np.array(merged['margin'])

from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()  # create object for the class
model = linear_regressor.fit(pci, margin)  # perform linear regression


Y_pred = linear_regressor.predict(pci)  # make predictions
r_sq = model.score(pci, margin)

from scipy import stats

pval = stats.ttest_ind(pci, margin).pvalue[0]

fig = plt.figure(figsize = (16, 12))
plt.rcParams.update({'font.size': 18})

plt.plot(pci, Y_pred, color='red')
plt.scatter(pci, margin, color = 'k', marker = 's')

plt.xlabel('Per-capita Income by NH Township (USD)')
plt.ylabel('Sanders vote margin on Buttigieg (%)')
plt.text(55000, 75, r'$R^2=$'+ str(round(r_sq, 5)))
plt.text(55000, 65, r'$p = 2.273 \times 10^{-142}$')
plt.savefig('nh_results.png', dpi = 300)
