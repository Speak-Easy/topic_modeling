1.) If you do not have virtualenv installed, run the following command: 
    pip install virtualenv
2.) Create a new virtualenv:
    virtualenv venv
3.) Activate the virtualenv:
    source venv/bin/activate
4.) The first time you activate your new virtualenv, perform the following command to install all of the necessary dependencies:
    pip install -r requirements.txt

When done, decative the virtualenv:
    deactivate


### Integrating the utilties as a subtree
1.) git remote add utils https://github.com/Reviewify/utilities.git
2.) git fetch utils
3.) git checkout -b utils_branch utils/master
4.) git checkout master
5.) git read-tree --prefix=utils/ -u utils_branch

### Updating the utils_branch
1.) git checkout utils_branch
2.) git pull
3.) git checkout master
4.) git merge --squash -s subtree --no-commit rack_branch
