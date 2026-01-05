from flask import Flask, render_template, request
import pandas as pd
import os
import plotly.express as px
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def analyze_traffic(df):
    df.columns = ['No','Time','Source','Destination','Protocol','Length','Info']

    df['Length'] = pd.to_numeric(df['Length'], errors='coerce').fillna(0)

    # Metrics
    protocol_stats = df['Protocol'].value_counts().reset_index()
    protocol_stats.columns = ['Protocol', 'Packets']

    traffic_by_source = df.groupby('Source')['Length'].sum().reset_index()
    traffic_by_source.columns = ['Source', 'Bytes']
    traffic_by_source = traffic_by_source.sort_values(by='Bytes', ascending=False).head(10)

    # Suspicious traffic detection
    threshold = traffic_by_source['Bytes'].mean() * 2
    suspicious = traffic_by_source[traffic_by_source['Bytes'] > threshold]

    return protocol_stats, traffic_by_source, suspicious

@app.route("/", methods=["GET", "POST"])
def dashboard():
    protocol_graph = None
    traffic_graph = None
    alert = None

    if request.method == "POST":
        file = request.files.get('file')

        if not file or file.filename == "":
            alert = "Please upload a valid CSV file."
        else:
            df = pd.read_csv(file)

            protocol_stats, traffic_by_source, suspicious = analyze_traffic(df)

            # Protocol Bar Chart
            fig1 = px.bar(
                protocol_stats,
                x='Protocol',
                y='Packets',
                title='Traffic Distribution by Protocol',
                color='Protocol'
            )
            protocol_graph = fig1.to_html(full_html=False)

            # Traffic by Source Bar Chart
            fig2 = px.bar(
                traffic_by_source,
                x='Source',
                y='Bytes',
                title='Top Traffic Generating Sources',
                color='Bytes',
                color_continuous_scale='Turbo'
            )
            traffic_graph = fig2.to_html(full_html=False)

            if not suspicious.empty:
                alert = "⚠️ Suspicious high traffic detected from one or more sources!"

    return render_template(
        "dashboard.html",
        protocol_graph=protocol_graph,
        traffic_graph=traffic_graph,
        alert=alert
    )

if __name__ == "__main__":
    app.run(debug=True)
