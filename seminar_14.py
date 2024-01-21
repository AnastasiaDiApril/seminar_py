# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
print()

one_hot_df = pd.DataFrame(columns=['robot', 'human'])
for index, row in data.iterrows():
    isRobot = 'robot' == row['whoAmI']
    isHuman = 'human' == row['whoAmI']
    one_hot_df.loc[len(one_hot_df)] = {'robot': isRobot, 'human': isHuman}

print(one_hot_df)
