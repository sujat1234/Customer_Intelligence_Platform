from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # Load customer segmentation data
    data_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "customer_segments.csv"
    )

    df = pd.read_csv(data_path)

    # Get selected segment
    selected_segment = request.args.get(
        "segment",
        "All Segments"
    )

    # Filter data
    if selected_segment != "All Segments":
        filtered_df = df[
            df["segment"] == selected_segment
        ]
    else:
        filtered_df = df

    # --------------------------------
    # RFM SUMMARY
    # --------------------------------

    average_recency = (
        filtered_df["recency_days"].mean()
        if not filtered_df.empty
        else 0
    )

    average_frequency = (
        filtered_df["number_of_orders"].mean()
        if not filtered_df.empty
        else 0
    )

    average_monetary = (
        filtered_df["total_spend"].mean()
        if not filtered_df.empty
        else 0
    )

    # --------------------------------
    # DASHBOARD METRICS
    # --------------------------------

    total_customers = len(filtered_df)

    total_revenue = filtered_df["total_spend"].sum()

    average_customer_spend = (
        filtered_df["total_spend"].mean()
        if not filtered_df.empty
        else 0
    )

    total_segments = df["segment"].nunique()

    # --------------------------------
    # SEGMENT COUNTS AND REVENUE
    # --------------------------------

    if selected_segment == "All Segments":

        segment_counts = (
            df["segment"]
            .value_counts()
            .to_dict()
        )

        segment_revenue = (
            df.groupby("segment")["total_spend"]
            .sum()
            .round(2)
            .to_dict()
        )

    else:

        segment_counts = {
            selected_segment: len(filtered_df)
        }

        segment_revenue = {
            selected_segment:
            round(filtered_df["total_spend"].sum(), 2)
        }

    # --------------------------------
    # CUSTOMER TABLE
    # --------------------------------

    customer_columns = [
        "CustomerID",
        "segment",
        "total_spend",
        "number_of_orders",
        "average_order_value",
        "recency_days"
    ]

    customer_table = filtered_df[
        customer_columns
    ].copy()

    # Highest spending customers first
    customer_table = customer_table.sort_values(
        "total_spend",
        ascending=False
    )

    # Show top 20 customers
    customer_table = customer_table.head(20)

    # Convert to dictionary for HTML
    customer_table = customer_table.to_dict(
        orient="records"
    )

    # --------------------------------
    # CUSTOMER SEARCH
    # --------------------------------

    customer = None

    customer_id = request.form.get("customer_id")

    if customer_id:

        try:

            customer_id = int(customer_id)

            result = df[
                df["CustomerID"] == customer_id
            ]

            if not result.empty:
                customer = result.iloc[0].to_dict()

        except ValueError:

            customer = None

    # --------------------------------
    # AVAILABLE SEGMENTS
    # --------------------------------

    segments = [
        "All Segments",
        "Champions",
        "Loyal Customers",
        "At Risk",
        "New Customers",
        "High-Value Occasional"
    ]

    # --------------------------------
    # SEND DATA TO HTML
    # --------------------------------

    return render_template(
        "index.html",

        total_customers=total_customers,

        total_revenue=total_revenue,

        average_customer_spend=average_customer_spend,

        average_recency=average_recency,

        average_frequency=average_frequency,

        average_monetary=average_monetary,

        total_segments=total_segments,

        segment_counts=segment_counts,

        segment_revenue=segment_revenue,

        customer=customer,

        customer_table=customer_table,

        segments=segments,

        selected_segment=selected_segment
    )


if __name__ == "__main__":
    app.run(debug=True)