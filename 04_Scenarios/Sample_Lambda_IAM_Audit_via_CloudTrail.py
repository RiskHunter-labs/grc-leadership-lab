import boto3
import datetime
import json

cloudtrail = boto3.client('cloudtrail')
sns = boto3.client('sns')
SENDER = 'compliance-alerts@yourdomain.com'
SNS_TOPIC_ARN = 'arn:aws:sns:us-gov-west-1:123456789012:ComplianceFindings'

EVENT_NAMES = [
    'CreateUser', 'DeleteUser', 'AttachUserPolicy',
    'PutUserPolicy', 'AddUserToGroup', 'RemoveUserFromGroup',
    'CreateAccessKey'
]

def lambda_handler(event, context):
    findings = []
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(days=7)

    for event_name in EVENT_NAMES:
        response = cloudtrail.lookup_events(
            LookupAttributes=[{'AttributeKey': 'EventName', 'AttributeValue': event_name}],
            StartTime=start_time,
            EndTime=end_time,
            MaxResults=50
        )
        
        for evt in response.get('Events', []):
            evt_data = json.loads(evt['CloudTrailEvent'])
            user_identity = evt_data.get('userIdentity', {}).get('arn', 'Unknown')
            mfa_used = evt_data.get('additionalEventData', {}).get('MFAUsed', 'No')

            if mfa_used == 'No':
                findings.append({
                    'EventName': event_name,
                    'Time': evt['EventTime'],
                    'User': user_identity,
                    'MFAUsed': mfa_used
                })

    if findings:
        message = f"IAM Alert: {len(findings)} event(s) without MFA\n\n"
        for f in findings:
            message += f"{f['Time']} - {f['EventName']} by {f['User']} (MFA: {f['MFAUsed']})\n"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="IAM Audit Alert – Unauthenticated Actions",
            Message=message
        )

    return {
        'statusCode': 200,
        'body': f"{len(findings)} unauthorized IAM actions flagged."
    }
