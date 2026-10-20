"""Menandai transaksi kantin ekstrem menggunakan robust statistics."""
import pandas as pd

df = pd.DataFrame({
    "id_transaksi": ["K001", "K002", "K003", "K004", "K005", "K006", "K007", "K008"],
    "total_rupiah": [12000, 15000, 9000, 18000, 14000, 16000, 12500, 185000],
})
median = df["total_rupiah"].median()
mad = (df["total_rupiah"] - median).abs().median()
# Batas robust sederhana; bila MAD nol, hindari pembagian nol.
df["skor_robust"] = 0 if mad == 0 else 0.6745 * (df["total_rupiah"] - median) / mad
df["perlu_ditinjau"] = df["skor_robust"].abs() > 3.5

print(f"Median transaksi: Rp{median:,.0f}")
print(df.to_string(index=False))
print("\nTransaksi yang perlu ditinjau:")
print(df[df["perlu_ditinjau"]].to_string(index=False))
print("Flag otomatis bukan bukti kesalahan; periksa konteks transaksi terlebih dahulu.")
