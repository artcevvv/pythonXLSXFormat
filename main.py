import pandas as pd;

delim = '\n'

spreadsht = pd.read_excel('./goods.xlsx', index_col=0)
spreadshtAsList= spreadsht.index.to_list()
spreadshtAsStr = [str(i) for i in (spreadshtAsList)]
formattedTextList = []
formattedPriceList = []


for i in range(len(spreadshtAsList)):
    slicedText = spreadshtAsList[i].split("по ")
    artifactRemoved = slicedText[1].replace(', , шт' or ' ', '')
    formattedTextList.append(slicedText[0].capitalize())
    formattedPriceList.append(artifactRemoved)


df = pd.DataFrame({
    'Имя': formattedTextList,
    'Тип': 'simple',
    'Базовая цена': formattedPriceList
})

df.to_csv('formatted_goods.csv', index=False)