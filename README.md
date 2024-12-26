# TodoApp
Architecture Overview

![Screenshot 2024-12-26 at 2 46 01 PM](https://github.com/user-attachments/assets/63d62ddf-08b7-4c42-9a34-40acac47db7f)

Prerequisite:

  Create AWS account

Steps

1. Create Dynamo db table-
   For storing the ToDo tasks, a DynamoDB table named ToDoTable was created, which has id (S) as the partition key. The partition key (also known as the hash key) is a fundamental part of the table's primary key. Below are the steps listed in the screenshot:
   <img width="1470" alt="Screenshot 2024-12-26 at 2 48 50 PM" src="https://github.com/user-attachments/assets/024e07b6-eb72-4fb1-8438-ad631144d34b" />
   here click on create table
     
  <img width="1470" alt="Screenshot 2024-12-26 at 2 49 38 PM" src="https://github.com/user-attachments/assets/56e89e5e-1e5f-4672-913d-b5ccc5a00be0" />

  <img width="1470" alt="Screenshot 2024-12-26 at 2 49 45 PM" src="https://github.com/user-attachments/assets/918f5e3d-b9e7-46ac-9182-98258701c127" />

2. create lambda function-
  ![Screenshot 2024-12-26 at 2 54 58 PM (2)](https://github.com/user-attachments/assets/24b86ae6-5a64-44f3-aa39-884285424723)

  <img width="1470" alt="Screenshot 2024-12-26 at 2 54 58 PM" src="https://github.com/user-attachments/assets/b219fdd3-e0d2-4c30-9331-ec9d8a8b350a" />
here click on create function

  <img width="1470" alt="Screenshot 2024-12-26 at 2 55 25 PM" src="https://github.com/user-attachments/assets/207e3d16-a3f1-438a-ab2e-4ff324360a7c" />

After this, the POST method is added to handle the creation of new ToDo tasks. 

<img width="1462" alt="Screenshot 2024-12-26 at 3 00 28 PM" src="https://github.com/user-attachments/assets/f6b52703-4219-4169-9555-f3fb3da8defb" />

select REST API-
![Screenshot 2024-12-26 at 1 18 29 AM (2)](https://github.com/user-attachments/assets/ad52f177-577e-4d5c-b156-8cc4ca63266a)


<img width="1470" alt="Screenshot 2024-12-26 at 3 03 11 PM" src="https://github.com/user-attachments/assets/886a584f-b9da-4b4f-850d-6bb46aa1150a" />

After this go to Resources -> Create method

<img width="1470" alt="Screenshot 2024-12-26 at 3 05 00 PM" src="https://github.com/user-attachments/assets/0db0534e-2cbc-42eb-890f-5ef9cc7fa515" />
select Lambda proxy integration because Lambda Proxy Integration is a feature in Amazon API Gateway that allows you to directly invoke an AWS Lambda function from an API endpoint while passing all parts of the HTTP request to the Lambda function. The Lambda function, in turn, processes the request and returns a response in a specific format that API Gateway can use to return the appropriate HTTP response to the client.

after creation of api resource test the api
<img width="1130" alt="Screenshot 2024-12-26 at 3 07 02 PM" src="https://github.com/user-attachments/assets/8f179838-528b-445f-93de-e1faca4c048e" />
<img width="1470" alt="Screenshot 2024-12-26 at 3 07 31 PM" src="https://github.com/user-attachments/assets/c402f07a-cadc-4d07-9cd6-9c4cc3da7ec1" />
After that as we can see item got added in dynamodb table
<img width="847" alt="Screenshot 2024-12-26 at 3 08 20 PM" src="https://github.com/user-attachments/assets/386b9192-c771-4ac2-b703-1c3f51f440ac" />


