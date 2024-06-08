"""async-s3."""
import asyncio
from typing import Iterable, Dict, Any

from async_s3.list_objects_async import ListObjectsAsync

import rich_click as click

from async_s3 import __version__

click.rich_click.USE_MARKDOWN = True

s3proto = "s3://"


@click.group()
@click.version_option(version=__version__, prog_name="as3")
def as3():
    """Async S3."""
    pass


@as3.command()
@click.argument("s3_url")
def ls(s3_url) -> None:
    """
    List objects in an S3 bucket.

    Example:
    as3 ls s3://bucket/key
    """
    if not s3_url.startswith(s3proto):
        click.echo("Invalid S3 URL. It should start with s3://")
        raise click.Abort()

    objects = list_objects(s3_url)
    click.echo("\n".join([obj["Key"] for obj in objects]))
    print_summary(objects)


@as3.command()
@click.argument("s3_url")
def du(s3_url) -> None:
    """
    Show count and size for objects in an S3 bucket.

    Example:
    as3 du s3://bucket/key
    """
    if not s3_url.startswith(s3proto):
        click.echo("Invalid S3 URL. It should start with s3://")
        raise click.Abort()

    objects = list_objects(s3_url)
    print_summary(objects)


def human_readable_size(size, decimal_places=2):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def print_summary(objects):
    """Print a summary of the objects."""
    total_size = sum(obj['Size'] for obj in objects)
    click.echo(f"\nTotal objects: {len(list(objects))}, size: {human_readable_size(total_size)}")


def list_objects(s3_url) -> Iterable[Dict[str, Any]]:
    return asyncio.run(list_objects_async(s3_url))


async def list_objects_async(s3_url) -> Iterable[Dict[str, Any]]:
    bucket, key = s3_url[len(s3proto):].split("/", 1)
    s3_list = ListObjectsAsync(bucket)
    return await s3_list.list_objects(key)


if __name__ == "__main__":  # pragma: no cover
    as3()  # pylint: disable=no-value-for-parameter
