from typing import Any, Dict

from h1st.h1flow.h1step_containable import NodeContainable
from h1st.trust.trustable import Trustable

from h1st.model.repository.model_repository import ModelRepository
from h1st.model.modeler import Modelable


class Model(NodeContainable, Trustable, Modelable):
    """
    Base class for H1st Model.

    To create your own model, inherit `Model` class and implement `process` accordingly.
    Please refer to Tutorial for more details how to create a model.

    The framework allows you to persist and load model to the model repository.
    To persist the model, you can call `persist()`, and then `load` to retrieve the model.
    See `persist()` and `load()` document for more detail.

        .. code-block:: python
           :caption: Model Persistence and Loading Example

           import h1st

           class MyModeler(h1st.model.Modeler):
               def build_model(self):
                   ...

           class MyModel(h1st.model.Model):



           my_modeler = MyModeler()
           my_modeler.model_class = MyModel

           my_model = my_modeler.build_model()

           # Persist the model to repo
           my_model.persist('1st_version')

           # Load the model from the repo
           my_model_2 = MyModel()
           my_model_2.load('1st_version')
    """

    ## TODO: Need a better naming and the definition of the property
    @property
    def stats(self):
        return getattr(self, "__stats__", None)

    @stats.setter
    def stats(self, value) -> Dict:
        setattr(self, "__stats__", value)

    @property
    def metrics(self):
        if not hasattr(self, "__metrics__"):
            setattr(self, "__metrics__", {})
        return getattr(self, "__metrics__")

    @metrics.setter
    def metrics(self, value) -> Dict:
        setattr(self, "__metrics__", value)

    def persist(self, version=None) -> str:
        """
        Persist this model's properties to the ModelRepository. Currently, only `stats`, `metrics`, `model` properties are supported.

        `model` property could be single model, list or dict of models
        Currently, only sklearn and tensorflow-keras are supported.

        :param version: model version, leave blank for autogeneration
        :returns: model version
        """
        repo = ModelRepository.get_model_repo(self)
        return repo.persist(model=self, version=version)

    def load(self, version: str = None) -> Any:
        """
        Load parameters from the specified `version` from the ModelRepository.
        Leave version blank to load latest version.
        """
        repo = ModelRepository.get_model_repo(self)
        repo.load(model=self, version=version)

        return self

    def process(self, input_data: Dict) -> Dict:
        """
        Implement logic to process data

        :params input_data: data to process
        :returns: processing result as a dictionary
        """
        # not raise NotImplementedError so the initial model created by integrator will just work
        return input_data
