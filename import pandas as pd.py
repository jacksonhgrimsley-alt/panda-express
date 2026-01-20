import pandas as pd
from datetime import date

# Create sample data for sneaker collection
sneaker_collection = {
    'sneaker_id': [1, 2, 3, 4, 5],
    'brand': ['Nike', 'Jordan', 'Adidas', 'New Balance', 'Reebok'],
    'model': ['Air Force 1', 'Retro 1 High', 'Yeezy Boost 350', '990v6', 'Classic Leather'],
    'size': [10.5, 11.0, 9.5, 10.0, 10.5],
    'colorway': ['White/White', 'Bred', 'Zebra', 'Grey', 'White/Gum'],
    'release_year': [2007, 1985, 2017, 2022, 1983],
    'purchase_price': [110.99, 170.00, 220.50, 199.99, 89.95],
    'condition': ['Good', 'Excellent', 'New', 'Very Good', 'Fair'],
    'date_added': ['2024-01-15', '2024-02-10', '2024-03-05', '2024-04-20', '2024-05-12'],
    'is_favorite': [True, True, False, True, False]
}

# Create DataFrame
df = pd.DataFrame(sneaker_collection)

# Set appropriate data types
df['sneaker_id'] = df['sneaker_id'].astype('int64')
df['size'] = df['size'].astype('float64')
df['release_year'] = df['release_year'].astype('int64')
df['purchase_price'] = df['purchase_price'].astype('float64')
df['date_added'] = pd.to_datetime(df['date_added'])
df['is_favorite'] = df['is_favorite'].astype('bool')

# Display DataFrame information
print("DataFrame created successfully!")
print("\nDataFrame Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Export to CSV
csv_filename = 'sneaker_collection.csv'
df.to_csv(csv_filename, index=False)

print(f"\n✅ DataFrame exported to '{csv_filename}' successfully!")
print(f"📊 Total rows: {len(df)}, Total columns: {len(df.columns)}")