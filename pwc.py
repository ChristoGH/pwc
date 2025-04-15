import pandas as pd
import os
import glob

def extract_bank_info(file_path):
    try:
        # Read the first few lines manually to get the header information
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Extract date and bank name from the first two lines
        date = lines[0].strip().split(',')[1].strip()
        bank_name = lines[1].strip().split(',')[1].strip()
        
        # Read the file for processing the credit impairments
        # Skip the first 6 rows as they contain header information
        df = pd.read_csv(file_path, skiprows=6, dtype=str)  # Read all columns as string initially
        
        # Find the row where Item Number is 194
        impairment_row = df[df['Item Number'] == '194']
        
        if not impairment_row.empty:
            try:
                # Get the value from column 7 (0-based index 6)
                impairment_value = impairment_row.iloc[0, 6]
                # Convert to float and multiply by 1000 (as values are in thousands)
                impairment_value = float(impairment_value.replace(',', '')) * 1000 if pd.notnull(impairment_value) else None
            except (ValueError, AttributeError) as e:
                print(f"Error converting impairment value in {file_path}: {e}")
                impairment_value = None
        else:
            print(f"No item number 194 found in {os.path.basename(file_path)}")
            impairment_value = None
        
        return {
            'date': date,
            'bank_name': bank_name,
            'credit_impairments': impairment_value,
            'file_name': os.path.basename(file_path)
        }
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return None

def process_all_files():
    # Get all CSV files in the pwc_data directory
    csv_files = glob.glob('pwc_data/*.csv')
    
    # Process each file and collect results
    results = []
    for file_path in csv_files:
        info = extract_bank_info(file_path)
        if info is not None:
            results.append(info)
    
    # Convert results to DataFrame for easy viewing/export
    if results:
        results_df = pd.DataFrame(results)
        # Format the credit_impairments as currency
        results_df['credit_impairments'] = results_df['credit_impairments'].apply(
            lambda x: f"R{x:,.2f}" if pd.notnull(x) else None
        )
        # Sort by bank name
        results_df = results_df.sort_values('bank_name')
        return results_df
    else:
        return pd.DataFrame(columns=['date', 'bank_name', 'credit_impairments', 'file_name'])

if __name__ == "__main__":
    results_df = process_all_files()
    print("\nProcessed Bank Information:")
    print(results_df)
    
    # Save to CSV
    results_df.to_csv('bank_impairments_summary.csv', index=False)