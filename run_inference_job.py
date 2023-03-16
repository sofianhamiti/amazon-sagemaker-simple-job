import sagemaker
from sagemaker.estimator import Estimator

if __name__ == "__main__":
    # PARAMETERS
    container_uri = "<ADD ECR IMAGE URI HERE>"
    instance_type = "ml.g5.2xlarge"

    # GET IAM ROLE FROM CURRENT ENVIRONMENT
    iam_role = sagemaker.get_execution_role()

    # SETUP JOB
    estimator = Estimator(
        image_uri=container_uri,
        role=iam_role,
        instance_count=1,
        instance_type=instance_type,
        # if needed, you can use environment variables to pass parameters to container
        environment={"test": "value"},
    )

    # RUN JOB
    estimator.fit()
