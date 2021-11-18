# Userlist SDK for Python

The official Python client library to manipulate [Userlist](https://userlist.com/) from your Python application.

Documentation is identical with the API documentation. The same parameters and filters are available.
And the same response structure. You can have a look at [Docs](https://userlist.com/docs/getting-started/integration-guide/#setting-up-the-integration).

## Authentication

The Authentication is done via the `push_key` variable.

Check your Push key at [Userlist Settings](https://app.userlist.com/settings/push).

## Installation
```pip install userlist```

## Quick Start
Import installed package.

`````from userlist_python import UserlistApiClient`````

Init the instance with an API key given after registration.

````userlist_client = UserlistApiClient('YOUR_API_KEY')````

## Endpoints
An instance of `UserlistApiClient` has all main methods that correspond to endpoints available for UserList API.

### Tracking user data (/users)
User data can be tracked by sending POST requests to `https://push.userlist.com/users`.
The only required parameter is identifier which is a unique identifier for that user within your application.
This can either be the user’s primary key in your database, a generated tracking identifier or their email address
(we don’t recommend using email address though, because it’s less reliable). Whatever you choose, make please keep
in mind that it’ll be the way Userlist identifies this user moving forward.

```
response = userlist_client.push_users(
    identifier="user_test",
    email='test@example.net',
    properties={"first_name": "Test2","last_name": "Testing2"}
)
```

### Deleting users (/users/{{identifier}})
You can remove user data by sending a DELETE request to `https://push.userlist.com/users/{{identifier}}`.
The identifier is the same one you sent when sending the user data initially. We’ll process your deletion request within
a few of moments and remove the user, all their events, as well as all their messages. All campaigns will immediately
be stopped. If you send any data or event with this property after requesting a deletion, we’ll treat it as fresh and
create a new user.

```
response = userlist_client.delete_users(
    'user_test'
)

 ```

### Tracking company data (/companies)
Company data can be tracked by sending POST requests to `https://push.userlist.com/companies`.
The only required parameter is identifier which is a unique identifier for that company within your application.
This can either be the company's primary key in your database, or some kind of generated tracking identifier.
Whatever you choose, make please keep in mind that it’ll be the way Userlist identifies this company moving forward.
```
response = userlist_client.push_companies(
    identifier="company_test",
    name='Example, Inc.',
    properties={
    "industry": "Testing",
    "billing_plan": "enterprise"
  },
    relationships=[
    {
      "user": "user_test",
      "properties": {
        "role": "owner"
      }
    }
  ]
)
 ```

### Deleting Companies (/companies/{{identifier}})
You can remove company data by sending a DELETE request to `https://push.userlist.com/companies/{{identifier}}`.
The identifier is the same one you sent when sending the company data initially. We’ll process your deletion request
within a few of moments and remove the company, all its events, as well as all relationships to users. The users that
where part of that company are not deleted automatically. If you send any data or event with this company after
requesting a deletion, we’ll treat it as fresh and create a new company record.

```
response = userlist_client.delete_companies(
    'company_test'
)
 ```

### Tracking relationships (/relationships)
Userlist allows you to track relationships between users and companies. It's possible to track many-to-many
relationships between users and companies. Creating a relationship needs at least two pieces of information:
a user and a company.
```
response = userlist_client.push_relationships(
    user="user_test",
    company='company_test',
    properties={
    "role": "admin"
  }
)
 ```

### Deleting relationships (/relationships/{{user-identifier}}/{{company-identifier}})
You can remove a relationship data by sending a DELETE request to
`https://push.userlist.com/relationships/{{user-identifier}}/{{company-identifier}}`. We’ll process your deletion
request within a few of moments and remove the relationship between this user and this company. Both the associated user
and company are not deleted automatically.
```
response = userlist_client.delete_relationships(
    'user_test',
    'company_test'
)
 ```

### Tracking events (/events)
Similar to tracking user or company data, tracking events works by sending POST requests to `https://push.userlist.com/events`.
Tracking an event requires at least two pieces of information: a name, and a user or company identifier.
Other parameters are optional.
```
response = userlist_client.push_events(
    name="product_purchased",
    company='company_test',
    properties={
    "product": "Flowers",
    "price": "$12.99"
  }
)
 ```

## Feedback

Feel free to contact us if you have spot a bug or have any suggestion at benedikt`[at]`benediktdeicke.com
