Components I used to get the continuous deployment done are:

## Setting up the droplet:
When set up, I made sure I could log into my VPS by SSH. In order to do so I created a SSH-key and used the "ssh-copy-id -i ~/.ssh/mykey root@ip_adress" command. When logging into the droplet (using the ssh root@ip_adress command) I accpted the fingerprint, entered the password and from then on was able to enter my vps simply by typing vps (since I created a shellsript for this and added this to my ~/.bashrc file using source vps.sh). I also noticed these setting can be changed by manually entering the sshd_config file and/or adding your ssh-key to the authorized_keys (cat /path/to/file >> ~/.ssh/authorized_keys)

## Cloning my github repo:
I also gave the ~/.ssh directory the right permissions and the authorized_keys file (chmod 700 ~/.ssh/ and chmod 600 ~/.ssh/authorized_keys), added github to the known_hosts and set up the secrets. I added my public key to my github settings (added the SSH_key) and from then on was able to push files from my local machine into the repo.

## My struggle:
I didn't use the one I had on my local machine, but after I did everything worked like supposed to. My script from the deploy.yml initiated after a push. And after a git push command from my local machine it triggered the jobs. And finally the appleboy/ssh-action@master command in the deploy.yml pulled through and my vps allowed the git pull command from the right directory (the one I initially cloned).

## My service file:

```
[Unit]
# This could be anything that helps you and colleagues know what this service is for.
Description=app gunicorn daemon
# This tells systemd when this application is ready to start```
After=network.target

[Service]
Type=notify
DynamicUser=yes
RuntimeDirectory=app
# Where the command supplied in ExecStart be run
WorkingDirectory=/github/My_Project/
ExecStart=/usr/bin/gunicorn main:app
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

## Bash:

> I used the touch command a lot to create a file to see if everything worked properly. Like: `touch push.txt` followed by `echo "push it" >> push.txt` and my auto 
> push command, since I created a shell script with a function for auto pushes:

```
function auto() {
  if [ -z "$1" ]; then
    echo "Please provide a commit message"
    return 1
  fi

  # Add all changes
  git add .

  # Commit changes with message provided as argument
  git commit -m "$1"

  # Pull changes from remote repository
  git pull

  # Push changes to remote repository
  git push
}
```

> also giving an error if no argument is given.

> This, to me, was one of the fun parts (finding out about these shell scripts). 
> I also created scripts to get me in the right directory at once:

```
function hi() {
  cd /path/to/directory
}
```
