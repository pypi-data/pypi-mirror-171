import numpy as np
from typing import List, Union
from .View import View


class TGDataset:
    def __init__(self, *, name: str, data: dict) -> None:
        self._name = name
        self._data = data
    def to_dict(self):
        return {
            'name': self._name,
            'data': self._data
        }

class TGSeries:
    def __init__(self, *, type: str, dataset: str, encoding: dict, attributes: dict, title: str='') -> None:
        self._type = type
        self._dataset = dataset
        self._encoding = encoding
        self._attributes = attributes
        self._title = title
    def to_dict(self):
        return {
            'type': self._type,
            'dataset': self._dataset,
            'encoding': self._encoding,
            'attributes': self._attributes,
            'title': self._title
        }

class TimeseriesGraph(View):
    def __init__(self, *,
        legend_opts: Union[None, dict]=None,
        **kwargs
    ) -> None:
        super().__init__('TimeseriesGraph', **kwargs)
        self._datasets = []
        self._series = []
        self._legend_opts = legend_opts
        # time_offset is used to allow float64 type in the time arrays
        self._time_offset = None
    def add_line_series(self, *,
            name: str,
            t: np.array,
            y: np.array,
            color: str,
            width: Union[None, int]=None,
            dash: Union[None, List[int]]=None
        ):
        # allow float64 for time array
        t = self._handle_time_offset_t(t)

        if t.dtype == np.float64:
            raise Exception('Cannot handle float64 datatype for t parameter in add_line_series')
        if y.dtype == np.float64:
            raise Exception('Cannot handle float64 datatype for y parameter in add_line_series')

        attributes = {'color': color}
        if width is not None:
            attributes['width'] = width
        if dash is not None:
            attributes['dash'] = dash
        self._add_series(type='line', name=name, t=t, y=y, attributes=attributes)
        return self
    def add_marker_series(self, *,
            name: str,
            t: np.array,
            y: np.array,
            color: str,
            radius: Union[None, int]=None,
            shape: Union[None, str]=None
        ):
        # allow float64 for time array
        t = self._handle_time_offset_t(t)
        
        if t.dtype == np.float64:
            raise Exception('Cannot handle float64 datatype for t parameter in add_marker_series')
        if y.dtype == np.float64:
            raise Exception('Cannot handle float64 datatype for y parameter in add_marker_series')
        attributes = {'color': color}
        if radius is not None:
            attributes['radius'] = radius
        if shape is not None:
            attributes['shape'] = shape
        self._add_series(type='marker', name=name, t=t, y=y, attributes=attributes)
        return self
    def add_dataset(self, ds: TGDataset):
        self._datasets.append(ds)
        return self
    def add_series(self, s: TGSeries):
        self._series.append(s)
        return self
    def to_dict(self) -> dict:
        ret = {
            'type': self.type,
            'datasets': [ds.to_dict() for ds in self._datasets],
            'series': [s.to_dict() for s in self._series]
        }
        if self._time_offset is not None:
            ret['timeOffset'] = self._time_offset
        if self._legend_opts is not None:
            ret['legendOpts'] = self._legend_opts
        return ret
    def register_task_handlers(self, task_backend):
        return super().register_task_handlers(task_backend)
    def child_views(self) -> List[View]:
        return []
    def _add_series(self, *, type: str, name: str, t: np.array, y: np.array, attributes: dict):
        ds = TGDataset(
            name=name,
            data={
                't': t,
                'y': y
            }
        )
        s = TGSeries(
            type=type,
            encoding={'t': 't', 'y': 'y'},
            dataset=name,
            attributes=attributes,
            title=name
        )
        self.add_dataset(ds)
        self.add_series(s)
    def _handle_time_offset_t(self, t: np.array):
        if t.dtype == np.float64:
            # We have a float64, let's see if we have a time offset
            if self._time_offset is None:
                # we don't, let's make one
                self._time_offset = t[0]
        if self._time_offset is not None:
            # if we have a time offset, let's subtract it
            t = (t - self._time_offset)
            if t.dtype == np.float64:
                # if we have a float64, now that we've subtracted the time offset, it's safe to use float32
                t = t.astype(np.float32)
        return t
