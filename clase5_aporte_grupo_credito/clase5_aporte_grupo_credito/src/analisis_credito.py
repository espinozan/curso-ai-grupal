"""Análisis exploratorio de morosidad por producto.

Clase 5 - Del análisis de datos a una propuesta de negocio.

El script evita modificar el CSV original. Hace revisión de calidad,
calcula indicadores descriptivos y genera una salida agregada.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DEFAULT_CANDIDATES = [
    Path("../modulo_3/dataset_credito.csv"),
    Path("data/dataset_credito.csv"),
    Path("dataset_credito.csv"),
]


def find_default_csv() -> Path | None:
    """Busca una ruta razonable sin asumir dónde está clonado el repositorio."""
    for path in DEFAULT_CANDIDATES:
        if path.exists():
            return path
    return None


def load_data(csv_path: Path) -> pd.DataFrame:
    """Carga el CSV y valida las columnas mínimas del análisis."""
    df = pd.read_csv(csv_path)
    required = {"PRODUCTO", "moroso"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas obligatorias: {sorted(missing)}")
    return df


def quality_report(df: pd.DataFrame) -> None:
    """Muestra controles básicos de calidad."""
    print("=== CALIDAD DE DATOS ===")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Duplicados exactos: {df.duplicated().sum()}")
    print("\nFaltantes por columna:")
    missing = df.isna().sum()
    print(missing[missing > 0].sort_values(ascending=False).to_string())

    # No corregimos automáticamente: solo señalamos valores que vale la pena revisar.
    if "edad" in df.columns:
        suspicious_age = df.loc[(df["edad"] < 18) | (df["edad"] > 100), "edad"]
        print(f"\nEdades potencialmente atípicas (<18 o >100): {len(suspicious_age)}")

    if "BCRA_Peor_Situacion" in df.columns:
        special_bcra = df.loc[df["BCRA_Peor_Situacion"] < 0, "BCRA_Peor_Situacion"]
        print(f"Valores negativos en BCRA_Peor_Situacion: {len(special_bcra)}")

    if "Nivel_Socioeconomico" in df.columns:
        special_nse = df.loc[df["Nivel_Socioeconomico"] < 0, "Nivel_Socioeconomico"]
        print(f"Valores negativos en Nivel_Socioeconomico: {len(special_nse)}")


def product_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula cantidad y proporción de morosos por producto."""
    result = (
        df.groupby("PRODUCTO", dropna=False)
        .agg(
            casos=("moroso", "size"),
            morosos=("moroso", "sum"),
            proporcion_morosos=("moroso", "mean"),
        )
        .sort_values("proporcion_morosos", ascending=False)
    )
    result["proporcion_morosos_pct"] = result["proporcion_morosos"] * 100
    return result


def save_outputs(df: pd.DataFrame, output_dir: Path) -> None:
    """Guarda resultados agregados y el gráfico."""
    output_dir.mkdir(parents=True, exist_ok=True)

    result = product_analysis(df).copy()
    result.reset_index().to_csv(
        output_dir / "morosidad_por_producto.csv", index=False
    )

    ax = result["proporcion_morosos_pct"].plot(
        kind="bar", figsize=(10, 5), rot=45
    )
    ax.set_title("Proporción de morosidad por producto")
    ax.set_xlabel("Producto")
    ax.set_ylabel("Morosos (%)")
    ax.grid(axis="y", alpha=0.25)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(output_dir / "grafico_morosidad_producto.png", dpi=160)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=None,
        help="Ruta al dataset_credito.csv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("resultados"),
        help="Carpeta de salida",
    )
    args = parser.parse_args()

    csv_path = args.csv or find_default_csv()
    if csv_path is None:
        raise FileNotFoundError(
            "No encontré dataset_credito.csv. Usá --csv /ruta/al/archivo.csv "
            "o colocalo en data/dataset_credito.csv."
        )

    print(f"Archivo utilizado: {csv_path}")
    df = load_data(csv_path)

    quality_report(df)

    general_rate = df["moroso"].mean() * 100
    print(f"\nMorosidad general: {general_rate:.2f}%")

    result = product_analysis(df)
    print("\n=== MOROSIDAD POR PRODUCTO ===")
    print(
        result[["casos", "morosos", "proporcion_morosos_pct"]]
        .round({"proporcion_morosos_pct": 2})
        .to_string()
    )

    save_outputs(df, args.output_dir)
    print(f"\nResultados guardados en: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
