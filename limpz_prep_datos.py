import pandas as pd

def procesar_datos(dataframe):
    
    if dataframe.isnull().values.any():
        dataframe = dataframe.dropna()
        print("Valores faltantes eliminados.")

    
    if dataframe.duplicated().any():
        dataframe = dataframe.drop_duplicates()
        print("Filas duplicadas eliminadas.")

    
    columns_numeric = dataframe.select_dtypes(include=['number']).columns
    for col in columns_numeric:
        
        lower_bound = dataframe[col].quantile(0.01)
        upper_bound = dataframe[col].quantile(0.99)
        dataframe = dataframe[(dataframe[col] >= lower_bound) & (dataframe[col] <= upper_bound)]

    print("Valores atípicos eliminados.")

    
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    dataframe['Categoria_Edad'] = pd.cut(dataframe['age'], bins=bins, labels=labels, right=False)

    
    dataframe.to_csv("datos_procesados.csv", index=False)
    print("Datos procesados guardados en 'datos_procesados.csv'.")

    return dataframe


nombre_archivo = "heart_failure_dataset.csv"
df = pd.read_csv(nombre_archivo)


df_procesado = procesar_datos(df)
