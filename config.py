class Config:
    DB_NAME = 'human_resources'
    DB_USER = 'prado'
    DB_PASSWORD = 'Prado'
    DB_HOST = 'db'
    DB_PORT = 5432

 # Define os cabeçalhos das tabelas aqui
    TABLE_HEADERS = {
        'departments': ['id', 'department'],
        'hired_employees': ['id', 'name', 'datetime', 'department_id', 'job_id'],
        'jobs': ['id', 'job']
    }