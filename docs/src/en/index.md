# ListObjectsAsync

## Overview
ListObjectsAsync is an asynchronous utility for listing objects in an AWS S3 bucket. 
This tool utilizes the aiobotocore library to provide efficient, non-blocking access to your S3 data, supporting 
recursive directory traversal with depth control.

## Features
- Asynchronous Operations: Utilizes asyncio for non-blocking IO operations.
- Paginated Results: Handles S3 pagination internally to provide a efficient traversal of long S3 objects lists.
- Recursive Traversal: Supports recursive listing of objects with controllable depth control.
- Retries: AUtilize AWS retry strategies.

## Usage

```python
--8<-- "list.py"
```
You can control the depth of recursion by specifying the max_depth parameter, by default depth is not limited.

```bash
pipx install async-s3
```

### Implementation Details

[ListObjectsAsync][async_s3]

