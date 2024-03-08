from pathlib import Path


def find_path_to_folder(folder):
    for root_path in Path('E:\\').glob(f'**\\{folder}\\'):
        return root_path


path_to_pytesseract = f"{find_path_to_folder('teseract')}\\tesseract.exe"

