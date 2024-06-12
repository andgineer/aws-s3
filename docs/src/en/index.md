# ListObjectsAsync

## Overview
ListObjectsAsync asynchronously requests objects list in an AWS S3 bucket. 

Supports recursive directory traversal with depth control.

Supports sophisticated grouping of prefixes to reduce the number of API calls.

Read detailed explanation in [the blog post](https://sorokin.engineer/posts/en/aws_s3_async_list.html).

## Features
- Utilizes aiobotocore for non-blocking IO operations.
- Groups folders to reduce the number of API calls.
- Handles S3 pagination to provide a efficient traversal of long S3 objects lists.
- Supports recursive listing of objects with controllable depth control.
- Utilize AWS retry strategies.

## Usage

```python
--8<-- "list.py"
```
You can control the depth of recursion by specifying the `max_depth` parameter, 
by default depth is not limited.

`max_folders` parameter allows you to group folders by prefix to reduce the number of API calls.

## Docstrings
[ListObjectsAsync][async_s3]

