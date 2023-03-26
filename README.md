# Git Cloud Large File Storage

Git LFS for large files that need cloud storage.

## Setup

### AWS S3

1. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. Create an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and 
[AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html#gs-get-keys).
3. Put the access keys in `~/.aws/credentials` as described [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). 
Note, the profile used by gclfs is `gclfs`. This can be overridden in `gclfs.config`. See example below.
4. Add bucket name to `gclfs.config`.

Example credentials file:

```ini
# ~/.aws/credentials
[default]
aws_access_key_id=AKIAASSFODNN7EXAMPLE
aws_secret_access_key=wJalrP0dnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[gclfs]
aws_access_key_id=BTIAIOSFODNN7EXAMPLE
aws_secret_access_key=xyalrXUghdEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

Example config file with overridden profile name:
```ini
# gclfs.config
[s3]
bucket=my-awesome-bucket
profile=default
```

## Usage

### Tracking

To track files with a specific extension that will be uploaded to cloud storage, run `gcl track *.<file_extension>`

For example, to track wav files:

`gcl track "*.wav"`

This adds the extension to `.gitattributes`. When pushing to remote repo, this will sync all wav files to S3.

**Important**: To keep the large files from getting committed to the git repo, you still have to add them to 
`.gitignore`.

### Commands

Your normal git commands work here and a remote git repo should be setup as usual 
(with `git init` and `git remote add`, etc.).

## Example

`gcl init` (initialize repo)

`gcl track "*.wav"` (track wav files)

`gcl add .` (add files to commit)

`gcl status` (get repo status)

`gcl commit -m "init commit"` (commit changes)

`gcl remote add origin git@github.com:me/my-awesome-project` (add remote repo)

`gcl push` (push git repo and sync files with cloud)

`gcl fetch` (fetch changes)

`gcl pull` (pull remote changes and sync files with cloud)

## Limitations

Currently, only AWS S3 is supported.

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
