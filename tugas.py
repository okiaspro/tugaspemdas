import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print("DataFrame sebelum peningkatan gaji:")
print(df)

# loop for dan fungsi lambda untuk menghitung kenaikan 5% gaji karyawan.
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

# DataFrame yang sudah diperbarui
print("DataFrame setelah peningkatan 5% gaji:")
print(df)

# Ringkasan
summary_pertanyaan_2 = "Setiap karyawan menerima peningkatan gaji sebesar 5%."
print(summary_pertanyaan_2)

# loop for untuk mengevaluasi karyawan usiadi atas 30 tahun dan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])

        # DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan
print("\nDataFrame setelah peningkatan tambahan untuk usia di atas 30 tahun:")
print(df)

# Ringkasan 
summary_pertanyaan_4 = "Karyawan yang usianya di atas 30 tahun menerima peningkatan tambahan sebesar 2% dari gaji saat ini."
print(summary_pertanyaan_4)

