# AWS-Retrieve-Lambda-Layers

A really simple Python utility script used to grab AWS Lambda Layer information (specifically, latest version ARNs for each Layer).

# Why?

I needed this script to handle some annoyances with AWS Lambda Layer versioning for me. After adding a new version to a Layer, AWS will not update all existing Lambda functions that use that layer to point to the latest version. This results in some really annoying conflicts when trying to update layers without "un-provisioning" existing resources. 

