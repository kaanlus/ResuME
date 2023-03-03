import boto3
import json
import time


# Create boto3 clients
# Verify flag set to false to silence http request cert warnings
personalize_runtime = boto3.client('personalize-runtime', verify=False)
personalize = boto3.client('personalize', verify=False)

# Get Personalize Recipes
response = personalize.list_recipes()
for recipe in response['recipes']:
    print(recipe)

# Create schema
schema = {
    "type": "record",
    "name": "Interactions",
    "namespace": "com.amazonaws.personalize.schema",
    "fields": [
        {
            "name": "USER_ID",
            "type": "string"
        },
        {
            "name": "ITEM_ID",
            "type": "string"
        },
        {
            "name": "TIMESTAMP",
            "type": "long"
        },
        {
            "name": "MAJOR",
            "type": "string"
        },
        {
            "name": "SKILLS",
            "type": "string"
        }
    ],
    "version": "1.0"
}

# Set necessary ARNs & other variables
dataset_group = ''
dataset = ''
schema_arn = ''
campaign = ''
solution = ''
role = ''
data_source = ''
recipe = ''

# Cleanups to remove old active resources that may interfere
if len(personalize.list_datasets(datasetGroupArn=dataset_group, maxResults=50)['datasets']) != 0:
    # Cleanup old dataset
    cleanup_interactions_dataset = personalize.delete_dataset(dataset_arn=dataset)

if len(personalize.list_campaigns(maxResults=50)['campaigns']) != 0:
    # Cleanup old campaigns
    cleanup_campaigns = personalize.delete_campaign(campaign_arn=campaign)

if len(personalize.list_solutions(maxResults=50)['solutions']) != 0:
    # Cleanup old solutions
    cleanup_solutions = personalize.delete_solution(solution_arn=solution)

if len(personalize.list_dataset_groups(maxResults=50)['datasetGroups']) != 0:
    # Cleanup old dataset group
    cleanup_interactions_dataset_group = personalize.delete_dataset_group(dataset_group_arn=dataset_group)

if len(personalize.list_schemas(maxResults=50)['schemas']) != 0:
    # Cleanup old schema
    cleanup_interactions_schema = personalize.delete_schema(schema_arn=schema_arn)

# Create new schema


# Create Dataset Group


# Create dataset in dataset group


# Import data with a dataset import job


# Create a solution


# Create a solution version


# Create a campaign from solution


# Get recommendations from campaign
