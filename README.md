# Userlist Python [![Tests](https://github.com/userlist/userlist-python/actions/workflows/test.yml/badge.svg)](https://github.com/userlist/userlist-python/actions/workflows/test.yml)

This library helps with integrating Userlist into Python applications.

## Installation

This library can be installed via pip:

```bash
pip install userlist-python
```

## Configuration

The only required configuration is the Push API key. You can get your Push API key via the [Push API settings](https://app.userlist.com/settings/push) in your Userlist account.

Configuration values can be set when creating a new push client or via environment variables. The environment takes precedence over values provided during the initialization process.

**Configuration via environment variables**

```bash
USERLIST_PUSH_KEY=401e5c498be718c0a38b7da7f1ce5b409c56132a49246c435ee296e07bf2be39
```

**Configuration during initialization**

```python
from userlist import Userlist

userlist = Userlist(push_key='401e5c498be718c0a38b7da7f1ce5b409c56132a49246c435ee296e07bf2be39')
```

## Usage

Before tracking user or event data, create a new push client. If you configured your push key via environment variables there's nothing to add. Otherwise, see the example above.

```python
from userlist import Userlist
userlist = Userlist()
```

### Tracking Users

#### Creating & updating Users

```python
user = {
    'identifier': 'user-1',
    'email': 'user@example.com',
    'properties': {
        'first_name': 'Jane',
        'last_name': 'Doe'
    }
}

userlist.users.push(user)

# Aliases
userlist.user(user)
userlist.users.create(user)
```

#### Deleting Users

```python
userlist.users.delete('user-1')
userlist.users.delete(user)
```

### Tracking Companies

#### Creating & updating Companies

```python
company = {
    'identifier': 'company-1',
    'name': 'Example, Inc.',
    'properties': {
        'industry': 'Software Testing'
    }
}

userlist.companies.push(company)

# Aliases
userlist.company(company)
userlist.companies.create(company)
```

#### Deleting Companies

```python
userlist.companies.delete('company-1')
userlist.companies.delete({'identifier': 'company-1'})
```

### Tracking Relationships

#### Creating & updating Relationships

```python
relationship = {
    'user': 'user-1',
    'company': 'company-1',
    'properties': {
        'role': 'admin'
    }
}

userlist.relationships.push(relationship)

# Aliases
userlist.relationship(relationship)
userlist.relationships.create(relationship)
```

This is equivalent to specifying the relationship on the user model:

```python
user = {
    'identifier': 'user-1',
    'relationships': [{
        'company': 'company-1',
        'properties': {
            'role': 'admin'
        }
    }]
}

userlist.users.push(user)
```

Or specifying the relationship on the company model:

```python
company = {
    'identifier': 'company-1',
    'relationships': [{
        'user': 'user-1',
        'properties': {
            'role': 'admin'
        }
    }]
}

userlist.companies.push(company)
```

#### Deleting Relationships

```python
relationship = {
    'user': 'user-1',
    'company': 'company-1'
}

userlist.relationships.delete(relationship)
```

### Tracking Events

```python
event = {
    'name': 'project_created',
    'user': 'user-1',
    'properties': {
        'name': 'Example Project'
    }
}

userlist.events.push(event)

# Aliases
userlist.event(event)
userlist.events.create(event)
```

### Sending Transactional Messages

```python
message = {
    'user': 'user-1',
    'template': 'welcome-email',
    'properties': {
        'account_name': 'Example, Inc.',
        'billing_plan': 'Pro'
    }
}

userlist.messages.push(message)

# Aliases
userlist.message(message)
userlist.messages.create(message)
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/userlist/userlist-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Userlist project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/userlist/userlist-python/blob/master/CODE_OF_CONDUCT.md).

## What is Userlist?

[![Userlist](https://userlist.com/images/external/userlist-logo-github.svg)](https://userlist.com/)

[Userlist](https://userlist.com/) allows you to onboard and engage your SaaS users with targeted behavior-based campaigns using email or in-app messages.

Userlist was started in 2017 as an alternative to bulky enterprise messaging tools. We believe that running SaaS products should be more enjoyable. Learn more [about us](https://userlist.com/about-us/).
