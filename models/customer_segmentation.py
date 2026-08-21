import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def load_customer_data():
    return pd.read_csv("data/customer_features.csv")


def train_customer_model(customer_df, n_clusters=5):
    features = [
        "total_spend",
        "number_of_orders",
        "average_order_value",
        "recency_days",
        "customer_lifetime_days",
        "purchase_frequency",
        "unique_products"
    ]

    X = customer_df[features].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    customer_df["cluster"] = model.fit_predict(X_scaled)

    return customer_df, model, scaler