from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

jwt_infos = {
    "KEY": os.getenv("KEY"),
    "ALGORITHM": os.getenv("ALGORITHM"),
    "JWT_HOURS": os.getenv("JWT_HOURS")
}
