import requests

def main():
    # Solicitar al usuario la cantidad de bitcoins que posee
    bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))

    try:
        # Consultar la API del índice de precios de Bitcoin de CoinDesk
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Levanta una excepción en caso de error en la solicitud

        # Obtener el precio actual de Bitcoin en USD desde la respuesta JSON
        data = response.json()
        price_usd = data["bpi"]["USD"]["rate_float"]

        # Calcular el costo actual de "n" Bitcoins en USD
        cost_usd = bitcoins * price_usd

        # Mostrar el costo actual de "n" Bitcoins en USD con cuatro decimales
        print(f"El costo actual de {bitcoins} Bitcoins es: ${cost_usd:.4f}")

    except requests.RequestException:
        print("Error al conectarse a la API de CoinDesk.")
    except KeyError:
        print("No se pudo encontrar el precio de Bitcoin en la respuesta JSON.")

if __name__ == "__main__":
    main()

