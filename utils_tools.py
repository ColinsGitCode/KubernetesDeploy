import os
from tqdm import tqdm
from time import sleep

from jinja2 import Environment, FileSystemLoader


class UtilsJinja2:
    @staticmethod
    def create_file_from_template(j2_path, data_dict, file_path):
        print("-------------------------------------------------")
        # Create a Jinja2 environment
        env = Environment(loader=FileSystemLoader("."))

        # Load the template
        template = env.get_template(j2_path)

        # Provide data to render the template
        # data = {"name": "John"}
        # Render the template with data
        output = template.render(data_dict)

        # Save the rendered output to a new file
        with open(file_path, "w") as f:
            f.write(output)

        print("Finish template the file: " + file_path)
        print("**************************************************")


class CmdExecutor:
    @staticmethod
    def exec_cmd(cmd: str) -> None:
        print("-------------------------------------------------")
        print("Executing: " + cmd)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("")
        os.system(cmd)
        print("")
        print("Finished: " + cmd)
        print("************************************************")
        print()

    @staticmethod
    def wait_countdown(seconds: int) -> None:
        for _ in tqdm(range(seconds), desc="Waiting Countdown"):
            sleep(1)


class AptGetUtils:
    @staticmethod
    def install(service_list: [str]) -> None:
        """
        apt-get install service1 service2 service3 ....

        :param service_list:
        :return: None
        """
        cmd = "apt-get install -y " + " ".join(service_list)
        CmdExecutor.exec_cmd(cmd)

    @staticmethod
    def uninstall(service_list: [str]) -> None:
        """
        apt-get uninstall
        1. apt-get remove -y service1 service2 service3....
        2. apt-get purge -y service1 service2 service3....
        3. apt-get autoremove -y

        :param service_list:
        :return: None
        """
        cmd_list = [
            "apt-get remove -y " + " ".join(service_list),
            "apt-get purge -y " + " ".join(service_list),
            "apt-get autoremove -y "
        ]
        for cmd in cmd_list:
            CmdExecutor.exec_cmd(cmd)


if __name__ == "__main__":
    AptGetUtils.install(["nginx"])
    # time.sleep(20)
    # AptGetUtils.uninstall(["nginx", "nginx-common"])