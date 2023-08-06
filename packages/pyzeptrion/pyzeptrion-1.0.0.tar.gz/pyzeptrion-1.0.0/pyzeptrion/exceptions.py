"""All exceptions for the Zeptrion Python bindings."""


class ZeptrionError(Exception):
    """General ZeptrionError exception occurred."""


class ZeptrionConnectionError(ZeptrionError):
    """When a connection error is encountered."""
