# PrivX URLs.

from typing import Union

from privx_api.exceptions import InternalAPIException


class AuthEnum:
    AUTHORIZE = "AUTH.AUTHORIZE"
    TOKEN = "AUTH.TOKEN"

    urls = {
        AUTHORIZE: "/auth/api/v1/oauth/authorize",
        TOKEN: "/auth/api/v1/oauth/token",
    }


class HostStoreEnum:
    STATUS = "HOST_STORE.STATUS"
    HOSTS = "HOST_STORE.HOSTS"
    HOST = "HOST_STORE.HOST"
    SEARCH = "HOST_STORE.SEARCH"
    RESOLVE = "HOST_STORE.RESOLVE"
    DEPLOY = "HOST_STORE.DEPLOY"
    DEPLOYABLE = "HOST_STORE.DEPLOYABLE"
    DISABLE = "HOST_STORE.DISABLE"
    TAGS = "HOST_STORE.TAGS"
    REALM = "HOST_STORE.REALM"
    SETTINGS = "HOST_STORE.SETTINGS"

    urls = {
        STATUS: "/host-store/api/v1/status",
        HOSTS: "/host-store/api/v1/hosts",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        SEARCH: "/host-store/api/v1/hosts/search",
        RESOLVE: "/host-store/api/v1/hosts/resolve",
        DEPLOY: "/host-store/api/v1/hosts/deploy",
        DEPLOYABLE: "/host-store/api/v1/hosts/{host_id}/deployable",
        DISABLE: "/host-store/api/v1/hosts/{host_id}/disabled",
        TAGS: "/host-store/api/v1/hosts/tags",
        REALM: "/host-store/api/v1/realm/resolve",
        SETTINGS: "/host-store/api/v1/settings/default_service_options",
    }


class RoleStoreEnum:
    ALL_AUTHORIZED_KEYS = "ROLE_STORE.ALL_AUTHORIZED_KEYS"
    AWS_ROLE = "ROLE_STORE.AWS_ROLE"
    AWS_ROLES = "ROLE_STORE.AWS_ROLES"
    AWS_ROLE_PRIVX_ROLES = "ROLE_STORE.AWS_ROLE_PRIVX_ROLES"
    AWS_TOKEN = "ROLE_STORE.AWS_TOKEN"
    CURRENT_AWS_ROLES = "ROLE_STORE.CURRENT_AWS_ROLES"
    DISABLE_MFA = "ROLE_STORE.DISABLE_MFA"
    ENABLE_MFA = "ROLE_STORE.ENABLE_MFA"
    EVALUATE = "ROLE_STORE.EVALUATE"
    EXTERNAL_SEARCH = "ROLE_STORE.EXTERNAL_SEARCH"
    GENERATE_PRINCIPAL_KEY = "ROLE_STORE.GENERATE_PRINCIPAL_KEY"
    IMPORT_PRINCIPAL_KEY = "ROLE_STORE.IMPORT_PRINCIPAL_KEY"
    LOG_CONF_COLLECTOR = "ROLE_STORE.LOG_CONF_COLLECTOR"
    LOG_CONF_COLLECTORS = "ROLE_STORE.LOG_CONF_COLLECTORS"
    MEMBERS = "ROLE_STORE.MEMBERS"
    PRINCIPAL_KEY = "ROLE_STORE.PRINCIPAL_KEY"
    PRINCIPAL_KEYS = "ROLE_STORE.PRINCIPAL_KEYS"
    REFRESH_SOURCES = "ROLE_STORE.REFRESH_SOURCES"
    RESET_MFA = "ROLE_STORE.RESET_MFA"
    RESOLVE = "ROLE_STORE.RESOLVE"
    RESOLVE_AUTHORIZED_KEYS = "ROLE_STORE.RESOLVE_AUTHORIZED_KEYS"
    RESOLVE_USER = "ROLE_STORE.RESOLVE_USER"
    ROLE = "ROLE_STORE.ROLE"
    ROLES = "ROLE_STORE.ROLES"
    SEARCH_USERS = "ROLE_STORE.SEARCH_USERS"
    SOURCE = "ROLE_STORE.SOURCE"
    SOURCES = "ROLE_STORE.SOURCES"
    STATUS = "ROLE_STORE.STATUS"
    USERS = "ROLE_STORE.USERS"
    USER_AUTHORIZED_KEYS = "ROLE_STORE.USER_AUTHORIZED_KEYS"
    USER_AUTHORIZED_KEY_ID = "ROLE_STORE.USER_AUTHORIZED_KEY_ID"
    USER_ROLES = "ROLE_STORE.USER_ROLES"
    USER_SETTINGS = "ROLE_STORE.USER_SETTINGS"

    urls = {
        ALL_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys",
        AWS_ROLE: "/role-store/api/v1/awsroles/{awsrole_id}",
        AWS_ROLES: "/role-store/api/v1/awsroles",
        AWS_ROLE_PRIVX_ROLES: "/role-store/api/v1/awsroles/{awsrole_id}/roles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        CURRENT_AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        DISABLE_MFA: "/role-store/api/v1/users/mfa/disable",
        ENABLE_MFA: "/role-store/api/v1/users/mfa/enable",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        EXTERNAL_SEARCH: "/role-store/api/v1/users/search/external",
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/generate",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        LOG_CONF_COLLECTOR: "/role-store/api/v1/logconf/collectors/{collector_id}",
        LOG_CONF_COLLECTORS: "/role-store/api/v1/logconf/collectors",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/{key_id}",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        REFRESH_SOURCES: "/role-store/api/v1/sources/refresh",
        RESET_MFA: "/role-store/api/v1/users/mfa/reset",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        RESOLVE_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys/resolve",
        RESOLVE_USER: "/role-store/api/v1/users/{user_id}/resolve",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        ROLES: "/role-store/api/v1/roles",
        SEARCH_USERS: "/role-store/api/v1/users/search",
        SOURCE: "/role-store/api/v1/sources/{source_id}",
        SOURCES: "/role-store/api/v1/sources",
        STATUS: "/role-store/api/v1/status",
        USERS: "/role-store/api/v1/users/{user_id}",
        USER_AUTHORIZED_KEYS: "/role-store/api/v1/users/{user_id}/authorizedkeys",
        USER_AUTHORIZED_KEY_ID: "/role-store/api/v1/users/{user_id}/authorizedkeys/{key_id}",
        USER_ROLES: "/role-store/api/v1/users/{user_id}/roles",
        USER_SETTINGS: "/role-store/api/v1/users/{user_id}/settings",
    }


class UserStoreEnum:
    STATUS = "USER_STORE.STATUS"
    USERS = "USER_STORE.USERS"
    USER = "USER_STORE.USER"
    PASSWORD = "USER_STORE.PASSWORD"
    TAGS = "USER_STORE.TAGS"
    TRUSTED_CLIENTS = "USER_STORE.TRUSTED_CLIENTS"
    TRUSTED_CLIENT = "USER_STORE.TRUSTED_CLIENT"
    EXTENDER_CLIENTS = "USER_STORE.EXTENDER_CLIENTS"
    API_CLIENTS = "USER_STORE.API_CLIENTS"
    API_CLIENT = "USER_STORE.API_CLIENT"

    urls = {
        STATUS: "/local-user-store/api/v1/status",
        USERS: "/local-user-store/api/v1/users",
        USER: "/local-user-store/api/v1/users/{user_id}",
        PASSWORD: "/local-user-store/api/v1/users/{user_id}/password",
        TAGS: "/local-user-store/api/v1/users/tags",
        TRUSTED_CLIENTS: "/local-user-store/api/v1/trusted-clients",
        TRUSTED_CLIENT: "/local-user-store/api/v1/trusted-clients/{trusted_client_id}",
        EXTENDER_CLIENTS: "/local-user-store/api/v1/extender-clients",
        API_CLIENTS: "/local-user-store/api/v1/api-clients",
        API_CLIENT: "/local-user-store/api/v1/api-clients/{api_client_id}",
    }


class ConnectionManagerEnum:
    SEARCH = "CONNECTION_MANAGER.SEARCH"

    urls = {SEARCH: "/connection-manager/api/v1/connections/search"}


class VaultEnum:
    STATUS = "VAULT.STATUS"
    SECRETS = "VAULT.SECRETS"
    SECRET = "VAULT.SECRET"
    METADATA = "VAULT.METADATA"
    SEARCH = "VAULT.SEARCH"
    SCHEMAS = "VAULT.SCHEMAS"

    urls = {
        STATUS: "/vault/api/v1/status",
        SECRETS: "/vault/api/v1/secrets",
        SECRET: "/vault/api/v1/secrets/{name}",
        METADATA: "/vault/api/v1/metadata/secrets/{name}",
        SEARCH: "/vault/api/v1/search/secrets",
        SCHEMAS: "/vault/api/v1/schemas",
    }


class LicenseManagerEnum:
    STATUS = "LICENSE_MANAGER.STATUS"
    LICENSE = "LICENSE_MANAGER.LICENSE"
    REFRESH = "LICENSE_MANAGER.REFRESH"
    OPT_IN = "LICENSE_MANAGER.OPT_IN"
    DEACTIVATE = "LICENSE_MANAGER.DEACTIVATE"

    urls = {
        STATUS: "/license-manager/api/v1/status",
        LICENSE: "/license-manager/api/v1/license",
        REFRESH: "/license-manager/api/v1/license/refresh",
        OPT_IN: "/license-manager/api/v1/license/optin",
        DEACTIVATE: "/license-manager/api/v1/license/deactivate",
    }


class MonitorServiceEnum:
    STATUS = "MONITOR.STATUS"
    COMPONENTS = "MONITOR.COMPONENTS"
    COMPONENT = "MONITOR.COMPONENT"
    SEARCH_AUDIT_EVENTS = "MONITOR.SEARCH_AUDIT_EVENTS"
    AUDIT_EVENTS = "MONITOR.AUDIT_EVENTS"
    AUDIT_EVENT_CODES = "MONITOR.AUDIT_EVENT_CODES"
    INSTANCE_STATUS = "MONITOR.INSTANCE_STATUS"
    TERMINATE_INSTANCES = "MONITOR.TERMINATE_INSTANCES"

    urls = {
        STATUS: "/monitor-service/api/v1/status",
        COMPONENTS: "/monitor-service/api/v1/components",
        COMPONENT: "/monitor-service/api/v1/components/{hostname}",
        SEARCH_AUDIT_EVENTS: "/monitor-service/api/v1/auditevents/search",
        AUDIT_EVENTS: "/monitor-service/api/v1/auditevents",
        AUDIT_EVENT_CODES: "/monitor-service/api/v1/auditevents/codes",
        INSTANCE_STATUS: "/monitor-service/api/v1/instance/status",
        TERMINATE_INSTANCES: "/monitor-service/api/v1/instance/exit",
    }


class PrivXSettingsEnum:
    STATUS = "SETTINGS.STATUS"
    SCOPE = "SETTINGS.SCOPE"
    SCOPE_SECTION = "SETTINGS.SCOPE_SECTION"
    SCOPE_SCHEMA = "SETTINGS.SCOPE_SCHEMA"
    SCOPE_SECTION_SCHEMA = "SETTINGS.SCOPE_SECTION_SCHEMA"

    urls = {
        STATUS: "/settings/api/v1/status",
        SCOPE: "/settings/api/v1/settings/{scope}",
        SCOPE_SECTION: "/settings/api/v1/settings/{scope}/{section}",
        SCOPE_SCHEMA: "/settings/api/v1/schema/{scope}",
        SCOPE_SECTION_SCHEMA: "/settings/api/v1/schema/{scope}/{section}",
    }


class WokFlowEngineEnum:
    STATUS = "WORKFLOW_ENGINE.STATUS"
    WORKFLOWS = "WORKFLOW_ENGINE.WORKFLOWS"
    WORKFLOW = "WORKFLOW_ENGINE.WORKFLOW"
    REQUESTS = "WORKFLOW_ENGINE.REQUESTS"
    REQUEST = "WORKFLOW_ENGINE.REQUEST"
    DECISION = "WORKFLOW_ENGINE.DECISION"
    SEARCH_REQUESTS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    SETTINGS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    TEST_SETTINGS = "WORKFLOW_ENGINE.TEST_SETTINGS"

    urls = {
        STATUS: "/workflow-engine/api/v1/status",
        WORKFLOWS: "/workflow-engine/api/v1/workflows",
        WORKFLOW: "/workflow-engine/api/v1/workflows/{workflow_id}",
        REQUESTS: "/workflow-engine/api/v1/requests",
        REQUEST: "/workflow-engine/api/v1/requests/{request_id}",
        DECISION: "/workflow-engine/api/v1/requests/{request_id}/decision",
        SEARCH_REQUESTS: "/workflow-engine/api/v1/requests/search",
        SETTINGS: "/workflow-engine/api/v1/settings",
        TEST_SETTINGS: "/workflow-engine/api/v1/testsmtp",
    }


class UrlEnum:
    AUTH = AuthEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    MONITOR = MonitorServiceEnum
    ROLE_STORE = RoleStoreEnum
    SETTINGS = PrivXSettingsEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum
    LICENSE = LicenseManagerEnum
    WORKFLOW_ENGINE = WokFlowEngineEnum

    @classmethod
    def get(cls, url_name: str) -> Union[str, None]:
        """
        looking for required url name among inner enums
        Args:
            url_name: str e.g. 'TOKEN'
        Returns:
            str e.g.'/auth/api/v1/oauth/token'
            None if url name not found
        """

        list_urls = list(
            filter(
                lambda inner_enum: inner_enum.urls.get(url_name),
                (
                    val
                    for key, val in cls.__dict__.items()
                    if key == key.upper() and not key.startswith("__")
                ),
            )
        )
        if len(list_urls) != 1:
            raise InternalAPIException
        return list_urls[0].urls.get(url_name)
