# AWS-Retrieve-Lambda-Layers

A really simple Python utility script used to grab AWS Lambda Layer information (specifically, latest version ARNs for each Layer).

The script uses a defined list of Lambda Layer names and retrieves ARNs that represent their most recent version. A formatted string can than be printed to stdout and retrieved in a Jenkinsfile, Terraform, etc.

This example is tailored to Terraform because that was my use case, but this can probably come in handy elsewhere.

# Why?

I needed this script to handle some annoyances with AWS Lambda Layer versioning for me. After adding a new version to a Layer, AWS will not update all existing Lambda functions that use that layer to point to the latest version. This results in some really annoying conflicts when trying to update layers without "un-provisioning" existing resources. 
