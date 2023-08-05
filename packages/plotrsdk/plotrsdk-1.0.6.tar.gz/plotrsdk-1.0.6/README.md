This is a SDK for the Lord of the Rings API at https://the-one-api.dev

# Installation & Setup
You can install this package using pip 
```
pip install plotrsdk
```

## Account Creation
Signup at https://the-one-api.dev/sign-up and copy your Access token

## Setup Environment Variable
Since, most of the APIs are protected using a access token, you will have to set an enviornment variable before using the SDK

```
export LOTR_TOKEN=xxxxxxxxx
```

# Usage

## Important things to remember
list function has a default limit of 10. If you want a bigger limit, you can do the following
```
.limit({"limit": 1000})
```

## Books
To list the books 

Intialize with API key

Services
-   Book
-   Movie
-   Character
-   Quote
-   Chapter

each method in service will have a variable which states whether key is required or not

Addon to each service
- Pagination
- Sorting
- Filter
  - pretty much straight forward, use dictionary, and use that to 
- Authentication