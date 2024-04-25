from utils_tools import CmdExecutor
from utils_tools import AptGetUtils
from constants import AnsibleConst


class AnsibleUninstall:
    @staticmethod
    def ansible_undeploy_tmux():
        # Execute: ansible-playbook -v -i /root/AnsibleProject/ansible_inventory /root/KubernetesDeploy/AnsiblePlaybooks/playbooks/tmux/install.yaml
        ansible_playbook_cmd = "ansible-playbook -v -i " + AnsibleConst.ANSIBLE_INVENTORY_FILE + " " + AnsibleConst.TMUX_PLAYBOOK_PATH + "/uninstall.yaml"
        CmdExecutor.exec_cmd(ansible_playbook_cmd)
    @staticmethod
    def process():
        """
        1. apt-get remove ansible
        2. rm -rf ansible*

        :return:
        """

        AptGetUtils.uninstall(["ansible", "ansible-core"])

        rm_cmd_list = [
            "rm -rf " + AnsibleConst.ANSIBLE_PROJECT,
            "rm -rf /usr/local/bin/ansible",
            "rm -rf /usr/local/bin/ansible-config",
            "rm -rf /usr/local/bin/ansible-playbook",
            ]
        for rm_cmd in rm_cmd_list:
            CmdExecutor.exec_cmd(rm_cmd)


if __name__ == '__main__':
    AnsibleUninstall.process()