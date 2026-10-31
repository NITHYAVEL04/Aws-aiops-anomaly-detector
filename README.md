# Aws-aiops-anomaly-detector
AWS Serverless AIOps Anomaly Detection &amp; Alerting Pipeline

🚀 Project Overview
In modern production environments, traditional DevOps relies on static threshold alerts (e.g., “Alert if CPU > 80%”). These legacy setups cause severe alert fatigue due to false positives and fail to adapt to changing workloads.

This project implements an AIOps (Artificial Intelligence for IT Operations) Pipeline on AWS. Instead of static rules, it leverages CloudWatch Machine Learning Anomaly Detection to dynamically learn normal behavioral baselines, automatically detect metric anomalies, and trigger an event-driven self-healing/notification workflow using AWS Lambda and Amazon SNS.

📊 Architecture & Flow Diagram


  |   AWS EC2 Node    | (Generates operational telemetry / CPU metrics) ->  (Continuous Metric Ingestion) -> | Amazon CloudWatch | (ML-Driven Anomaly Detection Model & Dynamic Band) -> (Breach Trigger / State Change to ALARM) -> AWS CloudWatch -> |       Alarm       | -> (Invokes Event Payload) -> |    AWS Lambda     | (Serverless AIOps Event Handler & Python Script) -> (Dispatches Alert) -> |    Amazon SNS     | (Delivers real-time incident notification to Email)
 


🛠️ Resource Breakdown & Connectivity

1.Amazon EC2 (t2.micro / t3.micro): Acts as the target production compute node generating infrastructure metrics.
2.Amazon CloudWatch Metrics & Anomaly Detection: Applies advanced statistical machine learning algorithms to continuously analyze historical CPU patterns and map  out dynamic expected boundary bands.
3.CloudWatch Alarm: Evaluates real-time metrics against the AI model bounds and transitions state to ALARM when an operational deviation occurs.
4.AWS Lambda (Python 3.10): Serves as the serverless event processor. It catches the alarm payload, parses the incident metadata, and executes automated response logic.
5.Amazon SNS (Simple Notification Service): Handles reliable pub/sub fan-out messaging to instantly alert operations teams via email.

⭐ Key Features

1.Zero Local Footprint: Designed and executed 100% via the cloud (CloudShell and AWS Management Console), requiring zero local computing power.
2.Dynamic AI Baselines: Replaces brittle static thresholds with self-adjusting machine learning anomaly detection bands.
3.Event-Driven Architecture: Fully decoupled, serverless execution model utilizing native AWS integrations (CloudWatch → Lambda → SNS).
4.Cost-Optimized: Built entirely within the AWS Free Tier parameters using zero-provisioned idle servers for logic execution.

💡 The Problem & How This Solution Overcomes It

Traditional Monitoring (The Problem): 
Static Thresholds: Fixed limits (e.g., 80% CPU) trigger constantly during normal traffic spikes, causing alert fatigue.
Reactive & Manual: Engineers must manually look at dashboards to correlate issues after alarms fire.
High Overhead: Requires maintaining persistent monitoring servers or third-party agents.

AIOps Pipeline (Our Solution):
ML Baseline Modeling: Automatically adapts to traffic patterns and time-of-day variations.
Automated Event-Driven Handling: Lambda instantly catches and parses anomalies for automated triage or notification.
Serverless Native: Zero server maintenance, automated scaling, and fully managed by AWS.

🌐 Impact in the AWS DevOps World

In modern cloud environments managing hundreds or thousands of microservices, manual monitoring is unsustainable. AIOps shifts operations from reactive firefighting to intelligent automation.
By mastering serverless event-driven pipelines, CloudWatch machine learning models, and automated telemetry handling, DevOps engineers can drastically reduce Mean Time to Detection (MTTD) and Mean Time to Resolution (MTTR), ensuring high availability and robust system resilience.
