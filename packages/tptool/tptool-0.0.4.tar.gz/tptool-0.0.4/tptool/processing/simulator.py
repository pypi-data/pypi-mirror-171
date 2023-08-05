import multiprocessing
from time import time, sleep

import numpy as np

from tptool.config.configs import SysConfig
from tptool.common.logger import Logger as Log


TAG = "Simulator"


class SimulatorProcess(multiprocessing.Process):
    """
    Simulates signals and converts them as raw data to feed the processes.
    """
    def __init__(self, parser_process):
        """
        Initialises values for process.
        :param parser_process: Reference to a ParserProcess instance.
        :type parser_process: ParserProcess.
        """
        multiprocessing.Process.__init__(self)
        self._exit = multiprocessing.Event()
        self._period = None
        self._parser = parser_process
        Log.i(TAG, "Process Ready")

    def open(self, port=None, speed=SysConfig.simulator_default_speed, timeout=0.5):
        """
        Opens a specified serial port.
        :param port: Not used.
        :type port: str.
        :param speed: Period of the generated signal.
        :type speed: float.
        :param timeout: Not used.
        :type timeout: float.
        :return: True if the port is available.
        :rtype: bool.
        """
        self._period = float(speed)
        Log.i(TAG, "Using sample rate at {}".format(self._period))
        return True

    def run(self):
        """
        Simulates raw data incoming as CSV.
        :return:
        """
        Log.i(TAG, "Process starting...")
        timestamp = time()
        coef = 2 * np.pi
        while not self._exit.is_set():
            stamp = time() - timestamp
            #vl, 6112, 8, 28244, 28244, 27539
            for i in range(1,SysConfig.plot_max_channels+1):
                self._parser.put([stamp, str(("vl,{},{},{},{},{}\n".format(stamp, i, np.cos(coef * stamp)+1, np.cos(coef * stamp)+i+1, np.cos(coef * stamp)+i+2)))
                                .encode(SysConfig.app_encoding)])
            sleep(self._period)
        Log.i(TAG, "Process finished")

    def stop(self):
        """
        Signals the process to stop acquiring data.
        :return:
        """
        Log.i(TAG, "Process finishing...")
        self._exit.set()

    @staticmethod
    def get_ports():
        """
        Gets a list of the available ports.
        :return: List of available ports.
        :rtype: str list.
        """
        return ["Sine Simulator"]

    @staticmethod
    def get_speeds():
        """
        Gets a list of the speeds.
        :return: List of the speeds.
        :rtype: str list.
        """
        return [str(v) for v in [0.002, 0.004, 0.005, 0.010, 0.020, 0.050, 0.100, 0.250]]
