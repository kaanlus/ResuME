import boto3
import json
import time


# Create boto3 clients
personalize_runtime = boto3.client('personalize-runtime', verify=False)
personalize = boto3.client('personalize', verify=False)

# Get Personalize Recipes
response = personalize.list_recipes()

for recipe in response['recipes']:
    print(recipe)

# Set necessary ARN's & other variables
datasetGroup= ''
dataset = ''
schemaInit = ''
campaign = ''
solution = ''
role = ''
dataSource = ''
recipe = ''

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

# Cleanups to remove old active resources that may interfere





# Create new schema





# Create Dataset Group





# Create dataset in dataset group





# Import data with a dataset import job





# Create a solution





# Create a solution version





# Create a campaign from solution





# Get recommendations from campaign




