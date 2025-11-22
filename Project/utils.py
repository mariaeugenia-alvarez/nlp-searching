import os
import json


def load_automotive_reviews(datasets_path, jsonl_file):
    """
    Carga reseñas de productos automotrices desde un archivo JSONL.

    Args:
        datasets_path: Ruta al directorio donde está el archivo
        jsonl_file: Nombre del archivo JSONL (ej: 'Automotive.jsonl')

    Returns:
        Dict con las reseñas indexadas por número
    """
    reviews_dict = {}
    file_path = os.path.join(datasets_path, jsonl_file)

    with open(file_path, "r", encoding="utf-8") as fp:
        for idx, line in enumerate(fp):
            review = json.loads(line.strip())
            reviews_dict[idx] = review

    return reviews_dict
