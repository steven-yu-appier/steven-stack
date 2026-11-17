"""Upload a Jira attachment or build an ADF document from its response."""

import argparse
import base64
import json
import os
from pathlib import Path
import subprocess


def upload(args):
    base = os.environ['JIRA_DOMAIN'].rstrip('/')
    if '://' not in base:
        base = 'https://' + base
    auth = base64.b64encode(
        (os.environ['JIRA_EMAIL'] + ':' + os.environ['JIRA_API_TOKEN']).encode()
    ).decode()
    filename = str(args.file.resolve()).replace('\\', '\\\\').replace('"', '\\"')
    subprocess.run(
        ['curl', '--config', '-', '--fail-with-body', '--silent', '--show-error',
         '--connect-timeout', '10', '--max-time', '50',
         '--header', 'Accept: application/json',
         '--header', 'X-Atlassian-Token: no-check',
         '--form', 'file=@"' + filename + '"',
         '--output', str(args.output),
         base + '/rest/api/3/issue/' + args.key + '/attachments'],
        input='header = "Authorization: Basic ' + auth + '"\n',
        text=True, check=True,
    )
    print(args.output.read_text())


def adf(args):
    attachments = json.loads(args.response.read_text())
    document = (json.loads(args.body.read_text()) if args.body
                else {'version': 1, 'type': 'doc', 'content': []})
    paragraphs = [
        {'type': 'paragraph', 'content': [
            {'type': 'text', 'text': item['filename'], 'marks': [
                {'type': 'link', 'attrs': {'href': item['content']}}]}]}
        for item in attachments
    ]
    index = len(document['content']) if args.index is None else args.index
    document['content'][index:index] = paragraphs
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    upload_parser = commands.add_parser('upload', help='Upload a file and save the API response')
    upload_parser.add_argument('key')
    upload_parser.add_argument('file', type=Path)
    upload_parser.add_argument('--output', type=Path, required=True)
    upload_parser.set_defaults(run=upload)
    adf_parser = commands.add_parser('adf', help='Build file links, optionally inserting into existing ADF')
    adf_parser.add_argument('response', type=Path)
    adf_parser.add_argument('--body', type=Path, help='Complete existing ADF document')
    adf_parser.add_argument('--index', type=int, help='Top-level insertion index; defaults to append')
    adf_parser.add_argument('--output', type=Path, required=True)
    adf_parser.set_defaults(run=adf)
    args = parser.parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
