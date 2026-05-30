import math


# autonomia.py - Modelo energetico da Base Lunar AURORA


# Parametros iniciais do problema
E0 = 120.0  # kWh - energia inicial armazenada
K = 0.067  # h^-1 - taxa de descarga
E_SEG = 48.0  # kWh - limite seguro, equivalente a 40% de E0
NOITE_LUNAR_HORAS = 336.0  # horas - duracao aproximada da noite lunar


def calcular_autonomia():
    return (1 / K) * math.log(E0 / E_SEG)


def calcular_cobertura_noite(autonomia):
    return autonomia / NOITE_LUNAR_HORAS * 100


def main():
    autonomia = calcular_autonomia()
    cobertura_noite = calcular_cobertura_noite(autonomia)

    print("Modelo energetico da Base Lunar AURORA")
    print("-" * 44)
    print(f"Energia inicial: {E0:.0f} kWh")
    print(f"Taxa de descarga: {K:.3f} h^-1")
    print(f"Limite seguro: {E_SEG:.0f} kWh")
    print(f"Noite lunar: aproximadamente {NOITE_LUNAR_HORAS:.0f} horas")
    print("-" * 44)
    print(f"Autonomia estimada: {autonomia:.1f} horas")
    print(f"Cobertura da noite lunar: {cobertura_noite:.1f}%")


if __name__ == "__main__":
    main()
