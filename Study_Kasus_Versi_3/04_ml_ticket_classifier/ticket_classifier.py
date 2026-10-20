"""Klasifikasi teks tiket layanan kampus dengan TF-IDF dan Logistic Regression."""
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts = [
    "wifi kampus tidak bisa tersambung", "internet laboratorium lambat",
    "akun jaringan tidak dapat login", "sinyal wifi putus-putus",
    "kartu mahasiswa saya hilang", "bagaimana mencetak kartu mahasiswa",
    "kartu identitas kampus rusak", "aktivasi kartu mahasiswa gagal",
    "jadwal kuliah berubah", "di mana melihat jadwal kelas",
    "kelas hari ini jam berapa", "jadwal ujian belum muncul",
    "wifi perpustakaan bermasalah", "saya perlu kartu mahasiswa baru",
    "jadwal kuliah di portal salah", "tidak bisa masuk jaringan kampus",
]
labels = [
    "TI", "TI", "TI", "TI",
    "Administrasi", "Administrasi", "Administrasi", "Administrasi",
    "Akademik", "Akademik", "Akademik", "Akademik",
    "TI", "Administrasi", "Akademik", "TI",
]
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=8, stratify=labels
)
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2)),
    LogisticRegression(max_iter=1000, random_state=8)
)
model.fit(X_train, y_train)
print(f"Akurasi pada data contoh: {accuracy_score(y_test, model.predict(X_test)):.2f}")
for message in [
    "saya tidak bisa login wifi kampus",
    "kartu mahasiswa saya rusak",
    "jadwal ujian belum terlihat",
]:
    print(f"Pesan: {message}\nUnit yang disarankan: {model.predict([message])[0]}\n")
print("Gunakan sebagai saran awal, bukan pengganti verifikasi petugas.")
