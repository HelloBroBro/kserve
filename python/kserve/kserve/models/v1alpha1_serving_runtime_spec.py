# Copyright 2023 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kserve.configuration import Configuration


class V1alpha1ServingRuntimeSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'affinity': 'V1Affinity',
        'annotations': 'dict(str, str)',
        'built_in_adapter': 'V1alpha1BuiltInAdapter',
        'containers': 'list[V1Container]',
        'disabled': 'bool',
        'grpc_data_endpoint': 'str',
        'grpc_endpoint': 'str',
        'host_ipc': 'bool',
        'http_data_endpoint': 'str',
        'image_pull_secrets': 'list[V1LocalObjectReference]',
        'labels': 'dict(str, str)',
        'multi_model': 'bool',
        'node_selector': 'dict(str, str)',
        'protocol_versions': 'list[str]',
        'replicas': 'int',
        'storage_helper': 'V1alpha1StorageHelper',
        'supported_model_formats': 'list[V1alpha1SupportedModelFormat]',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'affinity': 'affinity',
        'annotations': 'annotations',
        'built_in_adapter': 'builtInAdapter',
        'containers': 'containers',
        'disabled': 'disabled',
        'grpc_data_endpoint': 'grpcDataEndpoint',
        'grpc_endpoint': 'grpcEndpoint',
        'host_ipc': 'hostIPC',
        'http_data_endpoint': 'httpDataEndpoint',
        'image_pull_secrets': 'imagePullSecrets',
        'labels': 'labels',
        'multi_model': 'multiModel',
        'node_selector': 'nodeSelector',
        'protocol_versions': 'protocolVersions',
        'replicas': 'replicas',
        'storage_helper': 'storageHelper',
        'supported_model_formats': 'supportedModelFormats',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, affinity=None, annotations=None, built_in_adapter=None, containers=None, disabled=None, grpc_data_endpoint=None, grpc_endpoint=None, host_ipc=None, http_data_endpoint=None, image_pull_secrets=None, labels=None, multi_model=None, node_selector=None, protocol_versions=None, replicas=None, storage_helper=None, supported_model_formats=None, tolerations=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ServingRuntimeSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affinity = None
        self._annotations = None
        self._built_in_adapter = None
        self._containers = None
        self._disabled = None
        self._grpc_data_endpoint = None
        self._grpc_endpoint = None
        self._host_ipc = None
        self._http_data_endpoint = None
        self._image_pull_secrets = None
        self._labels = None
        self._multi_model = None
        self._node_selector = None
        self._protocol_versions = None
        self._replicas = None
        self._storage_helper = None
        self._supported_model_formats = None
        self._tolerations = None
        self._volumes = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        if annotations is not None:
            self.annotations = annotations
        if built_in_adapter is not None:
            self.built_in_adapter = built_in_adapter
        self.containers = containers
        if disabled is not None:
            self.disabled = disabled
        if grpc_data_endpoint is not None:
            self.grpc_data_endpoint = grpc_data_endpoint
        if grpc_endpoint is not None:
            self.grpc_endpoint = grpc_endpoint
        if host_ipc is not None:
            self.host_ipc = host_ipc
        if http_data_endpoint is not None:
            self.http_data_endpoint = http_data_endpoint
        if image_pull_secrets is not None:
            self.image_pull_secrets = image_pull_secrets
        if labels is not None:
            self.labels = labels
        if multi_model is not None:
            self.multi_model = multi_model
        if node_selector is not None:
            self.node_selector = node_selector
        if protocol_versions is not None:
            self.protocol_versions = protocol_versions
        if replicas is not None:
            self.replicas = replicas
        if storage_helper is not None:
            self.storage_helper = storage_helper
        if supported_model_formats is not None:
            self.supported_model_formats = supported_model_formats
        if tolerations is not None:
            self.tolerations = tolerations
        if volumes is not None:
            self.volumes = volumes

    @property
    def affinity(self):
        """Gets the affinity of this V1alpha1ServingRuntimeSpec.  # noqa: E501


        :return: The affinity of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this V1alpha1ServingRuntimeSpec.


        :param affinity: The affinity of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def annotations(self):
        """Gets the annotations of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Annotations that will be add to the pod. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :return: The annotations of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1alpha1ServingRuntimeSpec.

        Annotations that will be add to the pod. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :param annotations: The annotations of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def built_in_adapter(self):
        """Gets the built_in_adapter of this V1alpha1ServingRuntimeSpec.  # noqa: E501


        :return: The built_in_adapter of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: V1alpha1BuiltInAdapter
        """
        return self._built_in_adapter

    @built_in_adapter.setter
    def built_in_adapter(self, built_in_adapter):
        """Sets the built_in_adapter of this V1alpha1ServingRuntimeSpec.


        :param built_in_adapter: The built_in_adapter of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: V1alpha1BuiltInAdapter
        """

        self._built_in_adapter = built_in_adapter

    @property
    def containers(self):
        """Gets the containers of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.  # noqa: E501

        :return: The containers of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[V1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this V1alpha1ServingRuntimeSpec.

        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.  # noqa: E501

        :param containers: The containers of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[V1Container]
        """
        if self.local_vars_configuration.client_side_validation and containers is None:  # noqa: E501
            raise ValueError("Invalid value for `containers`, must not be `None`")  # noqa: E501

        self._containers = containers

    @property
    def disabled(self):
        """Gets the disabled of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Set to true to disable use of this runtime  # noqa: E501

        :return: The disabled of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this V1alpha1ServingRuntimeSpec.

        Set to true to disable use of this runtime  # noqa: E501

        :param disabled: The disabled of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def grpc_data_endpoint(self):
        """Gets the grpc_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Grpc endpoint for inferencing  # noqa: E501

        :return: The grpc_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: str
        """
        return self._grpc_data_endpoint

    @grpc_data_endpoint.setter
    def grpc_data_endpoint(self, grpc_data_endpoint):
        """Sets the grpc_data_endpoint of this V1alpha1ServingRuntimeSpec.

        Grpc endpoint for inferencing  # noqa: E501

        :param grpc_data_endpoint: The grpc_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: str
        """

        self._grpc_data_endpoint = grpc_data_endpoint

    @property
    def grpc_endpoint(self):
        """Gets the grpc_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Grpc endpoint for internal model-management (implementing mmesh.ModelRuntime gRPC service) Assumed to be single-model runtime if omitted  # noqa: E501

        :return: The grpc_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: str
        """
        return self._grpc_endpoint

    @grpc_endpoint.setter
    def grpc_endpoint(self, grpc_endpoint):
        """Sets the grpc_endpoint of this V1alpha1ServingRuntimeSpec.

        Grpc endpoint for internal model-management (implementing mmesh.ModelRuntime gRPC service) Assumed to be single-model runtime if omitted  # noqa: E501

        :param grpc_endpoint: The grpc_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: str
        """

        self._grpc_endpoint = grpc_endpoint

    @property
    def host_ipc(self):
        """Gets the host_ipc of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Use the host's ipc namespace. Optional: Default to false.  # noqa: E501

        :return: The host_ipc of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """Sets the host_ipc of this V1alpha1ServingRuntimeSpec.

        Use the host's ipc namespace. Optional: Default to false.  # noqa: E501

        :param host_ipc: The host_ipc of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def http_data_endpoint(self):
        """Gets the http_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        HTTP endpoint for inferencing  # noqa: E501

        :return: The http_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: str
        """
        return self._http_data_endpoint

    @http_data_endpoint.setter
    def http_data_endpoint(self, http_data_endpoint):
        """Sets the http_data_endpoint of this V1alpha1ServingRuntimeSpec.

        HTTP endpoint for inferencing  # noqa: E501

        :param http_data_endpoint: The http_data_endpoint of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: str
        """

        self._http_data_endpoint = http_data_endpoint

    @property
    def image_pull_secrets(self):
        """Gets the image_pull_secrets of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod  # noqa: E501

        :return: The image_pull_secrets of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """Sets the image_pull_secrets of this V1alpha1ServingRuntimeSpec.

        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod  # noqa: E501

        :param image_pull_secrets: The image_pull_secrets of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def labels(self):
        """Gets the labels of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Labels that will be add to the pod. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :return: The labels of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1alpha1ServingRuntimeSpec.

        Labels that will be add to the pod. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :param labels: The labels of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def multi_model(self):
        """Gets the multi_model of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Whether this ServingRuntime is intended for multi-model usage or not.  # noqa: E501

        :return: The multi_model of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._multi_model

    @multi_model.setter
    def multi_model(self, multi_model):
        """Sets the multi_model of this V1alpha1ServingRuntimeSpec.

        Whether this ServingRuntime is intended for multi-model usage or not.  # noqa: E501

        :param multi_model: The multi_model of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: bool
        """

        self._multi_model = multi_model

    @property
    def node_selector(self):
        """Gets the node_selector of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/  # noqa: E501

        :return: The node_selector of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this V1alpha1ServingRuntimeSpec.

        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/  # noqa: E501

        :param node_selector: The node_selector of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def protocol_versions(self):
        """Gets the protocol_versions of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Supported protocol versions (i.e. v1 or v2 or grpc-v1 or grpc-v2)  # noqa: E501

        :return: The protocol_versions of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._protocol_versions

    @protocol_versions.setter
    def protocol_versions(self, protocol_versions):
        """Sets the protocol_versions of this V1alpha1ServingRuntimeSpec.

        Supported protocol versions (i.e. v1 or v2 or grpc-v1 or grpc-v2)  # noqa: E501

        :param protocol_versions: The protocol_versions of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[str]
        """

        self._protocol_versions = protocol_versions

    @property
    def replicas(self):
        """Gets the replicas of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Configure the number of replicas in the Deployment generated by this ServingRuntime If specified, this overrides the podsPerRuntime configuration value  # noqa: E501

        :return: The replicas of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1alpha1ServingRuntimeSpec.

        Configure the number of replicas in the Deployment generated by this ServingRuntime If specified, this overrides the podsPerRuntime configuration value  # noqa: E501

        :param replicas: The replicas of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def storage_helper(self):
        """Gets the storage_helper of this V1alpha1ServingRuntimeSpec.  # noqa: E501


        :return: The storage_helper of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: V1alpha1StorageHelper
        """
        return self._storage_helper

    @storage_helper.setter
    def storage_helper(self, storage_helper):
        """Sets the storage_helper of this V1alpha1ServingRuntimeSpec.


        :param storage_helper: The storage_helper of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: V1alpha1StorageHelper
        """

        self._storage_helper = storage_helper

    @property
    def supported_model_formats(self):
        """Gets the supported_model_formats of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        Model formats and version supported by this runtime  # noqa: E501

        :return: The supported_model_formats of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[V1alpha1SupportedModelFormat]
        """
        return self._supported_model_formats

    @supported_model_formats.setter
    def supported_model_formats(self, supported_model_formats):
        """Sets the supported_model_formats of this V1alpha1ServingRuntimeSpec.

        Model formats and version supported by this runtime  # noqa: E501

        :param supported_model_formats: The supported_model_formats of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[V1alpha1SupportedModelFormat]
        """

        self._supported_model_formats = supported_model_formats

    @property
    def tolerations(self):
        """Gets the tolerations of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        If specified, the pod's tolerations.  # noqa: E501

        :return: The tolerations of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this V1alpha1ServingRuntimeSpec.

        If specified, the pod's tolerations.  # noqa: E501

        :param tolerations: The tolerations of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """Gets the volumes of this V1alpha1ServingRuntimeSpec.  # noqa: E501

        List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes  # noqa: E501

        :return: The volumes of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1alpha1ServingRuntimeSpec.

        List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes  # noqa: E501

        :param volumes: The volumes of this V1alpha1ServingRuntimeSpec.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1ServingRuntimeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ServingRuntimeSpec):
            return True

        return self.to_dict() != other.to_dict()
