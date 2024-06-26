from aot.networks.engines.aot_engine import AOTEngine, AOTInferEngine
from aot.networks.engines.deaot_engine import DeAOTEngine, DeAOTInferEngine
from aot.networks.engines.dm_aot_engine import DMAOTEngine, DMAOTInferEngine
from aot.networks.engines.dm_deaot_engine import DMDeAOTEngine, DMDeAOTInferEngine


def build_engine(name, phase='train', **kwargs):
    if name == 'aotengine':
        if phase == 'train':
            return AOTEngine(**kwargs)
        elif phase == 'eval':
            return AOTInferEngine(**kwargs)
        else:
            raise NotImplementedError
    elif name == 'deaotengine':
        if phase == 'train':
            return DeAOTEngine(**kwargs)
        elif phase == 'eval':
            return DeAOTInferEngine(**kwargs)
        else:
            raise NotImplementedError
    elif name == 'dmaotengine':
        if phase == 'train':
            return DMAOTEngine(**kwargs)
        elif phase == 'eval':
            return DMAOTInferEngine(**kwargs)
        else:
            raise NotImplementedError
    elif name == 'dmdeaotengine':
        if phase == 'train':
            return DMDeAOTEngine(**kwargs)
        elif phase == 'eval':
            return DMDeAOTInferEngine(**kwargs)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError
