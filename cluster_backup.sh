#Usage: "bash cluster_backup"


Folder=$(date | awk '{print$2$3"_Backup"}')

#Update the information, creating a backup folder and ignoring thre rest of the backup folders
Keypath="/home/keenan/.ssh/id_rsa"
Identity=`ssh-add -L | cut -d\  -f3`

#Comparing Identity to has because when ssh-add has not been added at the beginning of session the output of the "Identity" command gives "has"

if [ "$Identity" == "has" ]
then
  ssh-add $Key-path
fi


rsync -arvz -e 'ssh -p 922' --files-from='to_backup.txt' --delete komotok@fe1.cluster.cs.wwu.edu:/cluster/home/komotok /home/keenan/Backups/$Folder


