import pandas as pd

# listing = pd.read_csv('..\data\winemag-data-130k-v2.csv')
# print(listing.head(14))

# listing = pd.read_excel('..\data\winemag-data-130k-v2.xlsx', index_col=7)
# print(listing.head(3))

listing = pd.read_excel('..\data\winemag-data-130k-v2.xlsx')
test = listing.set_index('title')
print(test)
