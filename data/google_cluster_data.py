import pandas as pd

class GoogleClusterData:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_and_preprocess(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # Load CSV file
        df = pd.read_csv(self.file_path)

        # Basic preprocessing: remove rows with NaNs
        df.dropna(inplace=True)

        # Convert timestamp to datetime if exists
        if 'start_time' in df.columns:
            df['start_time'] = pd.to_datetime(df['start_time'], unit='s')
            df.set_index('start_time', inplace=True)

        # Sort by index if needed
        df.sort_index(inplace=True)

        # Resample if time-based index is present
        if df.index.inferred_type == 'datetime64':
            df = df.resample('1H').mean().interpolate()

        # Create a unified 'y' column for target if not present
        if 'y' not in df.columns:
            # Example: use CPU usage or task count as target
            candidate_cols = [col for col in df.columns if 'cpu' in col or 'task' in col]
            if candidate_cols:
                df['y'] = df[candidate_cols[0]]
            else:
                df['y'] = df.iloc[:, 0]  # fallback to first column

        return df[['y']]
