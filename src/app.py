@"
from utils import format_message

if __name__ == "__main__":
    print(format_message("Project OMG ready"))
"@ | Set-Content -Path src/app.py -Encoding utf8