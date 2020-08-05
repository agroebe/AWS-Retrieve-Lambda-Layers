import boto3

layer_names = [ 'requests_dependency' ]

client = boto3.client('lambda', region_name='us-east-1')

output = ''

for layer_name in layer_names:
    response = client.list_layer_versions(LayerName=layer_name)

    layer_versions = response['LayerVersions']

    # Latest version should be the haed of the list, so grab that.
    latest = layer_versions[0]
    latest_arn = latest['LayerVersionArn']

    output += '-var requests_dependency_arn=' + latest_arn + ' '

print(output)
