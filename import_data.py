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
    "name": "Users",
    "namespace": "com.amazonaws.personalize.schema",
    "fields": [
        {
            "name": "USER_ID",
            "type": "string"
        },
        {
            "name": "MAJOR",
            "type": "string"
        },
        {
            "name": "YEAR",
            "type": "string"
        }
    ],
    "version": "1.0"
}

# Set necessary ARNs & other variables
dataset_group = ''
dataset_arn = ''
schema_arn = ''
campaign_arn = ''
solution_arn = ''
role_arn = ''
recipe_arn = ''
data_source = ''
s3location = 's3://bucket/file.csv'

# Cleanups to remove old active resources that may interfere
if len(personalize.list_datasets(datasetGroupArn=dataset_group, maxResults=50)['datasets']) != 0:
    # Cleanup old dataset
    cleanup_interactions_dataset = personalize.delete_dataset(dataset_arn=dataset_arn)

if len(personalize.list_campaigns(maxResults=50)['campaigns']) != 0:
    # Cleanup old campaigns
    cleanup_campaigns = personalize.delete_campaign(campaign_arn=campaign_arn)

if len(personalize.list_solutions(maxResults=50)['solutions']) != 0:
    # Cleanup old solutions
    cleanup_solutions = personalize.delete_solution(solution_arn=solution_arn)

if len(personalize.list_dataset_groups(maxResults=50)['datasetGroups']) != 0:
    # Cleanup old dataset group
    cleanup_interactions_dataset_group = personalize.delete_dataset_group(dataset_group_arn=dataset_group)

if len(personalize.list_schemas(maxResults=50)['schemas']) != 0:
    # Cleanup old schema
    cleanup_interactions_schema = personalize.delete_schema(schema_arn=schema_arn)

# Create new schema
create_interactions_schema_response = personalize.create_schema(
    name='sample-schema',
    schema=json.dumps(schema)
)

interactions_schema_arn = create_interactions_schema_response['schemaArn']
print(json.dumps(create_interactions_schema_response, indent=2))

# Create Dataset Group
response = personalize.create_dataset_group(name='sample_dataset_group')
dataset_group_arn = response['datasetGroupArn']

description = personalize.describe_dataset_group(datasetGroupArn=dataset_group_arn)['datasetGroup']

print('Name: ' + description['name'])
print('ARN: ' + description['datasetGroupArn'])
print('Status: ' + description['status'])

# Create dataset in dataset group
# Interactions dataset in this example
response = personalize.create_dataset(
    name='sample_interactions_dataset',
    schemaArn=schema_arn,
    datasetGroupArn=dataset_group_arn,
    datasetType='Interactions'
)

dataset_arn = response['datasetArn']

# Import data with a dataset import job
response = personalize.create_dataset_import_job(
    jobName='Sample_Job',
    datasetArn=dataset_arn,
    dataSource={data_source: s3location},
    roleArn=role_arn,
    importMode='FULL'
)

dataset_interactions_import_job_arn = response['datasetImportJobArn']

description = personalize.describe_dataset_import_job(
    datasetImportJobArn=dataset_interactions_import_job_arn)['datasetImportJob']

print('Name: ' + description['jobName'])
print('ARN: ' + description['datasetImportJobArn'])
print('Status: ' + description['status'])

max_time = time.time() + 3 * 60 * 60  # 3 hours
while time.time() < max_time:
    describe_dataset_import_job_response = personalize.describe_dataset_import_job(
        datasetImportJobArn=dataset_interactions_import_job_arn
    )
    status = describe_dataset_import_job_response["datasetImportJob"]['status']
    print("Interactions Dataset Import Job: {}".format(status))

    if status == "ACTIVE" or status == "CREATE FAILED":
        break

    time.sleep(60)

# Create a solution
create_solution_response = personalize.create_solution(
    name='Sample Solution',
    recipeArn=recipe_arn,
    datasetGroupArn=dataset_group_arn
)
solution_arn = create_solution_response['solutionArn']
print('solution_arn: ', solution_arn)

# Create a solution version
create_solution_version_response = personalize.create_solution_version(
    solutionArn=solution_arn
)

solution_version_arn = create_solution_version_response['solutionVersionArn']
print(json.dumps(create_solution_version_response, indent=2))

max_time = time.time() + 3 * 60 * 60  # 3 hours
while time.time() < max_time:
    describe_solution_version_response = personalize.describe_solution_version(
        solutionVersionArn=solution_version_arn
    )
    status = describe_solution_version_response["solutionVersion"]["status"]
    print("Solution Version: {}".format(status))

    if status == "ACTIVE" or status == "CREATE FAILED":
        break

    time.sleep(60)

# Create a campaign from solution
response = personalize.create_campaign(
    name='Sample Campaign',
    solutionVersionArn=solution_version_arn
)

arn = response['campaignArn']

description = personalize.describe_campaign(campaignArn=arn)['campaign']
print('Name: ' + description['name'])
print('ARN: ' + description['campaignArn'])
print('Status: ' + description['status'])

# Get recommendations from campaign
response = personalize_runtime.get_recommendations(
    campaignArn=campaign_arn,
    userId='123',
    numResults=10
)

print("\nRecommended items:")
for item in response['itemList']:
    print("\n" + item['itemId'])
