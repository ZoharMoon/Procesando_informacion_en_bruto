import requests

def descargar_datos_csv(url: str, nombre_archivo: str):
    try:
        
        response = requests.get(url)
        response.raise_for_status()  

        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(response.text)

        print(f"Datos descargados exitosamente y guardados en '{nombre_archivo}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos: {e}")


url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"


descargar_datos_csv(url_datos, "heart_failure_dataset.csv")
