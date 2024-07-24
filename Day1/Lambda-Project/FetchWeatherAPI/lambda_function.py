import json
import requests

def lambda_handler(event, context):
    city = event.get('city', 'Hanoi')  # Get city from event or default to Hanoi
    api_key = "934044d634b14dfbb8751333242407"  # Replace with your actual API key
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        weather_data = response.json()
        
        return {
            'statusCode': 200,
            'body': json.dumps(weather_data)
        }
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")  # Log error to CloudWatch
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': f'HTTPError: {str(e)}'})
        }
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # Log error to CloudWatch
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'RequestException: {str(e)}'})
        }