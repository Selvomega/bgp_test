"""
The basic type of the router. 
"""

from abc import ABC, abstractmethod
from .basic_types import *

class BaseRouter(ABC):
    """
    The base type of the router. 
    """

    ########## Initialization ##########

    @abstractmethod
    def __init__(self, configuration : RouterConfiguration):
        """
        Initialize the BGP router. 
        """
        self.software_type : RouterSoftwareType = None
        self.router_configuration : RouterConfiguration = configuration

    ########## Turn on/off the instance ##########

    @abstractmethod
    def start_bgp_instance(self):
        """
        Start the BGP instance using `self.router_configuration` 
        """
        raise NotImplementedError("`start_bgp_instance` not implemented!")

    @abstractmethod
    def end_bgp_instance(self):
        """
        Shut down the BGP instance
        """
        raise NotImplementedError("`end_bgp_instance` not implemented!")

    @abstractmethod
    def restart_bgp_instance(self):
        """
        Restart the BGP instance.
        """
        raise NotImplementedError("`restart_bgp_instance` not implemented!")

    ########## Get methods ##########

    def get_software_type(self):
        """
        Get the type of the software
        """
        return self.software_type

    def get_router_configuration(self):
        """
        Get the configuration of the router
        """
        return self.router_configuration

    ########## Log manipulation ##########

    @abstractmethod
    def read_log(self, path: str):
        """
        Read (all) the content from the routing softwares' log.
        Must execute with sudo-command.
        """
        with open(path, 'r') as file:
            content = file.read()
        return content

    @abstractmethod
    def clear_log(self, path: str):
        """
        Clear the content from the routing softwares' log.
        Must execute with sudo-command.
        """
        with open(path, 'w') as file:
            file.write('')
        return

    ########## Crash management ##########

    @classmethod
    @abstractmethod
    def if_crashed(cls) -> bool:
        """
        Return if the router software has crashed.
        """
        raise NotImplementedError()

    @abstractmethod
    def recover_from_crash(self):
        """
        Recover the software from crash.
        """
        raise NotImplementedError()

    ########## Other utils ##########

    @abstractmethod
    def wait_for_log(self, time_duration: float):
        """
        Waiting until the log does not update anymore.
        """
        raise NotImplementedError()
