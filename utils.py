import os
from werkzeug.utils import secure_filename

def save_uploaded_file(uploaded_file, upload_folder):
    if uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(upload_folder, filename)
        uploaded_file.save(file_path)
        return filename
    return None
