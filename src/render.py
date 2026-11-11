import os
from functools import wraps

def validar_diretorio(func):
    @wraps(func)
    def wrapper(mypath, *args, **kwargs):

        current_dir = mypath[1:]

        if not os.path.exists(mypath):

            if os.path.exists(current_dir):
                return func(current_dir , *args, **kwargs)

            raise FileNotFoundError(f"Erro: O diretório '{mypath}' não foi encontrado.")
        
        return func(mypath, *args, **kwargs)
    return wrapper

@validar_diretorio
def return_files_from_directory(mypath):
    for (_, _, filenames) in os.walk(mypath):
        return filenames  # Simplificado: já retorna direto no primeiro loop
    return []

if __name__ == '__main__':
    
    jobs_directory = "../jobs"

    files = return_files_from_directory(jobs_directory)
    print(files)


