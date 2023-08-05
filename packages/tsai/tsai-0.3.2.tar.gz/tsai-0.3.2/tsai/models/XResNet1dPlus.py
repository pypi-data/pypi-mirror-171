# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/112b_models.XResNet1dPlus.ipynb.

# %% auto 0
__all__ = ['XResNet1dPlus', 'xresnet1d18plus', 'xresnet1d34plus', 'xresnet1d50plus', 'xresnet1d101plus', 'xresnet1d152plus',
           'xresnet1d18_deepplus', 'xresnet1d34_deepplus', 'xresnet1d50_deepplus', 'xresnet1d18_deeperplus',
           'xresnet1d34_deeperplus', 'xresnet1d50_deeperplus']

# %% ../../nbs/112b_models.XResNet1dPlus.ipynb 3
from ..imports import *
from .layers import *
from .utils import *

# %% ../../nbs/112b_models.XResNet1dPlus.ipynb 4
class XResNet1dPlus(nn.Sequential):
    @delegates(ResBlock1dPlus)
    def __init__(self, block, expansion, layers, fc_dropout=0.0, c_in=3, n_out=1000, stem_szs=(32,32,64),
                 widen=1.0, sa=False, act_cls=defaults.activation, ks=3, stride=2, coord=False, **kwargs):
        store_attr('block,expansion,act_cls,ks')
        if ks % 2 == 0: raise Exception('kernel size has to be odd!')
        stem_szs = [c_in, *stem_szs]
        stem = [ConvBlock(stem_szs[i], stem_szs[i+1], ks=ks, coord=coord, stride=stride if i==0 else 1,
                          act=act_cls)
                for i in range(3)]

        block_szs = [int(o*widen) for o in [64,128,256,512] +[256]*(len(layers)-4)]
        block_szs = [64//expansion] + block_szs
        blocks    = self._make_blocks(layers, block_szs, sa, coord, stride, **kwargs)
        backbone = nn.Sequential(*stem, MaxPool(ks=ks, stride=stride, padding=ks//2, ndim=1), *blocks)
        head = nn.Sequential(AdaptiveAvgPool(sz=1, ndim=1), Flatten(), nn.Dropout(fc_dropout),
                             nn.Linear(block_szs[-1]*expansion, n_out))
        super().__init__(OrderedDict([('backbone', backbone), ('head', head)]))
        self._init_cnn(self)

    def _make_blocks(self, layers, block_szs, sa, coord, stride, **kwargs):
        return [self._make_layer(ni=block_szs[i], nf=block_szs[i+1], blocks=l, coord=coord, 
                                 stride=1 if i==0 else stride, sa=sa and i==len(layers)-4, **kwargs)
                for i,l in enumerate(layers)]

    def _make_layer(self, ni, nf, blocks, coord, stride, sa, **kwargs):
        return nn.Sequential(
            *[self.block(self.expansion, ni if i==0 else nf, nf, coord=coord, stride=stride if i==0 else 1,
                      sa=sa and i==(blocks-1), act_cls=self.act_cls, ks=self.ks, **kwargs)
              for i in range(blocks)])
    
    def _init_cnn(self, m):
        if getattr(self, 'bias', None) is not None: nn.init.constant_(self.bias, 0)
        if isinstance(self, (nn.Conv1d,nn.Conv2d,nn.Conv3d,nn.Linear)): nn.init.kaiming_normal_(self.weight)
        for l in m.children(): self._init_cnn(l)

# %% ../../nbs/112b_models.XResNet1dPlus.ipynb 5
def _xresnetplus(expansion, layers, **kwargs):
    return XResNet1dPlus(ResBlock1dPlus, expansion, layers, **kwargs)

# %% ../../nbs/112b_models.XResNet1dPlus.ipynb 6
@delegates(ResBlock)
def xresnet1d18plus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [2, 2,  2, 2], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d34plus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [3, 4,  6, 3], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d50plus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(4, [3, 4,  6, 3], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d101plus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(4, [3, 4, 23, 3], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d152plus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(4, [3, 8, 36, 3], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d18_deepplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [2,2,2,2,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d34_deepplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [3,4,6,3,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d50_deepplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(4, [3,4,6,3,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d18_deeperplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [2,2,1,1,1,1,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d34_deeperplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(1, [3,4,6,3,1,1,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
@delegates(ResBlock)
def xresnet1d50_deeperplus (c_in, c_out, act=nn.ReLU, **kwargs): return _xresnetplus(4, [3,4,6,3,1,1,1,1], c_in=c_in, n_out=c_out, act_cls=act, **kwargs)
