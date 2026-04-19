# SOAR-Based-Automated-Incident-Response-for-RDP-Activity-in-Active-Directory

## 🧠 Project Overview


![image](https://github.com/KESAVA-0725/SOAR-Based-Automated-Incident-Response-for-RDP-Activity-in-Active-Directory/blob/main/Docs/AD.drawio.png?raw=true)

This project demonstrates a complete end-to-end Security Operations Center (SOC) home lab designed to simulate real-world enterprise security monitoring and automated incident response.

The primary objective of this lab is to detect Remote Desktop Protocol (RDP) login activity in a Windows Active Directory environment and automate the response workflow using SIEM and SOAR technologies. The system integrates log collection, detection, alerting, analyst decision-making, and automated remediation into a unified pipeline.

A Windows Server is configured as a Domain Controller with multiple domain users. A client machine is joined to the domain to simulate real user activity. RDP login events generated from this client are monitored using a SIEM platform. When suspicious activity is detected, alerts are generated and processed through a SOAR platform, where an analyst is given the option to respond. If approved, the system automatically disables the affected user account in Active Directory using a custom API.

This lab replicates a real-world SOC workflow where security teams monitor, analyze, and respond to threats in a structured and automated manner.

## 🎯 Objectives
- Simulate a real enterprise Active Directory environment
- Monitor RDP login activity in domain users
- Detect authentication events using SIEM
- Automate alert handling using SOAR
- Implement human-in-the-loop incident response
- Perform automated user account remediation
- Integrate alerting systems (Slack & Email)
- Build a complete detection-to-response pipeline

## 🏗️ Architecture
```
[Windows Client]
        │
        ▼
[Splunk SIEM] → (Alert Trigger)
        │
        ▼
[Tines SOAR]
        │
        ├── Slack Alert
        ├── Email Notification
        ├── Analyst Decision (Page Action)
        │
        ▼
[Condition Check]
        │
        ▼
[Flask API (Windows Server)]
        │
        ▼
[PowerShell Script]
        │
        ▼
[Active Directory]
        │
        ▼
[Slack Confirmation]
```

## 🧰 Technologies Used
- Splunk – Log monitoring & alerting
- Tines – Workflow automation
- Python (Flask) – API integration layer
- PowerShell – Active Directory management
- Active Directory – Identity and access control
- Slack – Alert notifications
- ngrok – Secure tunnel for API exposure
- Ubuntu – SIEM hosting environment
- Windows Server – Domain Controller
- Windows Client – Endpoint simulation
  
## 🔍 Detailed Workflow
### 🔹 Step 1 – Environment Setup

A Windows Server is configured as a Domain Controller using Active Directory. Multiple user accounts are created to simulate an organizational environment. A Windows client machine is joined to this domain to generate authentication events.

### 🔹 Step 2 – Log Collection

Splunk is installed on an Ubuntu machine to act as the SIEM platform. A Universal Forwarder is deployed on the Windows client system to forward Windows Security Event Logs to Splunk.

A dedicated index (home_lab) is created to store logs specifically related to this environment.

### 🔹 Step 3 – Detection

Splunk is configured to monitor RDP login events using Windows Event ID 4624 (successful logon events). When an RDP login is detected, an alert is triggered with details such as:

- Username
- Source IP address
- Timestamp

### 🔹 Step 4 – Alert Ingestion (SOAR)

The alert is sent to Tines via a webhook. This triggers the SOAR playbook, initiating the automated response workflow.

### 🔹 Step 5 – Notification

An HTTP action in Tines sends alert details to Slack and Email, notifying the SOC analyst about the detected activity.

### 🔹 Step 6 – Analyst Decision

A Page Action is presented to the analyst with options:

- YES → Disable user
- NO → Ignore

This step ensures human validation before taking critical actions.

### 🔹 Step 7 – Conditional Logic

A condition block evaluates the analyst’s response. If the decision is YES, the workflow proceeds to the remediation phase.

### 🔹 Step 8 – API Execution

A POST request is sent to a Flask API running on the Windows Server. This API acts as an integration layer between Tines and Active Directory.

### 🔹 Step 9 – Automated Response

The Flask application executes a PowerShell command:
```
Disable-ADAccount -Identity <username>
```
This disables the compromised user account in Active Directory.

### 🔹 Step 10 – Confirmation

After successful execution, a confirmation message is sent to Slack indicating that the user account has been disabled.

### 🔹 Step 11 – Validation

The final step involves verifying the disabled account in Active Directory, where the user is marked with a down-arrow icon.

## 🔐 Security Use Case

This lab simulates a real-world scenario where unauthorized or suspicious RDP access is detected and mitigated.

RDP is a common attack vector used in:

- Brute-force attacks
- Credential stuffing
- Lateral movement

By automating detection and response, this system reduces response time and minimizes risk.

## 📊 Key Features
- Real-time RDP monitoring
- Automated alert generation
- Human-in-the-loop response
- API-driven automation
- Active Directory integration
- Slack & Email notifications
- End-to-end SOC workflow

## ⚙️ Installation & Setup
### 🔹 Flask Setup
```
pip install flask requests
python app.py
```

### 🔹 ngrok Setup
```
ngrok http 5000
```

### 🔹 Splunk Setup
- Install Splunk on Ubuntu
- Start service
- Create index (home_lab)
- Configure forwarder

### 🔹 Tines Setup
- Create webhook
- Configure HTTP actions
- Add Page Action
- Add condition logic
- Integrate Slack

## 📌 Key Learnings
- SIEM log ingestion and analysis
- SOAR playbook development
- Active Directory automation
- API-based integrations
- Incident response lifecycle
- Real-world SOC simulation

## 🚀 Future Enhancements
- Integrate with Wazuh or ELK Stack
- Automate decision-making using AI/ML
- Add role-based access control
- Store logs in database
- Build dashboard for visualization
- Implement multi-user approval workflow
