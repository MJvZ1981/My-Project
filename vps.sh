# Let's you enter your vps on the vps command
function vps() {
    local ssh_user='root'               # Replace with your SSH username
    local ssh_host='164.90.194.212'     # Replace with your VPS IP address or hostname

    cd ~ && ssh ${ssh_user}@${ssh_host}
}
