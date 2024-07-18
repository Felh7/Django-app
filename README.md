# Ansible playbook for deploying web app with Django, nginx and postgresql 
### This playbook is created to automate the deployment of a typical applications server based on ubuntu 22.04 
#### The project itself is in the Python branch
Ansible installation guide: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html \
After completing the installation head to your hosts file that is usually located in ```/etc/ansible/```  directory and add your hosts. 
You can change variables in playbook files for yourself __(changing DB password variable is crucial for your app's security!)__. 
Go to nginx_conf file and change ```server name``` to yours. Don't forget to change the ```root path``` if you've changed the path variable in the playbook file.

To run the playbook type the following command from playbook.yml file's directory: \
```$ ansible-playbook playbook.yml -K [host's sudo password]```
