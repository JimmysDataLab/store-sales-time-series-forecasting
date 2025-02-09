### Export the CloudFormation Template
```bash
aws cloudformation get-template --stack-name databricks-workspace-stack-21da1 --query 'TemplateBody' --output text > /config/aws/databricks_cluster_template.yaml
```

### Document Stack Parameters
```bash
aws cloudformation describe-stacks --stack-name databricks-workspace-stack-21da1 --query 'Stacks[0].Parameters' --output text > /config/aws/databricks_cluster_parameters.yaml
```

### Delete Stack
```bash
aws cloudformation delete-stack --stack-name databricks-workspace-stack-21da1
```

## Re-create the Stack Using the Template
```bash
aws cloudformation create-stack --stack-name databricks-workspace-stack-21da1 \
    --template-body file://Users/akhil/Projects/Kaggle/store-sales-time-series-forecasting/config/aws/databricks_cluster_template.yaml \
    --parameters ParameterKey=AccountId,ParameterValue=4549a9f0-3686-444d-9030-2cc064f4e558 ParameterKey=WorkspaceName,ParameterValue=JimmysDataLab ParameterKey=SessionToken,ParameterValue=****\
    --capabilities CAPABILITY_NAMED_IAM
```