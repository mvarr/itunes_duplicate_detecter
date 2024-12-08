import pandas as pd
import locale

# set your file path
file_path = 'Müzikler.txt'  # write your full path if necessary
output_path = 'Temizlenmiş_Müzikler.txt'

# Allow dynamic locale setting
locale_name = "tr_TR.UTF-8"  # Default to Turkish
try:
    locale.setlocale(locale.LC_TIME, locale_name)
except locale.Error:
    print(f"Warning: Locale '{locale_name}' not supported. Using system default.")
print("your locale has been set to:", locale_name)


# itunes exported file is tab separated and utf-16 encoded, so script trying to find the correct spesifications:
print("trying to read file...")
try:
    df = pd.read_csv(file_path, delimiter='\t', encoding='utf-16')
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path and try again.")
    exit(1)
except UnicodeDecodeError:
    print("Error: Unable to decode the file. Ensure it's UTF-16 encoded.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)
print("file found and read successfully.")

print("reading columns...")
required_columns = ['Sanatçı', 'Ad', 'Eklenme Tarihi']
if not all(col in df.columns for col in required_columns):
    print(f"Error: Missing one or more required columns: {required_columns}")
    exit(1)
print("columns read successfully.")

# # i am using itunes at turkish locale, so i need to set variables at turkish
df['Eklenme Tarihi'] = pd.to_datetime(df['Eklenme Tarihi'], format='%d %b %Y', errors='coerce')

# Keep the oldest song by grouping by "Sanatçı" and "Ad" columns
filtered_df = df.sort_values('Eklenme Tarihi').drop_duplicates(subset=['Sanatçı', 'Ad'], keep='first')

# Save the results in the same format
filtered_df.to_csv(output_path, sep='\t', index=False, encoding='utf-16')

print(f'file saved! new files name is: {output_path}')
