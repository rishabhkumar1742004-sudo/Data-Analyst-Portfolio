import pandas as pd
import numpy as np
import os

def clean_netflix_data():
    raw_path = 'netflix_titles.csv'
    print("Loading raw Netflix titles dataset...")
    df = pd.read_csv(raw_path)
    print(f"Initial shape: {df.shape}")
    
    # 1. Clean newline and carriage return characters from all string columns
    # (This prevents Power BI from breaking rows at newlines during CSV import)
    print("Removing newlines and carriage returns from text fields...")
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: str(x).replace('\n', ' ').replace('\r', ' ').strip() if pd.notnull(x) else x)
        
    # 2. Fix the rating/duration shift for Louis C.K. standups
    # (Where duration is null and rating has the duration e.g. "74 min")
    null_duration_idx = df[df['duration'].isnull()].index
    if len(null_duration_idx) > 0:
        print(f"Fixing rating/duration shift for {len(null_duration_idx)} rows...")
        df.loc[null_duration_idx, 'duration'] = df.loc[null_duration_idx, 'rating']
        df.loc[null_duration_idx, 'rating'] = 'Not Rated'
        
    # 3. Fill missing values for categorical columns
    print("Filling missing values...")
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Not Rated')
    
    # 4. Parse date_added to Datetime and extract year_added
    print("Parsing date_added and extracting year...")
    df['date_added'] = df['date_added'].str.strip()
    df['date_added_parsed'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
    df['year_added'] = df['date_added_parsed'].dt.year.astype('Int64') # Int64 allows nulls in integers
    
    # 5. Extract numeric duration value
    print("Extracting numeric duration values...")
    df['duration_value'] = df['duration'].str.split(' ').str[0].astype(float).fillna(0).astype(int)
    
    # 6. Drop duplicate show_ids (if any)
    print("Removing duplicate show IDs...")
    df.drop_duplicates(subset=['show_id'], inplace=True)
    
    # Remove old files if they exist to avoid confusion
    for f in ['netflix_titles_cleaned.csv', 'netflix_genres.csv', 'netflix_countries.csv']:
        if os.path.exists(f):
            os.remove(f)
            
    # Save the cleaned fact table directly as 'Titles.csv'
    fact_file = 'Titles.csv'
    fact_cols = [
        'show_id', 'type', 'title', 'director', 'cast', 'country', 
        'date_added_parsed', 'release_year', 'rating', 'duration', 
        'duration_value', 'year_added', 'description'
    ]
    fact_df = df[fact_cols].rename(columns={'date_added_parsed': 'date_added'})
    fact_df.to_csv(fact_file, index=False)
    print(f"Saved fact table to '{fact_file}' with shape {fact_df.shape}")
    
    # 7. Generate Genre Bridge Table and save as 'Genre.csv'
    print("Generating Genre Bridge Table...")
    genres_df = df[['show_id', 'listed_in']].copy()
    genres_df['genre'] = genres_df['listed_in'].str.split(', ')
    genres_df = genres_df.explode('genre')
    genres_df = genres_df[['show_id', 'genre']]
    genre_file = 'Genre.csv'
    genres_df.to_csv(genre_file, index=False)
    print(f"Saved Genre table to '{genre_file}' with shape {genres_df.shape}")
    
    # 8. Generate Country Bridge Table and save as 'Country.csv'
    print("Generating Country Bridge Table...")
    countries_df = df[['show_id', 'country']].copy()
    countries_df['country_split'] = countries_df['country'].str.split(', ')
    countries_df = countries_df.explode('country_split')
    countries_df = countries_df[['show_id', 'country_split']].rename(columns={'country_split': 'country'})
    country_file = 'Country.csv'
    countries_df.to_csv(country_file, index=False)
    print(f"Saved Country table to '{country_file}' with shape {countries_df.shape}")
    
    print("\nData cleaning and transformation completed successfully!")

if __name__ == "__main__":
    clean_netflix_data()
