from dataclasses import dataclass

@dataclass
class VisitorContext:
    '''
    Provides the context for a page display. Contains data scraped from the visitor's client.
    '''

    remote_address: str = None
    '''
    The remote address of the visitor's client.
    '''

    addr_chain: list[str] = remote_address
    '''
    The entire chain of addresses, in order, gathered from the contents of the `X-Forwarded-By` header.
    '''

    scraped_cookies: list[str] = None
    '''
    The contents of any cookies extracted from the user's client.
    '''
    
    user_agent: str = None
    '''
    The client user-agent.
    '''

    other_headers: dict[str] = None
    '''
    A dictionary keyed with any other headers in the request.
    '''