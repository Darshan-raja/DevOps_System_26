create a SNS in private subnet

1. create a SNS topic
2. create a subscription for the topic
3. create a lambda function to send a message to the topic
4. create a trigger for the lambda function to be triggered by a SNS topic
   --> use blueprint to create a lambda function and a trigger for the lambda function to be triggered by a SNS topic 
   --> Basic information Info
Blueprint name : schedule a peridoic check any URL
--> Schedule expression (rate(1 minute))
--> add destination
        Source (Asynchronous invocation)
        Condition (on success)
-->Execution role (Create a new role with basic Lambda permissions)

create a SNS in public subnet

1. create a SNS topic