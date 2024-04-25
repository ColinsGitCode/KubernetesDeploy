import argparse
from utils_tools import CmdExecutor
from prerequisites_install import PrerequisitesInstall
from prerequisites_uninstall import PrerequisitesUninstall
from minikube_install import InstallMinikube
from minikube_uninstall import UninstallMinikube
from minikube_start import StartMinikube
from monitoring_install import InstallMonitoring
from monitoring_uninstall import UninstallMonitoring
from ansible_install import AnsibleInstall
from ansible_uninstall import AnsibleUninstall


class CommandArgsParser:
    @staticmethod
    def main_process():
        parser = argparse.ArgumentParser(description="The K8S Cluster Deployment Command Line Tools")
        parser.add_argument("--nginx_proxy",
                            help="The Nginx Proxy Operation: start/stop")
        parser.add_argument("--monitoring",
                            help="The kubernetes Cluster Monitoring System Operations: install/uninstall")
        parser.add_argument("--minikube",
                            help="The kubernetes Cluster Minikube Operations: install/uninstall/start/stop")
        parser.add_argument("--cluster",
                            help="The kubernetes Cluster Deployments Operations: install/uninstall")
        parser.add_argument("--ansible",
                            help="The Ansible Deployments for Kubernetes Cluster: install/uninstall")
        parser.add_argument("--tmux",
                            help="The TMUX Deployments By Using Ansible: install/uninstall")

        args = parser.parse_args()

        if args.nginx_proxy:
            if args.nginx_proxy == "start":
                InstallMonitoring.nginx_process()
            elif args.nginx_proxy == "stop":
                UninstallMonitoring.nginx_uninstall()
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --nginx_proxy start/stop !")
        elif args.ansible:
            if args.ansible == "install":
                AnsibleInstall.process()
            elif args.ansible == "uninstall":
                AnsibleUninstall.process()
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --ansible install/uninstall !")
        elif args.tmux:
            if args.tmux == "install":
                AnsibleInstall.ansible_deploy_tmux()
            elif args.tmux == "uninstall":
                AnsibleUninstall.ansible_undeploy_tmux()
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --tmux install/uninstall !")
        elif args.monitoring:
            if args.monitoring == "install":
                InstallMonitoring.process()
            elif args.monitoring == "uninstall":
                UninstallMonitoring.process()
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --monitoring install/uninstall !")
        elif args.minikube:
            if args.minikube == "install":
                InstallMinikube.process()
                InstallMonitoring.process()
            elif args.minikube == "uninstall":
                UninstallMonitoring.process()
                UninstallMinikube.process()
            elif args.minikube == "start":
                StartMinikube.process()
            elif args.minikube == "stop":
                CmdExecutor.exec_cmd("minikube stop")
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --minikube install/uninstall/start/stop !")
        elif args.cluster:
            if args.cluster == "install":
                PrerequisitesInstall.process()
                InstallMinikube.process()
                InstallMonitoring.process()
            elif args.cluster == "uninstall":
                UninstallMonitoring.process()
                UninstallMinikube.process()
                PrerequisitesUninstall.process()
            else:
                print("Incorrect arguments! \n"
                      "Please try: python3 main.py --cluster install/uninstall !")
        else:
            print("Incorrect arguments! \n"
                  "Please try : python3 main.py --nginx_proxy/monitoring/minikube/cluster !")


if __name__ == '__main__':
    CommandArgsParser.main_process()
