import pandas as pd

def load_abalone_data():
    abalone_data_path = '../abalone/abalone.data'
    column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
    abalone_df = pd.read_csv(abalone_data_path, header=None, names=column_names)
    abalone_df['Age'] = abalone_df['Rings'] + 1.5  # Age calculated from Rings
    return abalone_df
