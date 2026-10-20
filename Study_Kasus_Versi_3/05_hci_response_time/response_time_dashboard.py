"""Analisis waktu respons tiket dan visualisasi."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "kategori": ["Akademik", "TI", "Administrasi", "Akademik", "TI",
                 "Administrasi", "Akademik", "TI", "Administrasi"],
    "jam_respons": [5, 2, 8, 7, 3, 6, 4, 5, 9],
})
summary = df.groupby("kategori")["jam_respons"].agg(["mean", "median", "count"]).reset_index()
print("Ringkasan waktu respons (data sintetis):")
print(summary.round(2).to_string(index=False))

ax = summary.plot(x="kategori", y="mean", kind="bar", legend=False)
ax.set_title("Rata-rata Waktu Respons per Layanan")
ax.set_xlabel("Kategori layanan")
ax.set_ylabel("Waktu respons (jam)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("response_time_chart.png", dpi=150)
print("\nGrafik tersimpan: response_time_chart.png")
