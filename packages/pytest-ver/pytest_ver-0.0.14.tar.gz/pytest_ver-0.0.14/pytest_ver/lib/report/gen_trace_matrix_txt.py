import os

from .gen_base_txt import GenBaseTxt
from .gen_trace_matrix_base import GenTraceMatrixBase
from .. import services


# -------------------
## Generates a Trace Matrix report in text format
class GenTraceMatrixTxt(GenBaseTxt, GenTraceMatrixBase):
    # -------------------
    ## constructor
    #
    # @param matrix   the data to use
    def __init__(self, matrix):
        super().__init__()
        ## holds matrix info
        self._matrix = matrix
        ## holds path to the output file
        self._path = os.path.join(services.cfg.outdir, 'trace.txt')
        ## holds file pointer to the output file
        self._fp = None

    # -------------------
    ## generate the report
    #
    # @return None
    def gen(self):
        self._init()

        services.logger.start('report: trace matrix')

        with open(self._path, 'w') as self._fp:
            self._gen_test_run_details(self._fp)
            self._gen_title(self._fp, 'Trace Matrix')

            self._load_matrix_requirements()
            self._report_requirements(self._report_header, self._report_desc, self._report_details)

    # -------------------
    ## callback to report the current requirement and tester info
    #
    # @param req_id   the requirement id to report
    # @param info     the info to report
    # @return None
    def _report_header(self, req_id, info):
        self._fp.write(f'req id: {req_id} {info}\n')

    # -------------------
    ## callback to report the current requirement's description (if available)
    #
    # @param desc     the description to report
    # @return None
    def _report_desc(self, desc):
        self._fp.write(f'   desc : {desc}\n')

    # -------------------
    ## callback to report protocol id and info for the current requirement
    #
    # @param proto_id     the protocol id to report
    # @param proto_info   the protocol info to report
    # @return None
    def _report_details(self, proto_id, proto_info):
        if proto_id is None and proto_info is None:
            self._fp.write(f'\n')
        elif proto_id is None:
            self._fp.write(f'   {proto_info}\n')
        else:
            self._fp.write(f'   proto: {proto_id} {proto_info}\n')
