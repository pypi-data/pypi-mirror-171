'''
# `random_password`

Refer to the Terraform Registory for docs: [`random_password`](https://www.terraform.io/docs/providers/random/r/password).
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


class Password(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-random.password.Password",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/random/r/password random_password}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        length: jsii.Number,
        keepers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lower: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_lower: typing.Optional[jsii.Number] = None,
        min_numeric: typing.Optional[jsii.Number] = None,
        min_special: typing.Optional[jsii.Number] = None,
        min_upper: typing.Optional[jsii.Number] = None,
        number: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        numeric: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        override_special: typing.Optional[builtins.str] = None,
        special: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upper: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/random/r/password random_password} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param length: The length of the string desired. The minimum value for length is 1 and, length must also be >= (``min_upper`` + ``min_lower`` + ``min_numeric`` + ``min_special``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#length Password#length}
        :param keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See `the main provider documentation <../index.html>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#keepers Password#keepers}
        :param lower: Include lowercase alphabet characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#lower Password#lower}
        :param min_lower: Minimum number of lowercase alphabet characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_lower Password#min_lower}
        :param min_numeric: Minimum number of numeric characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_numeric Password#min_numeric}
        :param min_special: Minimum number of special characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_special Password#min_special}
        :param min_upper: Minimum number of uppercase alphabet characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_upper Password#min_upper}
        :param number: Include numeric characters in the result. Default value is ``true``. **NOTE**: This is deprecated, use ``numeric`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#number Password#number}
        :param numeric: Include numeric characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#numeric Password#numeric}
        :param override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in the special argument. The ``special`` argument must still be set to true for any overwritten characters to be used in generation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#override_special Password#override_special}
        :param special: Include special characters in the result. These are ``!@#$%&*()-_=+[]{}<>:?``. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#special Password#special}
        :param upper: Include uppercase alphabet characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#upper Password#upper}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Password.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PasswordConfig(
            length=length,
            keepers=keepers,
            lower=lower,
            min_lower=min_lower,
            min_numeric=min_numeric,
            min_special=min_special,
            min_upper=min_upper,
            number=number,
            numeric=numeric,
            override_special=override_special,
            special=special,
            upper=upper,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetKeepers")
    def reset_keepers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepers", []))

    @jsii.member(jsii_name="resetLower")
    def reset_lower(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLower", []))

    @jsii.member(jsii_name="resetMinLower")
    def reset_min_lower(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLower", []))

    @jsii.member(jsii_name="resetMinNumeric")
    def reset_min_numeric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNumeric", []))

    @jsii.member(jsii_name="resetMinSpecial")
    def reset_min_special(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSpecial", []))

    @jsii.member(jsii_name="resetMinUpper")
    def reset_min_upper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinUpper", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @jsii.member(jsii_name="resetNumeric")
    def reset_numeric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumeric", []))

    @jsii.member(jsii_name="resetOverrideSpecial")
    def reset_override_special(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideSpecial", []))

    @jsii.member(jsii_name="resetSpecial")
    def reset_special(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpecial", []))

    @jsii.member(jsii_name="resetUpper")
    def reset_upper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpper", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bcryptHash")
    def bcrypt_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bcryptHash"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="result")
    def result(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "result"))

    @builtins.property
    @jsii.member(jsii_name="keepersInput")
    def keepers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "keepersInput"))

    @builtins.property
    @jsii.member(jsii_name="lengthInput")
    def length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lengthInput"))

    @builtins.property
    @jsii.member(jsii_name="lowerInput")
    def lower_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lowerInput"))

    @builtins.property
    @jsii.member(jsii_name="minLowerInput")
    def min_lower_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLowerInput"))

    @builtins.property
    @jsii.member(jsii_name="minNumericInput")
    def min_numeric_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNumericInput"))

    @builtins.property
    @jsii.member(jsii_name="minSpecialInput")
    def min_special_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSpecialInput"))

    @builtins.property
    @jsii.member(jsii_name="minUpperInput")
    def min_upper_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minUpperInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="numericInput")
    def numeric_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "numericInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideSpecialInput")
    def override_special_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overrideSpecialInput"))

    @builtins.property
    @jsii.member(jsii_name="specialInput")
    def special_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "specialInput"))

    @builtins.property
    @jsii.member(jsii_name="upperInput")
    def upper_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "upperInput"))

    @builtins.property
    @jsii.member(jsii_name="keepers")
    def keepers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "keepers"))

    @keepers.setter
    def keepers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "keepers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepers", value)

    @builtins.property
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @length.setter
    def length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "length", value)

    @builtins.property
    @jsii.member(jsii_name="lower")
    def lower(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lower"))

    @lower.setter
    def lower(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "lower").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lower", value)

    @builtins.property
    @jsii.member(jsii_name="minLower")
    def min_lower(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLower"))

    @min_lower.setter
    def min_lower(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "min_lower").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLower", value)

    @builtins.property
    @jsii.member(jsii_name="minNumeric")
    def min_numeric(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNumeric"))

    @min_numeric.setter
    def min_numeric(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "min_numeric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNumeric", value)

    @builtins.property
    @jsii.member(jsii_name="minSpecial")
    def min_special(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSpecial"))

    @min_special.setter
    def min_special(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "min_special").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSpecial", value)

    @builtins.property
    @jsii.member(jsii_name="minUpper")
    def min_upper(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minUpper"))

    @min_upper.setter
    def min_upper(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "min_upper").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minUpper", value)

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "number"))

    @number.setter
    def number(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)

    @builtins.property
    @jsii.member(jsii_name="numeric")
    def numeric(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "numeric"))

    @numeric.setter
    def numeric(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "numeric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numeric", value)

    @builtins.property
    @jsii.member(jsii_name="overrideSpecial")
    def override_special(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideSpecial"))

    @override_special.setter
    def override_special(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "override_special").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideSpecial", value)

    @builtins.property
    @jsii.member(jsii_name="special")
    def special(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "special"))

    @special.setter
    def special(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "special").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "special", value)

    @builtins.property
    @jsii.member(jsii_name="upper")
    def upper(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "upper"))

    @upper.setter
    def upper(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Password, "upper").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upper", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-random.password.PasswordConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "length": "length",
        "keepers": "keepers",
        "lower": "lower",
        "min_lower": "minLower",
        "min_numeric": "minNumeric",
        "min_special": "minSpecial",
        "min_upper": "minUpper",
        "number": "number",
        "numeric": "numeric",
        "override_special": "overrideSpecial",
        "special": "special",
        "upper": "upper",
    },
)
class PasswordConfig(cdktf.TerraformMetaArguments):
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
        length: jsii.Number,
        keepers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lower: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        min_lower: typing.Optional[jsii.Number] = None,
        min_numeric: typing.Optional[jsii.Number] = None,
        min_special: typing.Optional[jsii.Number] = None,
        min_upper: typing.Optional[jsii.Number] = None,
        number: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        numeric: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        override_special: typing.Optional[builtins.str] = None,
        special: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        upper: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param length: The length of the string desired. The minimum value for length is 1 and, length must also be >= (``min_upper`` + ``min_lower`` + ``min_numeric`` + ``min_special``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#length Password#length}
        :param keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See `the main provider documentation <../index.html>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#keepers Password#keepers}
        :param lower: Include lowercase alphabet characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#lower Password#lower}
        :param min_lower: Minimum number of lowercase alphabet characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_lower Password#min_lower}
        :param min_numeric: Minimum number of numeric characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_numeric Password#min_numeric}
        :param min_special: Minimum number of special characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_special Password#min_special}
        :param min_upper: Minimum number of uppercase alphabet characters in the result. Default value is ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_upper Password#min_upper}
        :param number: Include numeric characters in the result. Default value is ``true``. **NOTE**: This is deprecated, use ``numeric`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#number Password#number}
        :param numeric: Include numeric characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#numeric Password#numeric}
        :param override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in the special argument. The ``special`` argument must still be set to true for any overwritten characters to be used in generation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#override_special Password#override_special}
        :param special: Include special characters in the result. These are ``!@#$%&*()-_=+[]{}<>:?``. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#special Password#special}
        :param upper: Include uppercase alphabet characters in the result. Default value is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#upper Password#upper}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(PasswordConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument length", value=length, expected_type=type_hints["length"])
            check_type(argname="argument keepers", value=keepers, expected_type=type_hints["keepers"])
            check_type(argname="argument lower", value=lower, expected_type=type_hints["lower"])
            check_type(argname="argument min_lower", value=min_lower, expected_type=type_hints["min_lower"])
            check_type(argname="argument min_numeric", value=min_numeric, expected_type=type_hints["min_numeric"])
            check_type(argname="argument min_special", value=min_special, expected_type=type_hints["min_special"])
            check_type(argname="argument min_upper", value=min_upper, expected_type=type_hints["min_upper"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument numeric", value=numeric, expected_type=type_hints["numeric"])
            check_type(argname="argument override_special", value=override_special, expected_type=type_hints["override_special"])
            check_type(argname="argument special", value=special, expected_type=type_hints["special"])
            check_type(argname="argument upper", value=upper, expected_type=type_hints["upper"])
        self._values: typing.Dict[str, typing.Any] = {
            "length": length,
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
        if keepers is not None:
            self._values["keepers"] = keepers
        if lower is not None:
            self._values["lower"] = lower
        if min_lower is not None:
            self._values["min_lower"] = min_lower
        if min_numeric is not None:
            self._values["min_numeric"] = min_numeric
        if min_special is not None:
            self._values["min_special"] = min_special
        if min_upper is not None:
            self._values["min_upper"] = min_upper
        if number is not None:
            self._values["number"] = number
        if numeric is not None:
            self._values["numeric"] = numeric
        if override_special is not None:
            self._values["override_special"] = override_special
        if special is not None:
            self._values["special"] = special
        if upper is not None:
            self._values["upper"] = upper

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
    def length(self) -> jsii.Number:
        '''The length of the string desired.

        The minimum value for length is 1 and, length must also be >= (``min_upper`` + ``min_lower`` + ``min_numeric`` + ``min_special``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#length Password#length}
        '''
        result = self._values.get("length")
        assert result is not None, "Required property 'length' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def keepers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Arbitrary map of values that, when changed, will trigger recreation of resource.

        See `the main provider documentation <../index.html>`_ for more information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#keepers Password#keepers}
        '''
        result = self._values.get("keepers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def lower(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include lowercase alphabet characters in the result. Default value is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#lower Password#lower}
        '''
        result = self._values.get("lower")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def min_lower(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of lowercase alphabet characters in the result. Default value is ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_lower Password#min_lower}
        '''
        result = self._values.get("min_lower")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_numeric(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of numeric characters in the result. Default value is ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_numeric Password#min_numeric}
        '''
        result = self._values.get("min_numeric")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_special(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of special characters in the result. Default value is ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_special Password#min_special}
        '''
        result = self._values.get("min_special")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_upper(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of uppercase alphabet characters in the result. Default value is ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#min_upper Password#min_upper}
        '''
        result = self._values.get("min_upper")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include numeric characters in the result. Default value is ``true``. **NOTE**: This is deprecated, use ``numeric`` instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#number Password#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def numeric(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include numeric characters in the result. Default value is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#numeric Password#numeric}
        '''
        result = self._values.get("numeric")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def override_special(self) -> typing.Optional[builtins.str]:
        '''Supply your own list of special characters to use for string generation.

        This overrides the default character list in the special argument.  The ``special`` argument must still be set to true for any overwritten characters to be used in generation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#override_special Password#override_special}
        '''
        result = self._values.get("override_special")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def special(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include special characters in the result. These are ``!@#$%&*()-_=+[]{}<>:?``. Default value is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#special Password#special}
        '''
        result = self._values.get("special")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def upper(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Include uppercase alphabet characters in the result. Default value is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/random/r/password#upper Password#upper}
        '''
        result = self._values.get("upper")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PasswordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Password",
    "PasswordConfig",
]

publication.publish()
