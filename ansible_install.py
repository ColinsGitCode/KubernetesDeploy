from utils_tools import CmdExecutor
from utils_tools import UtilsJinja2
from constants import AnsibleConst


class AnsibleInstall:
    @staticmethod
    def ansible_deploy_tmux():
        # Execute: ansible-playbook -v -i /root/AnsibleProject/ansible_inventory /root/KubernetesDeploy/AnsiblePlaybooks/playbooks/tmux/install.yaml
        ansible_playbook_cmd = "ansible-playbook -v -i " + AnsibleConst.ANSIBLE_INVENTORY_FILE + " " + AnsibleConst.TMUX_PLAYBOOK_PATH + "/install.yaml"
        CmdExecutor.exec_cmd(ansible_playbook_cmd)

    @staticmethod
    def process():
        """
        1. mkdir -r /root/AnsibleProject
        2. apt-get install -y ansible
            2.1 apt-get -y install software-properties-common
            2.2 apt-add-repository ppa:ansible/ansible
            2.3 apt-get update -y
            2.4 apt-get upgrade -y
            2.5 apt-get install -y ansible
        3. ansible-config init --disabled > ansible.cfg
        4. ansible --version
        5. ansible all -m ping -i /root/AnsibleProject/ansible_inventory
        6. ansible-playbook -vvv -i /root/AnsibleProject/ansible_inventory /root/AnsibleProject/ansible_playbook_demo.j2

        :return:
        """
        cmd = "mkdir -p " + AnsibleConst.ANSIBLE_PROJECT
        CmdExecutor.exec_cmd(cmd)

        apt_cmd_list = [
            "apt-get -y install software-properties-common",
            "apt-add-repository -y ppa:ansible/ansible",
            "apt-get update -y",
            "apt-get upgrade -y",
            "apt-get install -y ansible"
        ]
        for apt_cmd in apt_cmd_list:
            CmdExecutor.exec_cmd(apt_cmd)

        cmd = "/usr/bin/ansible --version"
        CmdExecutor.exec_cmd(cmd)

        cmd = "/usr/bin/ansible-config init --disabled > ansible.cfg"
        CmdExecutor.exec_cmd(cmd)

        UtilsJinja2.create_file_from_template(
            AnsibleConst.ANSIBLE_CFG_TEMPLATE,
            {"inventory_path": AnsibleConst.ANSIBLE_INVENTORY_FILE},
            AnsibleConst.ANSIBLE_CFG_FILE
        )

        UtilsJinja2.create_file_from_template(
            AnsibleConst.ANSIBLE_INVENTORY_TEMPLATE,
            {},
            AnsibleConst.ANSIBLE_INVENTORY_FILE
        )

        UtilsJinja2.create_file_from_template(
            AnsibleConst.ANSIBLE_PLAYBOOK_DEMO_YAML_TEMPLATE,
            {},
            AnsibleConst.ANSIBLE_PLAYBOOK_DEMO_YAML
        )

        cmd = "/usr/bin/ansible --version"
        CmdExecutor.exec_cmd(cmd)

        cmd = "/usr/bin/ansible all -m ping -i " + AnsibleConst.ANSIBLE_INVENTORY_FILE
        CmdExecutor.exec_cmd(cmd)

        cmd = "/usr/bin/ansible-playbook -v -i " + AnsibleConst.ANSIBLE_PROJECT + " " + AnsibleConst.ANSIBLE_PLAYBOOK_DEMO_YAML
        CmdExecutor.exec_cmd(cmd)

        ln_cmd_list = [
            "ln -s /usr/bin/ansible /usr/local/bin/ansible",
            "ln -s /usr/bin/ansible-config /usr/local/bin/ansible-config",
            "ln -s /usr/bin/ansible-playbook /usr/local/bin/ansible-playbook",
            "ansible --version",
            "ansible-config --help",
            "ansible-playbook --help"
        ]
        for ln_cmd in ln_cmd_list:
            CmdExecutor.exec_cmd(ln_cmd)


if __name__ == '__main__':
    AnsibleInstall.process()