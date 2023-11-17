from PIL import Image
import pytesseract
from openpyxl import load_workbook


def extrair_dados_imagem(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    return text



