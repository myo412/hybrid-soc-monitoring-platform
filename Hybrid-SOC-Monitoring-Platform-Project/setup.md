VM-Based ELK Stack Setup Guide
📌 Overview
This section documents the deployment of a self-managed ELK (Elasticsearch, Logstash, Kibana) stack on virtual machines to simulate an on-premises SOC monitoring environment.
The system ingests CloudTrail-like logs using Python and visualizes them in Kibana.
________________________________________
🧱 Environment Setup
Virtual Machines
•	Platform: VirtualBox / VMware / Hyper-V
•	OS: Ubuntu Server / Windows Server
•	RAM: Minimum 4GB recommended
•	Opened Ports:
o	9200 → Elasticsearch
o	5601 → Kibana
________________________________________
🔎 Step 1: Install Elasticsearch
Download Elasticsearch
From:
https://www.elastic.co/downloads/elasticsearch
Configuration
Edit elasticsearch.yml:
network.host: 0.0.0.0
discovery.type: single-node
This allows single-node operation and external access.
Start Elasticsearch
Linux:
sudo systemctl start elasticsearch
Windows:
Run elasticsearch.bat
Verify Installation
Open browser:
http://localhost:9200
You should see cluster information in JSON format.
________________________________________
📊 Step 2: Install Kibana
Download from:
https://www.elastic.co/downloads/kibana
Edit kibana.yml:
server.port: 5601
elasticsearch.hosts: ["http://localhost:9200"]
Start Kibana:
Linux:
sudo systemctl start kibana
Windows:
Run kibana.bat
Access:
http://localhost:5601
________________________________________
📝 Step 3: Log Ingestion Using Python
Created Python script:
push_logs.py
The script:
•	Generates simulated CloudTrail logs
•	Pushes logs into Elasticsearch index soc-logs
Fields included:
•	eventName
•	userName
•	sourceIPAddress
•	eventTime
After running the script:
python push_logs.py
Verify using:
GET soc-logs/_search
________________________________________
📈 Step 4: Create Kibana Index Pattern
1.	Go to Kibana → Stack Management
2.	Click Index Patterns
3.	Create new pattern:
4.	soc-logs*
5.	Select eventTime as time field
________________________________________
📊 Step 5: Create SOC Dashboard
Visualizations created:
1.	Events Over Time (Line Chart)
2.	Top Users (Pie Chart)
3.	Top Event Types (Pie Chart)
4.	Log Details Table
All visualizations added to:
SOC Monitoring Dashboard
________________________________________
🔐 Security Monitoring Use Cases
•	Monitor ConsoleLogin activity
•	Track IAM user creation
•	Detect bucket deletion
•	Analyze API activity trends
•	Monitor source IP addresses
________________________________________
🛠 Troubleshooting
Common issues resolved:
•	Index pattern time mismatch
•	Elasticsearch not starting
•	Port conflicts
•	Dashboard not refreshing due to time filter
________________________________________
________________________________________

