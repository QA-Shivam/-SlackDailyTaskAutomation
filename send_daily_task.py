import pandas as pd
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Constants from .env
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
EXCEL_PATH = os.getenv("EXCEL_PATH")
SLACK_MANAGER_ID = os.getenv("MANAGER_ID")  # e.g., U01XXXXXXX

# Get today's date and weekday
today = datetime.now()
weekday = today.strftime("%A")
formatted_date = today.strftime("%d-%B-%Y")  # e.g., 29-July-2025

# Skip weekends
if weekday in ["Saturday", "Sunday"]:
    print("📆 Weekend! Skipping task post.")
    exit()

# Load Excel file
try:
    df = pd.read_excel(EXCEL_PATH, engine="openpyxl")  # use xlrd for .xls
except Exception as e:
    print(f"❌ Failed to read Excel: {e}")
    exit()

# Check required columns
required_cols = {'Task Summary', 'Assignee Name', 'Slack User ID'}
if not required_cols.issubset(df.columns):
    print(f"❌ Missing required columns in Excel. Expected: {required_cols}")
    exit()

# Filter out empty rows
df = df.dropna(subset=['Task Summary', 'Slack User ID'])

if df.empty:
    print("⚠️ No valid tasks found in the Excel file.")
    exit()

# Prepare Slack message
message = f"*📅 Web Automation Tasks for {weekday}, {formatted_date}*\n\n"

for _, row in df.iterrows():
    task = str(row['Task Summary']).strip()
    slack_id = str(row['Slack User ID']).strip()
    message += f"📌 <@{slack_id}> : *{task}*\n"

# Add manager in CC
if SLACK_MANAGER_ID:
    message += f"\n*👤 CC:* <@{SLACK_MANAGER_ID}>"

# Send message to Slack
client = WebClient(token=SLACK_TOKEN)

try:
    response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
    print("✅ Task posted to Slack")
except SlackApiError as e:
    print(f"❌ Slack API Error: {e.response['error']}")
