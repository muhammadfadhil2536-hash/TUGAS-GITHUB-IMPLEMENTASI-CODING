"""Demo confidence score untuk alert perubahan tutupan lahan sintetis."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Fitur sintetis: perubahan indeks vegetasi, perubahan tekstur, ukuran area.
X = [
    [0.1, 0.2, 0.1], [0.2, 0.1, 0.2], [0.15, 0.25, 0.15],
    [0.3, 0.35, 0.25], [0.4, 0.45, 0.4], [0.45, 0.5, 0.35],
    [0.55, 0.6, 0.55], [0.65, 0.7, 0.65], [0.7, 0.75, 0.8],
    [0.85, 0.8, 0.9], [0.9, 0.9, 0.85], [0.6, 0.55, 0.6],
    [0.25, 0.3, 0.2], [0.5, 0.45, 0.5], [0.8, 0.85, 0.75],
    [0.35, 0.4, 0.3], [0.75, 0.65, 0.7], [0.95, 0.9, 0.95],
]
y = ["Perubahan rendah"]*6 + ["Perubahan sedang"]*6 + ["Perubahan tinggi"]*6

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=13, stratify=y
)
model = RandomForestClassifier(n_estimators=120, random_state=13)
model.fit(X_train, y_train)
print(f"Akurasi uji sintetis: {accuracy_score(y_test, model.predict(X_test)):.2f}")

sample = [[0.72, 0.76, 0.71]]
probs = model.predict_proba(sample)[0]
best_index = probs.argmax()
print("Kelas prediksi:", model.classes_[best_index])
print(f"Skor keyakinan model: {probs[best_index]:.1%}")
print("Alert tetap perlu pemeriksaan citra, konteks waktu, dan validasi lapangan.")
