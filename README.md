📡 Network Traffic Analyzer (Packet Sentinel)

A professional CSV-based Network Traffic Analyzer built with Flask and Python.
This tool analyzes Wireshark-exported network traffic and provides visual insights into protocol distribution, traffic volume, and potential suspicious activity — all through a clean web dashboard.

🚀 Features

Upload Wireshark-style CSV files

Analyze real network traffic data

Protocol-wise traffic distribution

Top traffic-generating source IPs

Automatic detection of suspicious high traffic

Interactive, color-coded bar charts

Clean and professional dashboard UI

No raw packet data displayed after upload

📂 Supported CSV Format

The application supports CSV files exported from Wireshark with the following columns:

No, Time, Source, Destination, Protocol, Length, Info


Example:

1,0.041,192.168.1.3,20.190.144.139,TCP,54,ACK

🛠️ Tech Stack

Python 3

Flask

Pandas

Plotly

Bootstrap 5

📁 Project Structure
Packet_Sentinel/
│
├── app.py
├── templates/
│   └── dashboard.html
├── static/
│   └── style.css
├── uploads/
├── .gitignore
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Urusha-Lama/Network-Traffic-Analyzer.git
cd Network-Traffic-Analyzer

2️⃣ Create Virtual Environment (Recommended)
python -m venv pkts
pkts\Scripts\activate

3️⃣ Install Dependencies
pip install flask pandas plotly

4️⃣ Run the Application
python app.py


Open in browser:

http://127.0.0.1:5000

📊 How It Works

Upload a network traffic CSV file

The system processes traffic metrics

Protocol distribution is visualized

High traffic sources are identified

Suspicious traffic is flagged automatically

🔐 Use Cases

Cybersecurity academic projects

Network traffic analysis demonstrations

Intrusion Detection System (IDS) concepts

SOC dashboard simulation

Portfolio project for cybersecurity roles


👤 Author

Urusha Lama
Cybersecurity Enthusiast | Network Security Projects

📄 License

This project is open-source and available for educational and learning purposes.
