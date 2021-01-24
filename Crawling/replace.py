import pandas as pd


data = pd.read_csv('res.csv', usecols=[0, 1], names=['date', 'tweet'])
warehouse = []
store = []
for date, tw in zip(data['date'], data['tweet']):
    tmp = []
    if tw not in warehouse:
        warehouse.append(tw)
        text = ''.join(tw)
        text = tw.replace(",", ' ')
        tmp.append(date)
        tmp.append(text)
    store.append(tmp)

f = open('final.csv', 'w')
for item in store:
    for i in range(len(item)):
        if i == 0:
            f.write(str(item[i]))
        else:
            f.write(',' + str(item[i]))
    f.write('\n')
f.close()
