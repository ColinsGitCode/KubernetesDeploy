# Kubernetes Cluster in Local Ubuntu Environment

## 1. Overview
- Local Ubuntu Environment k8scluster Deployment Scripts.
 
### 1.1 Kubernetes Cluster URLs
1. Kubernetes Cluster Dashboard
   - http://192.168.100.81:31000/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/node?namespace=monitoring
2. Kubernetes Cluster Monitoring System
   - Grafana URLs
     - http://192.168.100.81:30333/login
   - Prometheus URLs
     - http://192.168.100.81:30334/graph?g0.expr=&g0.tab=1&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h
   - AlertManager URLs
     - http://192.168.100.81:30335/#/alerts

## 2. Usage
~~~
# cd into the local repository directory after git clone
cd local_repo_dir

# python3 main.py -h
usage: main.py [-h] [--nginx_proxy NGINX_PROXY] [--monitoring MONITORING] [--minikube MINIKUBE] [--cluster CLUSTER] [--ansible ANSIBLE]

The K8S Cluster Deployment Command Line Tools

options:
  -h, --help            show this help message and exit
  --nginx_proxy NGINX_PROXY
                        The Nginx Proxy Operation: start/stop
  --monitoring MONITORING
                        The kubernetes Cluster Monitoring System Operations: install/uninstall
  --minikube MINIKUBE   The kubernetes Cluster Minikube Operations: install/uninstall/start/stop
  --cluster CLUSTER     The kubernetes Cluster Deployments Operations: install/uninstall
  --ansible ANSIBLE     The Ansible Deployments for Kubernetes Cluster: install/uninstall
~~~

## 3. Functions:
### 3.1 Installation Process
   1. Install Prerequisites.(`yq, kubectl, skopeo, helm, docker and kind`)
   2. Install Kubernetes Cluster (by using `minikube` in local environment).
   3. Install the Monitoring System (`Prometheus and Grafana`) of the Kubernetes Cluster.

### 3.2 Uninstallation Process
   1. Uninstall Prerequisites.(`yq, kubectl, skopeo, helm, docker and kind`)
   2. Uninstall Kubernetes Cluster (by using `minikube` in local environment).
   3. Uninstall the Monitoring System (`Prometheus and Grafana`) of the Kubernetes Cluster.
   

## 4. Scripts brief Introduction
1. `prerequisites_install.py`
    - Scripts for **install** Kubernetes cluster prerequisites, such as `yq`, `kubectl`, `skopeo`, `helm`, `docker` and `kind`.

2. `prerequisites_uninstall.py`
    - Scripts for **uninstall** Kubernetes cluster prerequisites, such as `yq`, `kubectl`, `skopeo`, `helm`, `docker` and `kind`.

3. `minikube_install.py`
    - Using the **minikube** as the default kubernetes in local ubuntu environment. Installing the minikube kubernetes service, and config cluster dashboard.

4. `minikube_uninstall.py`
    - Uninstallation for **minikube** kubernetes service
     
5. `minikube_start.py`
    - Starting the **minikube** kubernetes service

6. `monitoring_install.py`
    - Installing the `kube-prometheus`, which includes `prometheus`, `grafana`, and `alertmanager`, as the monitoring system of the kubernetes cluster
   
7. `monitoring_uninstall.py`
    - Uninstalling the `kube-prometheus`, which is the monitoring system of the kubernetes cluster.

8. `ansible_install.py`
   - Installing the `Ansible`, which is the automation tools for further kubernetes cluster deployments.
    
9. `ansible_install.py`
   - Uninstalling the `Ansible`. 
     
10. `utils_tools.py`
    - Python functions for execute linux commands, and templates the configuration files from jinja2 files
     
11. `constants.py`
    -  Constants values definition, such as file path and so on.
