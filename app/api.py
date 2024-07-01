from flask import Blueprint, request, jsonify
from app.db import Database
import pandas as pd
from config import Config

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.csv'):
        table_name = file.filename.rsplit('.', 1)[0]  # Get the name of the table from the file name
        
        if table_name not in Config.TABLE_HEADERS:
            return jsonify({'error': 'Table name is not configured'}), 400

        headers = Config.TABLE_HEADERS[table_name]
        df = pd.read_csv(file, header=None)  # Read CSV without headers
        df.columns = headers  # Set the DataFrame headers from config

        # Remover linhas com valores nulos
        df = df.dropna()  # Remove todas as linhas com qualquer valor nulo

        db = Database()
        if not db.check_table_exists(table_name):
            db.create_table_from_sql(table_name)
        db.bulk_insert(df, table_name, headers)
        return jsonify({'message': 'File successfully uploaded'}), 200

    return jsonify({'error': 'Invalid file format'}), 400
