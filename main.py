from utils_tools import UtilsJinja2
from prerequisites_install import PrerequisitesInstall
from prerequisites_uninstall import PrerequisitesUninstall
from minikube_install import InstallMinikube
from minikube_uninstall import UninstallMinikube
from monitoring_install import InstallMonitoring
from monitoring_uninstall import UninstallMonitoring

class K8SClusterDeployment:
    @staticmethod
    def install_k8scluster() -> None:
        PrerequisitesInstall.process()
        InstallMinikube.process()
        InstallMonitoring.process()

    @staticmethod
    def uninstall_k8scluster() -> None:
        UninstallMonitoring.process()
        UninstallMinikube.process()
        PrerequisitesUninstall.process()


if __name__ == '__main__':
    K8SClusterDeployment.install_k8scluster()
    #
    # K8SClusterDeployment.uninstall_k8scluster()
