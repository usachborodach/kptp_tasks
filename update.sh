#!/bin/bash
cd /home/user/repos/kptp_tasks/ || exit 1

git pull

nano /home/user/repos/kptp_tasks/tasks.yml

git add .

if git commit; then
    echo 'commit done, execute "git push"...'
    git push
    echo '"git push" is done'
else
    echo 'commit aborted, "git push" aborted'
fi

echo 'sleep 1 sec...'
sleep 1