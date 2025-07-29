# 🧾 Slack Daily Task Automation

This Python script automates the daily posting of team tasks to a Slack channel using data from a shared Google Sheet. It runs automatically on weekdays and sends formatted messages to Slack users and the manager.

---

## ✅ Features

- Read task data from Google Sheets (team-editable)
- Format and post messages to Slack
- Skip weekends
- Support `.env` configuration
- Schedule using Windows Task Scheduler
- Easy to run via `.bat` file

---

## 🚀 Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/SlackDailyTaskAutomation.git
cd SlackDailyTaskAutomation
2. Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create .env file in the root folder
Create a file named .env and add the following values:
SLACK_TOKEN=xoxb-your-slack-bot-token
SLACK_CHANNEL=#your-channel-name
MANAGER_ID=U0XXXXXXX        # Slack User ID to CC
SHEET_URL=https://docs.google.com/spreadsheets/d/your-sheet-id/edit

## 🧪 Run Script Manually
python send_daily_task.py

## 📬 Output
A Slack message like:
<img width="1141" height="456" alt="Screenshot 2025-07-29 213305" src="https://github.com/user-attachments/assets/006c8332-9c2b-4ee3-9a0a-bacb024cbdee" />
