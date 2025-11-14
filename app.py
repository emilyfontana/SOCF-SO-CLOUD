
#Atividade ii cloud


from flask import Flask
import json
import os
import platform
import psutil

APP = Flask(__name__)


@APP.get("/info")
def home():
    return json.dumps([
        {
            'integrante': " Emily Pontes Fontana - 4u noite"
            
        }
    ])

@APP.get("/metricas")
def infos():
    processo = psutil.Process(os.getpid())
    # process ID
    pid = processo.pid

    # memória 
    mem = psutil.virtual_memory().used / 1024**2

    # uso médio de CPU
    cpu = psutil.cpu_percent(interval=0.1)

    # S.O utilizado
    sis = platform.platform()
#retorna infos
    return (
        f"| Nome: Emily Pontes Fontana "
        f"| PID: {pid}\n"
        f"| Memória usada: {mem:.2f} MB\n"
        f"| CPU: {cpu:.2f}%\n"
        f"| Sistema Operacional: {sis}\n"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # port Render
    APP.run(host="0.0.0.0", port=port)