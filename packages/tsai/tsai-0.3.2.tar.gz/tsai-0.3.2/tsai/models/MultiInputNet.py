# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/130_models.MultiInputNet.ipynb.

# %% auto 0
__all__ = ['MultiInputNet']

# %% ../../nbs/130_models.MultiInputNet.ipynb 3
from ..imports import *
from .layers import *
from .utils import *

# %% ../../nbs/130_models.MultiInputNet.ipynb 4
class MultiInputNet(Module):
    
    def __init__(self, *models, c_out=None, reshape_fn=None, multi_output=False, custom_head=None, device=None, **kwargs):
        r"""
        Args:
            models       : list of models (one model per dataloader in dls). They all must have a head.
            c_out        : output layer size.
            reshape_fn   : callable to transform a 3d input into a 2d input (Noop, Reshape(-1), GAP1d())
            multi_output : determines if the model creates M+1 output (one per model plus a combined one), or just a single output (combined one).
            custom_head  : allows you to pass a custom joint head. If None a MLP will be created (you can pass 'layers' to this default head using kwargs)
            device       : cpu or cuda. If None, default_device() will be chosen.
            kwargs       : head kwargs
        """

        c_out = ifnone(c_out, get_layers(models[0], cond=is_linear)[-1].out_features)
        self.M = len(models)
        self.m = []
        self.backbones = nn.ModuleList()
        self.heads = nn.ModuleList()
        head_nf = 0
        min_nf = np.inf
        for i, model in enumerate(models):
            try: # if subscriptable
                self.heads.append(model[1])
                self.backbones.append(model[0])
            except:
                self.heads.append(model.head)
                model.head = Identity()
                self.backbones.append(model)
            self.m.append(Sequential(self.backbones[-1], self.heads[-1]))
            head_nf += model.head_nf
            min_nf = min(min_nf, model.head_nf)

        self.head_nf = head_nf
        if custom_head is None: head = create_fc_head(head_nf, c_out, 1, **kwargs)
        else: head = custom_head(self.head_nf, c_out, **kwargs)
        self.heads.append(head)
        self.multi_output = multi_output
        self.m.append(self)
        self.reshape = ifnone(reshape_fn, GAP1d())
        self.concat = Concat(dim=1)
        device = ifnone(device, default_device())
        self.to(device=device)

    def forward(self, xs):
        xs = tuple(*xs) if len(xs) == 1 else xs
        out = []
        for k in range(self.M):
            x = xs[k]
            # Create separate features
            feat = self.backbones[k](*x) if isinstance(x, (list, tuple, L)) else self.backbones[k](x)

            # Process features separately
            if self.training and self.multi_output: out.append(self.heads[k](feat))
            
            # Concat features
            if feat.ndim == 3: feat = self.reshape(feat)
            concat_feats = feat if k==0 else self.concat([concat_feats, feat])
            
        # Process joint features
        out.append(self.heads[-1](concat_feats))
        if self.training and self.multi_output: return out
        else:  return out[0]
