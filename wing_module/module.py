from drongo.utils import dict2


class Module(object):
    def __init__(self, app, **config):
        self.app = app
        self.config = dict2.from_dict(config)

        self.init(self.config)
