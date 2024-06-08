import boto3
import json

class BedrockChat:
    def __init__(self, secret_name="opensearch_serverless_secrets"):
        self.session = boto3.session.Session()
        self.region_name = self.session.region_name
        self.bedrock_client = boto3.client('bedrock-agent-runtime')
        self.client = self.session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )
        self.secret_name = secret_name
        self.knowledge_base_id = self._get_knowledge_base_id()

    def _get_knowledge_base_id(self):
        get_secret_value_response = self.client.get_secret_value(
            SecretId=self.secret_name
        )
        secret = get_secret_value_response['SecretString']
        parsed_secret = json.loads(secret)
        return parsed_secret["KNOWLEDGE_BASE_ID"]

    def chat_with_bedrock(self, user_input):
        response = self.bedrock_client.retrieve_and_generate(
            input={"text": user_input},
            retrieveAndGenerateConfiguration={
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": self.knowledge_base_id,
                    "modelArn": f"arn:aws:bedrock:{self.region_name}::foundation-model/anthropic.claude-v2"
                },
                "type": "KNOWLEDGE_BASE"
            }
        )

        response_text = response['output']['text']

        if not response['citations'][0]['retrievedReferences']:
            display_text = response_text
        else:
            s3_uri = response['citations'][0]['retrievedReferences'][0]['location']['s3Location']['uri']
            display_text = f"{response_text}\nReference: {s3_uri}"

        return display_text

# Example usage:

