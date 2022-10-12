import pandas as pd

df = pd.read_csv(r'C:\Users\LEGION\Downloads\crop_yield\crop_yield\New_Data.csv')

def rice():
    rice_list = []
    
    
    for i in range(len(df.no)):
        if 'rice' == df.crop[i]:
            rice_list.append(i)

    data = pd.DataFrame()

    for indexes in sad_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.crop == 'rice')
    final_rice = data.dropna()
    print(final_rice)

def crops(expression):
    if expression == 'rice':
        print("you selected Rice Crop\n\n\n")
        rice()
    else:
        print(df)
