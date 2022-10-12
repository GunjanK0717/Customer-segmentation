catagories = input("Enter Product Cat")

if (catagories == 'grocery'):
    data = df.where(df.Pcatagories == "grocery")
    final_groc = data.dropna()
    print(final_groc)
elif (catagories == 'fashion'):
    data = df.where(df.Pcatagories == "fashion")
    final_groc = data.dropna()
    print(final_groc)
elif (catagories == 'hardware'):
    data = df.where(df.Pcatagories == "hardware")
    final_groc = data.dropna()
    print(final_groc)
elif (catagories == 'tools'):
    data = df.where(df.Pcatagories == "tools")
    final_groc = data.dropna()
    print(final_groc)
elif (catagories == 'jwellery'):
    data = df.where(df.Pcatagories == "jwellery")
    final_groc = data.dropna()
    print(final_groc)