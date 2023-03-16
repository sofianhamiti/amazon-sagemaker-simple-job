import sagemaker
from sagemaker.estimator import Estimator

if __name__ == "__main__":
    # PARAMETERS
    container_uri = (
        "366243680492.dkr.ecr.eu-west-1.amazonaws.com/custom-training:latest"
    )
    instance_type = "ml.g5.2xlarge"

    # GET IAM ROLE FROM ENVIRONMENT
    iam_role = sagemaker.get_execution_role()

    # SETUP JOB
    estimator = Estimator(
        image_uri=container_uri,
        role=iam_role,
        instance_count=1,
        instance_type=instance_type,
        # if needed, you can pass parameters as environment variables
        environment={"test": "value"},
    )

    # RUN JOB
    estimator.fit()
