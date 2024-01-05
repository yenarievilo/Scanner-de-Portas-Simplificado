import argparse
import socket
from colorama import init, Fore

# Cores para identificação
init()
VERDE = Fore.GREEN
RESET = Fore.RESET
CINZA = Fore.LIGHTBLACK_EX

def porta_esta_aberta(host, porta):
    """
    Determina se o `host` possui a `porta` aberta
    """
    s = socket.socket()
    try:
        s.connect((host, porta))
        s.settimeout(0.2)
    except:
        return False
    else:
        return True

def verificar_portas(host, porta_inicial, porta_final):
    """
    Verifica as portas de `porta_inicial` a `porta_final` no `host`
    """
    for porta in range(porta_inicial, porta_final + 1):
        if porta_esta_aberta(host, porta):
            print(f"{VERDE}[+] {host}:{porta} está aberta      {RESET}")
        else:
            print(f"{CINZA}[!] {host}:{porta} está fechada    {RESET}", end="\r")

def main():
    parser = argparse.ArgumentParser(description="Scanner Simplificado.")
    parser.add_argument("host", help="O host a ser verificado")
    parser.add_argument("--porta-inicial", type=int, default=1, help="Porta inicial do intervalo (padrão: 1)")
    parser.add_argument("--porta-final", type=int, default=1024, help="Porta final do intervalo (padrão: 1024)")

    args = parser.parse_args()

    verificar_portas(args.host, args.porta_inicial, args.porta_final)

if __name__ == "__main__":
    main()
