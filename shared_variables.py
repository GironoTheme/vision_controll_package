from pathlib import Path


disk_with_tesseract = 'E'


def find_path_to_folder(folder):
    for root_path in Path(f'{disk_with_tesseract}:\\').glob(f'**\\{folder}\\'):
        return root_path


path_to_pytesseract = f"{find_path_to_folder('teseract')}\\tesseract.exe"

