import pandas as pd  # pandas is a data analysis and manipulation tool
import uuid  # uuid is a Universally Unique Identifier generator
import numpy as np

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 32, 40, 28, 35],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eva@example.com']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Masking
df['name'] = 'XXX'
print("\nMasked Data:\n", df)

# Pseudonymisation
df['user_id'] = [str(uuid.uuid4()) for _ in range(len(df))]
df = df.drop(columns=['name'])
print("\nPseudonymized Data:\n", df)

# Generalisation
df['age'] = df['age'].apply(lambda x: '20-30' if 20 <= x <= 30 else '31-40')
print("\nGeneralized Data:\n", df)

# Data Perturbation
df['age'] = df['age'].apply(lambda x: x + str(np.random.randint(-2, 3)))
print("\nPerturbed Data:\n", df)
