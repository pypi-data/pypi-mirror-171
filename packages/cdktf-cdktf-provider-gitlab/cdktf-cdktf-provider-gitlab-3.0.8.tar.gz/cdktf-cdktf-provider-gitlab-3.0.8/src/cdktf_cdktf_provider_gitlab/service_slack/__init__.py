'''
# `gitlab_service_slack`

Refer to the Terraform Registory for docs: [`gitlab_service_slack`](https://www.terraform.io/docs/providers/gitlab/r/service_slack).
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


class ServiceSlack(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.serviceSlack.ServiceSlack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack gitlab_service_slack}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        project: builtins.str,
        webhook: builtins.str,
        branches_to_be_notified: typing.Optional[builtins.str] = None,
        confidential_issue_channel: typing.Optional[builtins.str] = None,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issue_channel: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_request_channel: typing.Optional[builtins.str] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        note_channel: typing.Optional[builtins.str] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_only_broken_pipelines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_only_default_branch: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pipeline_channel: typing.Optional[builtins.str] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_channel: typing.Optional[builtins.str] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_push_channel: typing.Optional[builtins.str] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
        wiki_page_channel: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack gitlab_service_slack} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project: ID of the project you want to activate integration on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#project ServiceSlack#project}
        :param webhook: Webhook URL (ex.: https://hooks.slack.com/services/...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#webhook ServiceSlack#webhook}
        :param branches_to_be_notified: Branches to send notifications for. Valid options are "all", "default", "protected", and "default_and_protected". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#branches_to_be_notified ServiceSlack#branches_to_be_notified}
        :param confidential_issue_channel: The name of the channel to receive confidential issue events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issue_channel ServiceSlack#confidential_issue_channel}
        :param confidential_issues_events: Enable notifications for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issues_events ServiceSlack#confidential_issues_events}
        :param confidential_note_events: Enable notifications for confidential note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_note_events ServiceSlack#confidential_note_events}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#id ServiceSlack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issue_channel: The name of the channel to receive issue events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issue_channel ServiceSlack#issue_channel}
        :param issues_events: Enable notifications for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issues_events ServiceSlack#issues_events}
        :param merge_request_channel: The name of the channel to receive merge request events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_request_channel ServiceSlack#merge_request_channel}
        :param merge_requests_events: Enable notifications for merge requests events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_requests_events ServiceSlack#merge_requests_events}
        :param note_channel: The name of the channel to receive note events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_channel ServiceSlack#note_channel}
        :param note_events: Enable notifications for note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_events ServiceSlack#note_events}
        :param notify_only_broken_pipelines: Send notifications for broken pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_broken_pipelines ServiceSlack#notify_only_broken_pipelines}
        :param notify_only_default_branch: This parameter has been replaced with ``branches_to_be_notified``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_default_branch ServiceSlack#notify_only_default_branch}
        :param pipeline_channel: The name of the channel to receive pipeline events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_channel ServiceSlack#pipeline_channel}
        :param pipeline_events: Enable notifications for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_events ServiceSlack#pipeline_events}
        :param push_channel: The name of the channel to receive push events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_channel ServiceSlack#push_channel}
        :param push_events: Enable notifications for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_events ServiceSlack#push_events}
        :param tag_push_channel: The name of the channel to receive tag push events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_channel ServiceSlack#tag_push_channel}
        :param tag_push_events: Enable notifications for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_events ServiceSlack#tag_push_events}
        :param username: Username to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#username ServiceSlack#username}
        :param wiki_page_channel: The name of the channel to receive wiki page events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_channel ServiceSlack#wiki_page_channel}
        :param wiki_page_events: Enable notifications for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_events ServiceSlack#wiki_page_events}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceSlack.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceSlackConfig(
            project=project,
            webhook=webhook,
            branches_to_be_notified=branches_to_be_notified,
            confidential_issue_channel=confidential_issue_channel,
            confidential_issues_events=confidential_issues_events,
            confidential_note_events=confidential_note_events,
            id=id,
            issue_channel=issue_channel,
            issues_events=issues_events,
            merge_request_channel=merge_request_channel,
            merge_requests_events=merge_requests_events,
            note_channel=note_channel,
            note_events=note_events,
            notify_only_broken_pipelines=notify_only_broken_pipelines,
            notify_only_default_branch=notify_only_default_branch,
            pipeline_channel=pipeline_channel,
            pipeline_events=pipeline_events,
            push_channel=push_channel,
            push_events=push_events,
            tag_push_channel=tag_push_channel,
            tag_push_events=tag_push_events,
            username=username,
            wiki_page_channel=wiki_page_channel,
            wiki_page_events=wiki_page_events,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBranchesToBeNotified")
    def reset_branches_to_be_notified(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranchesToBeNotified", []))

    @jsii.member(jsii_name="resetConfidentialIssueChannel")
    def reset_confidential_issue_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialIssueChannel", []))

    @jsii.member(jsii_name="resetConfidentialIssuesEvents")
    def reset_confidential_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialIssuesEvents", []))

    @jsii.member(jsii_name="resetConfidentialNoteEvents")
    def reset_confidential_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialNoteEvents", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssueChannel")
    def reset_issue_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssueChannel", []))

    @jsii.member(jsii_name="resetIssuesEvents")
    def reset_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesEvents", []))

    @jsii.member(jsii_name="resetMergeRequestChannel")
    def reset_merge_request_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestChannel", []))

    @jsii.member(jsii_name="resetMergeRequestsEvents")
    def reset_merge_requests_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsEvents", []))

    @jsii.member(jsii_name="resetNoteChannel")
    def reset_note_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoteChannel", []))

    @jsii.member(jsii_name="resetNoteEvents")
    def reset_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoteEvents", []))

    @jsii.member(jsii_name="resetNotifyOnlyBrokenPipelines")
    def reset_notify_only_broken_pipelines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyOnlyBrokenPipelines", []))

    @jsii.member(jsii_name="resetNotifyOnlyDefaultBranch")
    def reset_notify_only_default_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyOnlyDefaultBranch", []))

    @jsii.member(jsii_name="resetPipelineChannel")
    def reset_pipeline_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineChannel", []))

    @jsii.member(jsii_name="resetPipelineEvents")
    def reset_pipeline_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineEvents", []))

    @jsii.member(jsii_name="resetPushChannel")
    def reset_push_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushChannel", []))

    @jsii.member(jsii_name="resetPushEvents")
    def reset_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEvents", []))

    @jsii.member(jsii_name="resetTagPushChannel")
    def reset_tag_push_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPushChannel", []))

    @jsii.member(jsii_name="resetTagPushEvents")
    def reset_tag_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPushEvents", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetWikiPageChannel")
    def reset_wiki_page_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiPageChannel", []))

    @jsii.member(jsii_name="resetWikiPageEvents")
    def reset_wiki_page_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiPageEvents", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="jobEvents")
    def job_events(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "jobEvents"))

    @builtins.property
    @jsii.member(jsii_name="branchesToBeNotifiedInput")
    def branches_to_be_notified_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchesToBeNotifiedInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssueChannelInput")
    def confidential_issue_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "confidentialIssueChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEventsInput")
    def confidential_issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "confidentialIssuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEventsInput")
    def confidential_note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "confidentialNoteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issueChannelInput")
    def issue_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issueChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesEventsInput")
    def issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "issuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestChannelInput")
    def merge_request_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeRequestChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEventsInput")
    def merge_requests_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mergeRequestsEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="noteChannelInput")
    def note_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="noteEventsInput")
    def note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyOnlyBrokenPipelinesInput")
    def notify_only_broken_pipelines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyOnlyBrokenPipelinesInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyOnlyDefaultBranchInput")
    def notify_only_default_branch_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyOnlyDefaultBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineChannelInput")
    def pipeline_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineEventsInput")
    def pipeline_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pipelineEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pushChannelInput")
    def push_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pushChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEventsInput")
    def push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPushChannelInput")
    def tag_push_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagPushChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPushEventsInput")
    def tag_push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tagPushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiPageChannelInput")
    def wiki_page_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wikiPageChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiPageEventsInput")
    def wiki_page_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "wikiPageEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="branchesToBeNotified")
    def branches_to_be_notified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchesToBeNotified"))

    @branches_to_be_notified.setter
    def branches_to_be_notified(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "branches_to_be_notified").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchesToBeNotified", value)

    @builtins.property
    @jsii.member(jsii_name="confidentialIssueChannel")
    def confidential_issue_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "confidentialIssueChannel"))

    @confidential_issue_channel.setter
    def confidential_issue_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "confidential_issue_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialIssueChannel", value)

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEvents")
    def confidential_issues_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "confidentialIssuesEvents"))

    @confidential_issues_events.setter
    def confidential_issues_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "confidential_issues_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialIssuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEvents")
    def confidential_note_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "confidentialNoteEvents"))

    @confidential_note_events.setter
    def confidential_note_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "confidential_note_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialNoteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issueChannel")
    def issue_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issueChannel"))

    @issue_channel.setter
    def issue_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "issue_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issueChannel", value)

    @builtins.property
    @jsii.member(jsii_name="issuesEvents")
    def issues_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "issuesEvents"))

    @issues_events.setter
    def issues_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "issues_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestChannel")
    def merge_request_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeRequestChannel"))

    @merge_request_channel.setter
    def merge_request_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "merge_request_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestChannel", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEvents")
    def merge_requests_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mergeRequestsEvents"))

    @merge_requests_events.setter
    def merge_requests_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "merge_requests_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsEvents", value)

    @builtins.property
    @jsii.member(jsii_name="noteChannel")
    def note_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noteChannel"))

    @note_channel.setter
    def note_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "note_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteChannel", value)

    @builtins.property
    @jsii.member(jsii_name="noteEvents")
    def note_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noteEvents"))

    @note_events.setter
    def note_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "note_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnlyBrokenPipelines")
    def notify_only_broken_pipelines(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notifyOnlyBrokenPipelines"))

    @notify_only_broken_pipelines.setter
    def notify_only_broken_pipelines(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "notify_only_broken_pipelines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnlyBrokenPipelines", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnlyDefaultBranch")
    def notify_only_default_branch(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notifyOnlyDefaultBranch"))

    @notify_only_default_branch.setter
    def notify_only_default_branch(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "notify_only_default_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnlyDefaultBranch", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineChannel")
    def pipeline_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pipelineChannel"))

    @pipeline_channel.setter
    def pipeline_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "pipeline_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineChannel", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineEvents")
    def pipeline_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pipelineEvents"))

    @pipeline_events.setter
    def pipeline_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "pipeline_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineEvents", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="pushChannel")
    def push_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pushChannel"))

    @push_channel.setter
    def push_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "push_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushChannel", value)

    @builtins.property
    @jsii.member(jsii_name="pushEvents")
    def push_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pushEvents"))

    @push_events.setter
    def push_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "push_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="tagPushChannel")
    def tag_push_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagPushChannel"))

    @tag_push_channel.setter
    def tag_push_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "tag_push_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPushChannel", value)

    @builtins.property
    @jsii.member(jsii_name="tagPushEvents")
    def tag_push_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tagPushEvents"))

    @tag_push_events.setter
    def tag_push_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "tag_push_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "webhook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="wikiPageChannel")
    def wiki_page_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wikiPageChannel"))

    @wiki_page_channel.setter
    def wiki_page_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "wiki_page_channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiPageChannel", value)

    @builtins.property
    @jsii.member(jsii_name="wikiPageEvents")
    def wiki_page_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "wikiPageEvents"))

    @wiki_page_events.setter
    def wiki_page_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceSlack, "wiki_page_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiPageEvents", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.serviceSlack.ServiceSlackConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project": "project",
        "webhook": "webhook",
        "branches_to_be_notified": "branchesToBeNotified",
        "confidential_issue_channel": "confidentialIssueChannel",
        "confidential_issues_events": "confidentialIssuesEvents",
        "confidential_note_events": "confidentialNoteEvents",
        "id": "id",
        "issue_channel": "issueChannel",
        "issues_events": "issuesEvents",
        "merge_request_channel": "mergeRequestChannel",
        "merge_requests_events": "mergeRequestsEvents",
        "note_channel": "noteChannel",
        "note_events": "noteEvents",
        "notify_only_broken_pipelines": "notifyOnlyBrokenPipelines",
        "notify_only_default_branch": "notifyOnlyDefaultBranch",
        "pipeline_channel": "pipelineChannel",
        "pipeline_events": "pipelineEvents",
        "push_channel": "pushChannel",
        "push_events": "pushEvents",
        "tag_push_channel": "tagPushChannel",
        "tag_push_events": "tagPushEvents",
        "username": "username",
        "wiki_page_channel": "wikiPageChannel",
        "wiki_page_events": "wikiPageEvents",
    },
)
class ServiceSlackConfig(cdktf.TerraformMetaArguments):
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
        project: builtins.str,
        webhook: builtins.str,
        branches_to_be_notified: typing.Optional[builtins.str] = None,
        confidential_issue_channel: typing.Optional[builtins.str] = None,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issue_channel: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_request_channel: typing.Optional[builtins.str] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        note_channel: typing.Optional[builtins.str] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_only_broken_pipelines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notify_only_default_branch: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pipeline_channel: typing.Optional[builtins.str] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_channel: typing.Optional[builtins.str] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_push_channel: typing.Optional[builtins.str] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
        wiki_page_channel: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project: ID of the project you want to activate integration on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#project ServiceSlack#project}
        :param webhook: Webhook URL (ex.: https://hooks.slack.com/services/...). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#webhook ServiceSlack#webhook}
        :param branches_to_be_notified: Branches to send notifications for. Valid options are "all", "default", "protected", and "default_and_protected". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#branches_to_be_notified ServiceSlack#branches_to_be_notified}
        :param confidential_issue_channel: The name of the channel to receive confidential issue events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issue_channel ServiceSlack#confidential_issue_channel}
        :param confidential_issues_events: Enable notifications for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issues_events ServiceSlack#confidential_issues_events}
        :param confidential_note_events: Enable notifications for confidential note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_note_events ServiceSlack#confidential_note_events}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#id ServiceSlack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issue_channel: The name of the channel to receive issue events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issue_channel ServiceSlack#issue_channel}
        :param issues_events: Enable notifications for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issues_events ServiceSlack#issues_events}
        :param merge_request_channel: The name of the channel to receive merge request events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_request_channel ServiceSlack#merge_request_channel}
        :param merge_requests_events: Enable notifications for merge requests events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_requests_events ServiceSlack#merge_requests_events}
        :param note_channel: The name of the channel to receive note events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_channel ServiceSlack#note_channel}
        :param note_events: Enable notifications for note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_events ServiceSlack#note_events}
        :param notify_only_broken_pipelines: Send notifications for broken pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_broken_pipelines ServiceSlack#notify_only_broken_pipelines}
        :param notify_only_default_branch: This parameter has been replaced with ``branches_to_be_notified``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_default_branch ServiceSlack#notify_only_default_branch}
        :param pipeline_channel: The name of the channel to receive pipeline events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_channel ServiceSlack#pipeline_channel}
        :param pipeline_events: Enable notifications for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_events ServiceSlack#pipeline_events}
        :param push_channel: The name of the channel to receive push events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_channel ServiceSlack#push_channel}
        :param push_events: Enable notifications for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_events ServiceSlack#push_events}
        :param tag_push_channel: The name of the channel to receive tag push events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_channel ServiceSlack#tag_push_channel}
        :param tag_push_events: Enable notifications for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_events ServiceSlack#tag_push_events}
        :param username: Username to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#username ServiceSlack#username}
        :param wiki_page_channel: The name of the channel to receive wiki page events notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_channel ServiceSlack#wiki_page_channel}
        :param wiki_page_events: Enable notifications for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_events ServiceSlack#wiki_page_events}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceSlackConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
            check_type(argname="argument branches_to_be_notified", value=branches_to_be_notified, expected_type=type_hints["branches_to_be_notified"])
            check_type(argname="argument confidential_issue_channel", value=confidential_issue_channel, expected_type=type_hints["confidential_issue_channel"])
            check_type(argname="argument confidential_issues_events", value=confidential_issues_events, expected_type=type_hints["confidential_issues_events"])
            check_type(argname="argument confidential_note_events", value=confidential_note_events, expected_type=type_hints["confidential_note_events"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issue_channel", value=issue_channel, expected_type=type_hints["issue_channel"])
            check_type(argname="argument issues_events", value=issues_events, expected_type=type_hints["issues_events"])
            check_type(argname="argument merge_request_channel", value=merge_request_channel, expected_type=type_hints["merge_request_channel"])
            check_type(argname="argument merge_requests_events", value=merge_requests_events, expected_type=type_hints["merge_requests_events"])
            check_type(argname="argument note_channel", value=note_channel, expected_type=type_hints["note_channel"])
            check_type(argname="argument note_events", value=note_events, expected_type=type_hints["note_events"])
            check_type(argname="argument notify_only_broken_pipelines", value=notify_only_broken_pipelines, expected_type=type_hints["notify_only_broken_pipelines"])
            check_type(argname="argument notify_only_default_branch", value=notify_only_default_branch, expected_type=type_hints["notify_only_default_branch"])
            check_type(argname="argument pipeline_channel", value=pipeline_channel, expected_type=type_hints["pipeline_channel"])
            check_type(argname="argument pipeline_events", value=pipeline_events, expected_type=type_hints["pipeline_events"])
            check_type(argname="argument push_channel", value=push_channel, expected_type=type_hints["push_channel"])
            check_type(argname="argument push_events", value=push_events, expected_type=type_hints["push_events"])
            check_type(argname="argument tag_push_channel", value=tag_push_channel, expected_type=type_hints["tag_push_channel"])
            check_type(argname="argument tag_push_events", value=tag_push_events, expected_type=type_hints["tag_push_events"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument wiki_page_channel", value=wiki_page_channel, expected_type=type_hints["wiki_page_channel"])
            check_type(argname="argument wiki_page_events", value=wiki_page_events, expected_type=type_hints["wiki_page_events"])
        self._values: typing.Dict[str, typing.Any] = {
            "project": project,
            "webhook": webhook,
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
        if branches_to_be_notified is not None:
            self._values["branches_to_be_notified"] = branches_to_be_notified
        if confidential_issue_channel is not None:
            self._values["confidential_issue_channel"] = confidential_issue_channel
        if confidential_issues_events is not None:
            self._values["confidential_issues_events"] = confidential_issues_events
        if confidential_note_events is not None:
            self._values["confidential_note_events"] = confidential_note_events
        if id is not None:
            self._values["id"] = id
        if issue_channel is not None:
            self._values["issue_channel"] = issue_channel
        if issues_events is not None:
            self._values["issues_events"] = issues_events
        if merge_request_channel is not None:
            self._values["merge_request_channel"] = merge_request_channel
        if merge_requests_events is not None:
            self._values["merge_requests_events"] = merge_requests_events
        if note_channel is not None:
            self._values["note_channel"] = note_channel
        if note_events is not None:
            self._values["note_events"] = note_events
        if notify_only_broken_pipelines is not None:
            self._values["notify_only_broken_pipelines"] = notify_only_broken_pipelines
        if notify_only_default_branch is not None:
            self._values["notify_only_default_branch"] = notify_only_default_branch
        if pipeline_channel is not None:
            self._values["pipeline_channel"] = pipeline_channel
        if pipeline_events is not None:
            self._values["pipeline_events"] = pipeline_events
        if push_channel is not None:
            self._values["push_channel"] = push_channel
        if push_events is not None:
            self._values["push_events"] = push_events
        if tag_push_channel is not None:
            self._values["tag_push_channel"] = tag_push_channel
        if tag_push_events is not None:
            self._values["tag_push_events"] = tag_push_events
        if username is not None:
            self._values["username"] = username
        if wiki_page_channel is not None:
            self._values["wiki_page_channel"] = wiki_page_channel
        if wiki_page_events is not None:
            self._values["wiki_page_events"] = wiki_page_events

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
    def project(self) -> builtins.str:
        '''ID of the project you want to activate integration on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#project ServiceSlack#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def webhook(self) -> builtins.str:
        '''Webhook URL (ex.: https://hooks.slack.com/services/...).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#webhook ServiceSlack#webhook}
        '''
        result = self._values.get("webhook")
        assert result is not None, "Required property 'webhook' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branches_to_be_notified(self) -> typing.Optional[builtins.str]:
        '''Branches to send notifications for. Valid options are "all", "default", "protected", and "default_and_protected".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#branches_to_be_notified ServiceSlack#branches_to_be_notified}
        '''
        result = self._values.get("branches_to_be_notified")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def confidential_issue_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive confidential issue events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issue_channel ServiceSlack#confidential_issue_channel}
        '''
        result = self._values.get("confidential_issue_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def confidential_issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for confidential issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_issues_events ServiceSlack#confidential_issues_events}
        '''
        result = self._values.get("confidential_issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def confidential_note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for confidential note events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#confidential_note_events ServiceSlack#confidential_note_events}
        '''
        result = self._values.get("confidential_note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#id ServiceSlack#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issue_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive issue events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issue_channel ServiceSlack#issue_channel}
        '''
        result = self._values.get("issue_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#issues_events ServiceSlack#issues_events}
        '''
        result = self._values.get("issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def merge_request_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive merge request events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_request_channel ServiceSlack#merge_request_channel}
        '''
        result = self._values.get("merge_request_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_requests_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for merge requests events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#merge_requests_events ServiceSlack#merge_requests_events}
        '''
        result = self._values.get("merge_requests_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def note_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive note events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_channel ServiceSlack#note_channel}
        '''
        result = self._values.get("note_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for note events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#note_events ServiceSlack#note_events}
        '''
        result = self._values.get("note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notify_only_broken_pipelines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Send notifications for broken pipelines.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_broken_pipelines ServiceSlack#notify_only_broken_pipelines}
        '''
        result = self._values.get("notify_only_broken_pipelines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notify_only_default_branch(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This parameter has been replaced with ``branches_to_be_notified``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#notify_only_default_branch ServiceSlack#notify_only_default_branch}
        '''
        result = self._values.get("notify_only_default_branch")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pipeline_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive pipeline events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_channel ServiceSlack#pipeline_channel}
        '''
        result = self._values.get("pipeline_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for pipeline events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#pipeline_events ServiceSlack#pipeline_events}
        '''
        result = self._values.get("pipeline_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def push_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive push events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_channel ServiceSlack#push_channel}
        '''
        result = self._values.get("push_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#push_events ServiceSlack#push_events}
        '''
        result = self._values.get("push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag_push_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive tag push events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_channel ServiceSlack#tag_push_channel}
        '''
        result = self._values.get("tag_push_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for tag push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#tag_push_events ServiceSlack#tag_push_events}
        '''
        result = self._values.get("tag_push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#username ServiceSlack#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_page_channel(self) -> typing.Optional[builtins.str]:
        '''The name of the channel to receive wiki page events notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_channel ServiceSlack#wiki_page_channel}
        '''
        result = self._values.get("wiki_page_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_page_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable notifications for wiki page events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_slack#wiki_page_events ServiceSlack#wiki_page_events}
        '''
        result = self._values.get("wiki_page_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceSlackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ServiceSlack",
    "ServiceSlackConfig",
]

publication.publish()
