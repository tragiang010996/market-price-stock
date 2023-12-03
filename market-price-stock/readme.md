- [Introduction](#introduction)
- [Start server](#start-server)
- [API Document](#API-document)


# Introduction

API records market price stock trades, return a confirmation

# Start Server
Step 1
```
docker-compose build
```
Step 2
```
docker-compose up
```
# API Document
### Method: ```GET```

### Request URL
```
http://localhost:8000/api
```
### Arguments

symbol ```REQUIRED```

quantity ```REQUIRED```