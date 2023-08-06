from argparse import ArgumentParser

from quick_client import ApiException
from quick_client import ApplicationCreationData

from quick.commands.base import ArgumentGroup
from quick.commands.base import Group
from quick.commands.base import ManagerCommand
from quick.parser import ArgsAction


class DeployStreamsApp(ManagerCommand):
    name = "deploy"
    help = "Deploy a new application"
    description = (
        "Deploy a new application. "
        "\n"
        "The application must be provided as a Docker image. "
        "You can specify the registry."
        "You can also deploy the application from a private registry. If you want to do this, you must specify the "
        "corresponding image pull secret."
    )

    def client_error_message(self, exception: ApiException) -> str:
        return f"Could not create application: {exception.body}"

    def execute(self):
        arguments = {} if self.args.props is None else self.args.props

        app_creation_data = ApplicationCreationData(
            name=self.args.application_name,
            registry=self.args.registry,
            image_name=self.args.image,
            tag=self.args.tag,
            image_pull_secret=self.args.image_pull_secret,
            replicas=self.args.replicas,
            port=self.args.port,
            arguments=arguments,
        )

        self.client.deploy_application(application_creation_data=app_creation_data)

        print(f"Deployed application {self.args.application_name}")

    def add_args(self, parser: ArgumentParser, required: ArgumentGroup, optional: ArgumentGroup):
        required.add_argument(
            "application_name", metavar="NAME", type=str, help="Name of the application (must be unique)"
        )
        required.add_argument(
            "--registry",
            metavar="REGISTRY_URL",
            type=str,
            help="URL to container registry",
            required=True,
        )
        required.add_argument("--image", metavar="IMAGE", type=str, help="Name of the image", required=True)
        required.add_argument(
            "--tag",
            metavar="TAG",
            type=str,
            help="Docker image tag",
            required=True,
        )
        optional.add_argument(
            "--image-pull-secret",
            metavar="IMAGE_PULL_SECRET",
            type=str,
            help="The name of the image pull secret (in a string format) for pulling an image from a private registry",
        )
        optional.add_argument(
            "--replicas",
            metavar="REPLICAS",
            type=int,
            help="Number of replicas",
            default=1,
        )
        optional.add_argument(
            "--args",
            dest="props",
            metavar="ARG=VALUE",
            action=ArgsAction,
            nargs="*",
            help="CLI arguments of the application (broker and schema registry not required)",
        )
        optional.add_argument(
            "--port",
            metavar="PORT",
            type=int,
            help="The container port of the application",
        )


class DeleteStreamsApp(ManagerCommand):
    name = "delete"
    help = "Delete an application"
    description = "Delete an application. This stops the running Streams application and removes all its state."

    def client_error_message(self, exception: ApiException) -> str:
        return f"Could not delete application {self.args.application_name}"

    def add_args(self, parser: ArgumentParser, required: ArgumentGroup, optional: ArgumentGroup):
        required.add_argument("application_name", metavar="NAME", type=str, help="Name of the application")

    def execute(self):
        self.client.delete_application(name=self.args.application_name)
        print(f"Deleted application {self.args.application_name}")


class StreamsAppGroup(Group):
    name = "app"
    help = "Manage streams applications"
    description = (
        "Streams applications are Kafka Streams applications processing your data stream. "
        "You can deploy them to the quick cluster."
    )
    sub_parser = [
        DeployStreamsApp,
        DeleteStreamsApp,
    ]
