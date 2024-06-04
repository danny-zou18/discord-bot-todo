from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from discord_interactions import verify_key_decorator
import boto3
from botocore.exceptions import ClientError
import os

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TASKS_TABLE_NAME']
table = dynamodb.Table(table_name)

@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)


@verify_key_decorator("1fd00a1eedaa0e600ef43e89c2678800127ad6841d7bbf43418e0fda0af90314")
def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "hello":
            message_content = "Hello there!"

        elif command_name == "echo":
            original_message = data["options"][0]["value"]
            message_content = f"Echoing: {original_message}"

        elif command_name == "addtask":
            task_id = data["options"][0]["value"]
            task_description = data["options"][1]["value"]

            try:
                response = table.put_item(
                    Item={
                        'taskId': task_id,
                        'taskDescription': task_description,
                        'status': 'pending'
                    }
                )
                message_content = f"Task added successfully with ID: {task_id}"
            except ClientError as e:
                if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                    message_content = f"Task with ID: {task_id} already exists."
                else:
                    raise

        elif command_name == "tasks":
            tasks = get_all_tasks()
            message_content = "\n".join([f"Task ID: {task['taskId']}, Description: {task['taskDescription']}, Status: {task['status']}" for task in tasks])

        elif command_name == "remove":
            task_id = data["options"][0]["value"]

            try:
                response = table.delete_item(
                    Key={
                        'taskId': task_id
                    }
                )
                message_content = f"Task with ID {task_id} removed successfully"
            except ClientError as e:
                if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                    message_content = f"Task with ID: {task_id} not found."
                else:
                    raise  # Raise the exception for unexpected errors 

        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)

def get_all_tasks():
    response = table.scan()
    return response['Items']


if __name__ == "__main__":
    app.run(debug=True)