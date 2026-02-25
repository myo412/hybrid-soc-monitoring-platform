☁️ AWS OpenSearch SOC Architecture
📌 Overview
This implementation demonstrates a cloud-native SOC monitoring pipeline using AWS managed services.
The system collects AWS CloudTrail logs and visualizes them in OpenSearch Dashboards.
________________________________________
🏗 Architecture Flow
CloudTrail → S3 → Lambda → OpenSearch → Dashboard
________________________________________
🔍 Component Breakdown
1️⃣ AWS CloudTrail
•	Enabled for all regions
•	Logs API activity across AWS account
•	Configured to deliver logs to S3 bucket
________________________________________
2️⃣ Amazon S3
•	Stores CloudTrail log files in JSON format
•	Configured event notification to trigger Lambda
________________________________________
3️⃣ AWS Lambda
Purpose:
•	Parse CloudTrail JSON
•	Extract log records
•	Push each record to OpenSearch index soc-logs
IAM Role Permissions:
•	S3 Read Access
•	OpenSearch HTTP write access
________________________________________
4️⃣ Amazon OpenSearch
•	Managed search and analytics engine
•	Index created: soc-logs
•	Stores structured CloudTrail events
Index fields:
•	eventName
•	userName
•	sourceIPAddress
•	eventTime
________________________________________
5️⃣ OpenSearch Dashboards
Used for:
•	Creating index pattern soc-logs*
•	Visualizing logs
•	Building SOC dashboard
Visualizations:
•	Events Over Time (Line Chart)
•	Top Users (Pie Chart)
•	Top Event Types (Pie Chart)
•	Log Details Table
________________________________________
📊 Detection Capabilities
This architecture enables:
•	Monitoring of login activity
•	Detection of high-risk API actions
•	Tracking user behavior
•	Source IP analysis
•	Time-based anomaly detection
________________________________________
🔐 Security & Best Practices
•	IAM least privilege roles
•	HTTPS secured OpenSearch endpoint
•	Proper index pattern configuration
•	Log validation and testing using Python scripts
________________________________________
🚀 Future Enhancements
•	Alerting integration
•	Geo-IP enrichment
•	Anomaly detection
•	Slack/Email notification integration

