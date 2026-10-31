import json
import os
import urllib.request

def lambda_handler(event, context):
    print("AIOps Engine Received Anomaly Event:")
    print(json.dumps(event))
    
    # Extract details from the CloudWatch alarm payload
    alarm_name = event.get('alarmData', {}).get('alarmName', 'CloudWatch Anomaly Alarm')
    state_reason = event.get('alarmData', {}).get('state', {}).get('reason', 'AI model detected metric anomaly deviation.')
    
    message = f"🚨 AIOps Alert: Anomaly Detected!\n\nAlarm: {alarm_name}\nDetails: {state_reason}"
    
    print(message)
    # The event is successfully processed and can be routed to auto-remediation workflows.
    
    return {
        'statusCode': 200,
        'body': json.dumps('AIOps Event Processed Successfully')
    }
