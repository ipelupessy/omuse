from amuse.community import *
from amuse.community.interface.common import CommonCodeInterface, CommonCode

class iemicInterface(CodeInterface,CommonCodeInterface):
    include_headers = ['worker_code.h']

    def __init__(self, **keyword_arguments):
        CodeInterface.__init__(self, name_of_the_worker="iemic_worker", **keyword_arguments)

    @remote_function
    def initialize():
        returns ()

    @remote_function
    def set_default_params():
        returns ()

    @remote_function
    def get_ocean_params():
        returns (ocean_params="s")

    @remote_function
    def set_ocean_params(ocean_params="s"):
        returns ()

    @remote_function
    def get_continuation_params():
        returns (continuation_params="s")

    @remote_function
    def set_continuation_params(continuation_params="s"):
        returns ()

    @remote_function
    def commit_parameters():
        returns ()

    @remote_function
    def step():
        returns ()

    @remote_function
    def cleanup_code():
        returns ()

    @remote_function(must_handle_array=True)
    def get_u(i=0, j=0, k=0):
        returns (var=0.)

    @remote_function(must_handle_array=True)
    def get_v(i=0, j=0, k=0):
        returns (var=0.)

    @remote_function(must_handle_array=True)
    def get_w(i=0, j=0, k=0):
        returns (var=0.)

    @remote_function(must_handle_array=True)
    def get_p(i=0, j=0, k=0):
        returns (var=0.)

    @remote_function(must_handle_array=True)
    def get_t(i=0, j=0, k=0):
        returns (var=0.)

    @remote_function(must_handle_array=True)
    def get_s(i=0, j=0, k=0):
        returns (var=0.)

class iemic(InCodeComponentImplementation):
    def __init__(self, **options):
        InCodeComponentImplementation.__init__(self,  iemicInterface(**options), **options)