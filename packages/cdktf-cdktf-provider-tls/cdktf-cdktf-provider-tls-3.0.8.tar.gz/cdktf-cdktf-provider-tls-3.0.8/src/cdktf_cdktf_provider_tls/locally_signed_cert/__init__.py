'''
# `tls_locally_signed_cert`

Refer to the Terraform Registory for docs: [`tls_locally_signed_cert`](https://www.terraform.io/docs/providers/tls/r/locally_signed_cert).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class LocallySignedCert(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tls.locallySignedCert.LocallySignedCert",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert tls_locally_signed_cert}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allowed_uses: typing.Sequence[builtins.str],
        ca_cert_pem: builtins.str,
        ca_private_key_pem: builtins.str,
        cert_request_pem: builtins.str,
        validity_period_hours: jsii.Number,
        early_renewal_hours: typing.Optional[jsii.Number] = None,
        is_ca_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_subject_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert tls_locally_signed_cert} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allowed_uses: List of key usages allowed for the issued certificate. Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#allowed_uses LocallySignedCert#allowed_uses}
        :param ca_cert_pem: Certificate data of the Certificate Authority (CA) in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_cert_pem LocallySignedCert#ca_cert_pem}
        :param ca_private_key_pem: Private key of the Certificate Authority (CA) used to sign the certificate, in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_private_key_pem LocallySignedCert#ca_private_key_pem}
        :param cert_request_pem: Certificate request data in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#cert_request_pem LocallySignedCert#cert_request_pem}
        :param validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#validity_period_hours LocallySignedCert#validity_period_hours}
        :param early_renewal_hours: The resource will consider the certificate to have expired the given number of hours before its actual expiry time. This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#early_renewal_hours LocallySignedCert#early_renewal_hours}
        :param is_ca_certificate: Is the generated certificate representing a Certificate Authority (CA) (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#is_ca_certificate LocallySignedCert#is_ca_certificate}
        :param set_subject_key_id: Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#set_subject_key_id LocallySignedCert#set_subject_key_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LocallySignedCert.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = LocallySignedCertConfig(
            allowed_uses=allowed_uses,
            ca_cert_pem=ca_cert_pem,
            ca_private_key_pem=ca_private_key_pem,
            cert_request_pem=cert_request_pem,
            validity_period_hours=validity_period_hours,
            early_renewal_hours=early_renewal_hours,
            is_ca_certificate=is_ca_certificate,
            set_subject_key_id=set_subject_key_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetEarlyRenewalHours")
    def reset_early_renewal_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEarlyRenewalHours", []))

    @jsii.member(jsii_name="resetIsCaCertificate")
    def reset_is_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCaCertificate", []))

    @jsii.member(jsii_name="resetSetSubjectKeyId")
    def reset_set_subject_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetSubjectKeyId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="caKeyAlgorithm")
    def ca_key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caKeyAlgorithm"))

    @builtins.property
    @jsii.member(jsii_name="certPem")
    def cert_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certPem"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="readyForRenewal")
    def ready_for_renewal(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "readyForRenewal"))

    @builtins.property
    @jsii.member(jsii_name="validityEndTime")
    def validity_end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validityEndTime"))

    @builtins.property
    @jsii.member(jsii_name="validityStartTime")
    def validity_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validityStartTime"))

    @builtins.property
    @jsii.member(jsii_name="allowedUsesInput")
    def allowed_uses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertPemInput")
    def ca_cert_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertPemInput"))

    @builtins.property
    @jsii.member(jsii_name="caPrivateKeyPemInput")
    def ca_private_key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPrivateKeyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="certRequestPemInput")
    def cert_request_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certRequestPemInput"))

    @builtins.property
    @jsii.member(jsii_name="earlyRenewalHoursInput")
    def early_renewal_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "earlyRenewalHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="isCaCertificateInput")
    def is_ca_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCaCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="setSubjectKeyIdInput")
    def set_subject_key_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "setSubjectKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="validityPeriodHoursInput")
    def validity_period_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validityPeriodHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUses")
    def allowed_uses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUses"))

    @allowed_uses.setter
    def allowed_uses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "allowed_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUses", value)

    @builtins.property
    @jsii.member(jsii_name="caCertPem")
    def ca_cert_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCertPem"))

    @ca_cert_pem.setter
    def ca_cert_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "ca_cert_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertPem", value)

    @builtins.property
    @jsii.member(jsii_name="caPrivateKeyPem")
    def ca_private_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caPrivateKeyPem"))

    @ca_private_key_pem.setter
    def ca_private_key_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "ca_private_key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPrivateKeyPem", value)

    @builtins.property
    @jsii.member(jsii_name="certRequestPem")
    def cert_request_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certRequestPem"))

    @cert_request_pem.setter
    def cert_request_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "cert_request_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certRequestPem", value)

    @builtins.property
    @jsii.member(jsii_name="earlyRenewalHours")
    def early_renewal_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "earlyRenewalHours"))

    @early_renewal_hours.setter
    def early_renewal_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "early_renewal_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "earlyRenewalHours", value)

    @builtins.property
    @jsii.member(jsii_name="isCaCertificate")
    def is_ca_certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCaCertificate"))

    @is_ca_certificate.setter
    def is_ca_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "is_ca_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="setSubjectKeyId")
    def set_subject_key_id(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "setSubjectKeyId"))

    @set_subject_key_id.setter
    def set_subject_key_id(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "set_subject_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setSubjectKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="validityPeriodHours")
    def validity_period_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "validityPeriodHours"))

    @validity_period_hours.setter
    def validity_period_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LocallySignedCert, "validity_period_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityPeriodHours", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tls.locallySignedCert.LocallySignedCertConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allowed_uses": "allowedUses",
        "ca_cert_pem": "caCertPem",
        "ca_private_key_pem": "caPrivateKeyPem",
        "cert_request_pem": "certRequestPem",
        "validity_period_hours": "validityPeriodHours",
        "early_renewal_hours": "earlyRenewalHours",
        "is_ca_certificate": "isCaCertificate",
        "set_subject_key_id": "setSubjectKeyId",
    },
)
class LocallySignedCertConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        allowed_uses: typing.Sequence[builtins.str],
        ca_cert_pem: builtins.str,
        ca_private_key_pem: builtins.str,
        cert_request_pem: builtins.str,
        validity_period_hours: jsii.Number,
        early_renewal_hours: typing.Optional[jsii.Number] = None,
        is_ca_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_subject_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param allowed_uses: List of key usages allowed for the issued certificate. Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#allowed_uses LocallySignedCert#allowed_uses}
        :param ca_cert_pem: Certificate data of the Certificate Authority (CA) in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_cert_pem LocallySignedCert#ca_cert_pem}
        :param ca_private_key_pem: Private key of the Certificate Authority (CA) used to sign the certificate, in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_private_key_pem LocallySignedCert#ca_private_key_pem}
        :param cert_request_pem: Certificate request data in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#cert_request_pem LocallySignedCert#cert_request_pem}
        :param validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#validity_period_hours LocallySignedCert#validity_period_hours}
        :param early_renewal_hours: The resource will consider the certificate to have expired the given number of hours before its actual expiry time. This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#early_renewal_hours LocallySignedCert#early_renewal_hours}
        :param is_ca_certificate: Is the generated certificate representing a Certificate Authority (CA) (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#is_ca_certificate LocallySignedCert#is_ca_certificate}
        :param set_subject_key_id: Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#set_subject_key_id LocallySignedCert#set_subject_key_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LocallySignedCertConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument allowed_uses", value=allowed_uses, expected_type=type_hints["allowed_uses"])
            check_type(argname="argument ca_cert_pem", value=ca_cert_pem, expected_type=type_hints["ca_cert_pem"])
            check_type(argname="argument ca_private_key_pem", value=ca_private_key_pem, expected_type=type_hints["ca_private_key_pem"])
            check_type(argname="argument cert_request_pem", value=cert_request_pem, expected_type=type_hints["cert_request_pem"])
            check_type(argname="argument validity_period_hours", value=validity_period_hours, expected_type=type_hints["validity_period_hours"])
            check_type(argname="argument early_renewal_hours", value=early_renewal_hours, expected_type=type_hints["early_renewal_hours"])
            check_type(argname="argument is_ca_certificate", value=is_ca_certificate, expected_type=type_hints["is_ca_certificate"])
            check_type(argname="argument set_subject_key_id", value=set_subject_key_id, expected_type=type_hints["set_subject_key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_uses": allowed_uses,
            "ca_cert_pem": ca_cert_pem,
            "ca_private_key_pem": ca_private_key_pem,
            "cert_request_pem": cert_request_pem,
            "validity_period_hours": validity_period_hours,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if early_renewal_hours is not None:
            self._values["early_renewal_hours"] = early_renewal_hours
        if is_ca_certificate is not None:
            self._values["is_ca_certificate"] = is_ca_certificate
        if set_subject_key_id is not None:
            self._values["set_subject_key_id"] = set_subject_key_id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def allowed_uses(self) -> typing.List[builtins.str]:
        '''List of key usages allowed for the issued certificate.

        Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#allowed_uses LocallySignedCert#allowed_uses}
        '''
        result = self._values.get("allowed_uses")
        assert result is not None, "Required property 'allowed_uses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ca_cert_pem(self) -> builtins.str:
        '''Certificate data of the Certificate Authority (CA) in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_cert_pem LocallySignedCert#ca_cert_pem}
        '''
        result = self._values.get("ca_cert_pem")
        assert result is not None, "Required property 'ca_cert_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_private_key_pem(self) -> builtins.str:
        '''Private key of the Certificate Authority (CA) used to sign the certificate, in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#ca_private_key_pem LocallySignedCert#ca_private_key_pem}
        '''
        result = self._values.get("ca_private_key_pem")
        assert result is not None, "Required property 'ca_private_key_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cert_request_pem(self) -> builtins.str:
        '''Certificate request data in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#cert_request_pem LocallySignedCert#cert_request_pem}
        '''
        result = self._values.get("cert_request_pem")
        assert result is not None, "Required property 'cert_request_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity_period_hours(self) -> jsii.Number:
        '''Number of hours, after initial issuing, that the certificate will remain valid for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#validity_period_hours LocallySignedCert#validity_period_hours}
        '''
        result = self._values.get("validity_period_hours")
        assert result is not None, "Required property 'validity_period_hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def early_renewal_hours(self) -> typing.Optional[jsii.Number]:
        '''The resource will consider the certificate to have expired the given number of hours before its actual expiry time.

        This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#early_renewal_hours LocallySignedCert#early_renewal_hours}
        '''
        result = self._values.get("early_renewal_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_ca_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Is the generated certificate representing a Certificate Authority (CA) (default: ``false``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#is_ca_certificate LocallySignedCert#is_ca_certificate}
        '''
        result = self._values.get("is_ca_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def set_subject_key_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/locally_signed_cert#set_subject_key_id LocallySignedCert#set_subject_key_id}
        '''
        result = self._values.get("set_subject_key_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocallySignedCertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LocallySignedCert",
    "LocallySignedCertConfig",
]

publication.publish()
