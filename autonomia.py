import math

import numpy as np
import matplotlib.pyplot as plt


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


def energia_restante(t):
    return E0 * np.exp(-K * t)


def criar_grafico_autonomia(autonomia):
    t = np.linspace(0, 40, 400)
    energia = energia_restante(t)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#080D1A")
    ax.set_facecolor("#0D1B2E")

    ax.plot(t, energia, color="#FF7A33", linewidth=2.5, label="E(t) = 120 * e^(-0.067t)")
    ax.axhline(E_SEG, color="#FF4444", linestyle="--", label=f"E_seg = {E_SEG:.0f} kWh")
    ax.axvline(autonomia, color="#00C9FF", linestyle=":", label=f"t* = {autonomia:.1f} h")
    ax.fill_between(
        t,
        energia,
        E_SEG,
        where=(energia >= E_SEG),
        alpha=0.15,
        color="#00C48C",
        label="Zona segura",
    )

    ax.set_xlabel("Tempo (horas)", color="white")
    ax.set_ylabel("Energia (kWh)", color="white")
    ax.set_title("AURORA - Curva de Autonomia Energetica", color="#FF7A33")
    ax.legend(facecolor="#111827", labelcolor="white")
    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_edgecolor("#1E293B")

    plt.tight_layout()


def main():
    autonomia = calcular_autonomia()
    cobertura_noite = calcular_cobertura_noite(autonomia)
    energia_no_limite = energia_restante(autonomia)

    print("Modelo energetico da Base Lunar AURORA")
    print("-" * 44)
    print(f"Energia inicial: {E0:.0f} kWh")
    print(f"Taxa de descarga: {K:.3f} h^-1")
    print(f"Limite seguro: {E_SEG:.0f} kWh")
    print(f"Noite lunar: aproximadamente {NOITE_LUNAR_HORAS:.0f} horas")
    print("-" * 44)
    print(f"Autonomia estimada: {autonomia:.1f} horas")
    print(f"Cobertura da noite lunar: {cobertura_noite:.1f}%")
    print(f"Energia no instante t*: {energia_no_limite:.1f} kWh")

    criar_grafico_autonomia(autonomia)
    plt.show()


if __name__ == "__main__":
    main()
