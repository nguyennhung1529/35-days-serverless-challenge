def lambda_handler(event, context):
    try:
        # Your code here
        result = "Hello, World!"
        return {
            'statusCode': 200,
            'body': result
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
