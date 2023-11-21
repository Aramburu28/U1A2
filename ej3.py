#Exercise 3: List all process in operative system with PID, and allow termination of one by PID
import psutil

def list():
    for p in psutil.process_iter():
        print("Proceso " + p.name() + " con ID " + str(p.pid))
def terminar(id):
    proceso = psutil.Process(id)
    print("Terminando " + proceso.name())
    psutil.Process(id).terminate()
    print(proceso.name() + " Terminado exitosamente")
if __name__ == "__main__":
    list()
    elim = int(input("PID de proceso a terminar: "))
    terminar(elim)
