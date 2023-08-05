from typing import Dict

from sara_sdk.common.session import Session
from ...utils.rest import retrieve as _retrieve, list_paginated as _list_paginated, list as _list, update as _update, delete as _delete, create as _create

RESOURCE = "missions/stages"


def list(session: Session = None, **filters):
    """
    List a array of stages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of stages

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list(page=1,page_size=10,name="stage name")
    """
    result = _list(resource=RESOURCE, session=session, version="v2", **filters)
    return result


def list_paginated(session: Session = None, **filters):
    """
    List iterator of pages of stages

    Args:
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of stages

    Returns:
      result (json): returns the result of the request as json by page

    Example:
      >>> next(list(page=1,page_size=10,name="stage name"))
    """
    result = _list_paginated(resource=RESOURCE, session=session,
                             version="v2", **filters)
    return result


def retrieve(uuid: str, session: Session = None):
    """
    Retrieve a stage by uuid

    Args:
      uuid (string): stage uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(RESOURCE, id=uuid, session=session, version="v2")
    return result


def update(uuid: str, model: Dict, session: Session = None):
    """
    Update a stage by passing uuid and an model (Data to update)

    Args:
      uuid (string): stage uuid to retrieve
      model (Dict): A dictionary with the data the will be updated on stage
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> update("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", { "name": "new name" })
    """
    result = _update(RESOURCE, id=uuid, payload=model,
                     session=session,  version="v2")
    return result


def create(model: Dict, session: Session = None):
    """
    Create a stage by passing an model (Data)

    Args:
      model (Dict): A dictionary with the data the will be used to create an stage
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json
    """
    result = _create(RESOURCE, payload=model, session=session, version="v2")
    return result


def delete(uuid: str, session: Session = None):
    """
    Delete a stage by passing uuid

    Args:
      uuid (string): stage uuid to delete
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> delete("f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _delete(RESOURCE, id=uuid, session=session, version="v2")
    return result


def list_steps(stage: str, session: Session = None, **filters):
    """
    List a array of steps of one stage

    Args:
      stage (string): stage uuid to retrieve
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of steps

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_steps("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", page=1,page_size=10,name="step name")
    """
    result = _list(resource="{}/{}/steps".format(RESOURCE, stage),
                   session=session, version="v2", **filters)
    return result


def retrieve_steps(stage: str, step: str, session: Session = None):
    """
    Retrieve a step of one stage by uuid

    Args:
      stage (string): stage uuid to retrieve
      step (string): step uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_step("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", "f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/steps".format(RESOURCE,
                       stage), id=step, session=session, version="v2")
    return result


def list_params(stage: str, session: Session = None, **filters):
    """
    List a array of params of one stage

    Args:
      stage (string): stage uuid to retrieve
      session (Session): Used only if want to use a different session instead default
      filters (Any): filters to pass to filter the list of params

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> list_params("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", page=1,page_size=10,name="param name")
    """
    result = _list(resource="{}/{}/params".format(RESOURCE, stage),
                   session=session, version="v2", **filters)
    return result


def retrieve_params(stage: str, param: str, session: Session = None):
    """
    Retrieve a param of one stage by uuid

    Args:
      stage (string): stage uuid to retrieve
      param (string): param uuid to retrieve
      session (Session): Used only if want to use a different session instead default

    Returns:
      result (json): returns the result of the request as json

    Example:
      >>> retrieve_params("f8b85a7a-4540-4d46-a2ed-00e6134ee84a", "f8b85a7a-4540-4d46-a2ed-00e6134ee84a")
    """
    result = _retrieve(resource="{}/{}/params".format(RESOURCE,
                       stage), id=param, session=session, version="v2")
    return result
