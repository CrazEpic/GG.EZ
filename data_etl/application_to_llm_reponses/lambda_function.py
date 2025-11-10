import json
import boto3

# Bedrock client used to interact with APIs around models
bedrock = boto3.client(
    service_name="bedrock",
)

# Bedrock Runtime client used to invoke and question the models
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
)


def handler(event, context):
    prompt = json.loads(event.get("body")).get("input").get("question")

    # The payload to be provided to Bedrock
    body = json.dumps(
        {
            "prompt": prompt,
            "maxTokens": 200,
            "temperature": 0.7,
            "topP": 1,
        }
    )

    # The actual call to retrieve an answer from the model
    response = bedrock_runtime.invoke_model(body=body, modelId="anthropic.claude-3-5-haiku-20241022-v1:0", accept="application/json", contentType="application/json")

    response_body = json.loads(response.get("body").read())

    # The response from the model now mapped to the answer
    answer = response_body.get("completions")[0].get("data").get("text")
